/**
 * Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2023-2026.
 *
 * @if Eng
 * @brief Implements the BLE UART bridge GATT server.
 * @else
 * @brief 实现 BLE UART 透传 GATT 服务端。
 * @endif
 *
 * History: \n
 * 2026-07-25, Create file. \n
 */

#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include "securec.h"
#include "soc_osal.h"
#include "common_def.h"
#include "bts_device_manager.h"
#include "bts_def.h"
#include "bts_le_gap.h"
#include "bts_gatt_stru.h"
#include "bts_gatt_server.h"
#include "ble_uart_bridge.h"
#include "ble_uart_bridge_server.h"
#include "ble_uart_bridge_server_adv.h"

/* UART bridge service identity. / UART 透传服务标识。 */
#define BLE_UART_BRIDGE_SERVER_LOG "[ble uart bridge server]"
#define BLE_UART_BRIDGE_UUID_LEN 2

/* GATT handles, connection state, and data values. / GATT 句柄、连接状态与数据值。 */
static uint8_t g_server_id;
static uint16_t g_conn_id;
static uint16_t g_service_handle;
static uint16_t g_data_handle;
static uint16_t g_notify_handle;
static uint16_t g_notify_cccd_handle;
static volatile bool g_connected;
static volatile bool g_hello_notify_enabled;
static volatile bool g_handshake_indication_pending;
static volatile uint16_t g_att_mtu = SDK_BLE_MTU_MIN;
static osal_semaphore g_ble_enable_sem;
static volatile bool g_ble_enable_sem_ready;
static volatile uint8_t g_ble_enable_status = BT_ENABLE_DISABLE_FAIL;
static const bd_addr_t g_ble_uart_bridge_addr = {
    .addr = {0x44, 0x44, 0x55, 0x41, 0x52, 0x63},
    .type = BT_ADDRESS_TYPE_PUBLIC_DEVICE_ADDRESS,
};
static uint8_t g_property_value[BLE_UART_BRIDGE_PROPERTY_MAX_LEN] = "uart_ready";
static uint16_t g_property_value_len = sizeof("uart_ready") - 1;
/* The SDK response path requires a nonzero copy span even when an ATT Write Response has no value. */
static uint8_t g_empty_response_value;
static const uint8_t DEFAULT_VALUE[] = "uart_ready";
static const uint8_t HELLO_MESSAGE[] = "uart_from_peripheral";
#define BLE_UUID_HIGH_BYTE_SHIFT 8
#define BLE_CCCD_VALUE_LEN 2
#define BLE_CCCD_INDICATE_ENABLED 2
#define BLE_ATT_PROTOCOL_OVERHEAD 3
#define BLE_ATT_READ_RESPONSE_OVERHEAD 1
#define BLE_UART_BRIDGE_PREFERRED_MTU (BLE_UART_BRIDGE_BLE_PAYLOAD_MAX_LEN + BLE_ATT_PROTOCOL_OVERHEAD)
#define BLE_UART_BRIDGE_SERVER_STARTUP_DELAY_MS 1000U
#define BLE_UART_BRIDGE_ENABLE_TIMEOUT_MS 5000

/**
 * @if Eng
 * @brief Describes the payload used to send one GATT response.
 * @else
 * @brief 描述发送一条 GATT 响应所需的数据。
 * @endif
 */
typedef struct {
    uint16_t request_id;
    uint8_t status;
    uint16_t offset;
    uint8_t *value;
    uint16_t value_len;
} ble_uart_bridge_response_t;

/**
 * @if Eng
 * @brief Declares the helper used to send an indication value.
 * @else
 * @brief 声明用于发送指示值的内部辅助接口。
 * @endif
 */
static errcode_t ble_uart_bridge_send_value_notification(uint16_t handle,
                                                         const uint8_t *data,
                                                         uint16_t len,
                                                         const char *name);

/**
 * @if Eng
 * @brief Converts a 16-bit value to the SDK Bluetooth UUID representation.
 * @else
 * @brief 将 16 位数值转换为 SDK 蓝牙 UUID 表示形式。
 * @endif
 */
static void ble_uart_bridge_uuid16(uint16_t value, bt_uuid_t *uuid)
{
    /* The SDK represents 16-bit UUID bytes in high-byte-first order. / SDK 的 16 位 UUID 字节按高字节在前表示。 */
    uuid->uuid_len = BLE_UART_BRIDGE_UUID_LEN;
    uuid->uuid[0] = (uint8_t)(value >> BLE_UUID_HIGH_BYTE_SHIFT);
    uuid->uuid[1] = (uint8_t)value;
}

/**
 * @if Eng
 * @brief Sends a GATT response for a read or write request.
 * @else
 * @brief 为 GATT 读写请求发送响应。
 * @endif
 */
static errcode_t ble_uart_bridge_send_response(uint8_t server_id,
                                               uint16_t conn_id,
                                               const ble_uart_bridge_response_t *response_data)
{
    gatts_send_rsp_t response = {0};
    /* This sample always returns the complete value, so the response starts at offset zero. / 本案例始终返回完整值，偏移为零。 */
    response.request_id = response_data->request_id;
    response.status = response_data->status;
    response.offset = response_data->offset;
    response.value = response_data->value;
    response.value_len = response_data->value_len;
    if (response.value_len == 0) {
        /* The SDK copies before request dispatch and rejects zero-sized memcpy_s. / SDK 分发请求前先复制，拒绝零长度 memcpy_s。 */
        response.value = &g_empty_response_value;
        response.value_len = sizeof(g_empty_response_value);
    }
    return gatts_send_response(server_id, conn_id, &response);
}

/**
 * @if Eng
 * @brief Handles reads of the UART data characteristic.
 * @else
 * @brief 处理 UART 数据特征的读取请求。
 * @endif
 */
static void ble_uart_bridge_read_request_cb(uint8_t server_id,
                                            uint16_t conn_id,
                                            gatts_req_read_cb_t *request,
                                            errcode_t status)
{
    uint16_t response_len;
    uint16_t read_max;

    osal_printk("%s read request received, handle=0x%04x\r\n", BLE_UART_BRIDGE_SERVER_LOG, request->handle);
    if (!request->need_rsp) {
        /* The stack does not expect an ATT response for this request type. / 当前请求类型无需返回 ATT 响应。 */
        return;
    }

    if (status != ERRCODE_BT_SUCCESS) {
        ble_uart_bridge_response_t response = {
            request->request_id, GATT_STATUS_UNLIKELY_ERROR, request->offset, NULL, 0
        };
        (void)ble_uart_bridge_send_response(server_id, conn_id, &response);
        return;
    }
    if (request->handle != g_data_handle) {
        /* Never expose the cached UART value through an unrelated handle. / 不允许通过无关句柄读取缓存的 UART 数据。 */
        ble_uart_bridge_response_t response = {
            request->request_id, GATT_STATUS_INVALID_HANDLE, request->offset, NULL, 0
        };
        (void)ble_uart_bridge_send_response(server_id, conn_id, &response);
        return;
    }
    if (request->offset >= g_property_value_len) {
        ble_uart_bridge_response_t response = {
            request->request_id, GATT_STATUS_INVALID_OFFSET, request->offset, NULL, 0
        };
        (void)ble_uart_bridge_send_response(server_id, conn_id, &response);
        return;
    }

    response_len = (uint16_t)(g_property_value_len - request->offset);
    read_max = g_att_mtu > BLE_ATT_READ_RESPONSE_OVERHEAD ?
        (uint16_t)(g_att_mtu - BLE_ATT_READ_RESPONSE_OVERHEAD) : 0;
    if (response_len > read_max) {
        response_len = read_max;
    }
    ble_uart_bridge_response_t response = {
        request->request_id, GATT_STATUS_SUCCESS, request->offset,
        &g_property_value[request->offset], response_len
    };
    if (ble_uart_bridge_send_response(server_id, conn_id, &response) == ERRCODE_BT_SUCCESS) {
        osal_printk("%s read response sent: offset=%u, bytes=%u\r\n", BLE_UART_BRIDGE_SERVER_LOG,
                    request->offset, response_len);
    }
}

/**
 * @if Eng
 * @brief Validates a CCCD write and updates the indication state.
 * @else
 * @brief 校验 CCCD 写请求并更新指示使能状态。
 * @endif
 */
static void ble_uart_bridge_handle_cccd_write(uint8_t server_id, uint16_t conn_id, gatts_req_write_cb_t *request)
{
    uint16_t cccd_value = 0;
    uint8_t response_status = GATT_STATUS_SUCCESS;
    errcode_t ret;

    if (request->is_prep) {
        response_status = GATT_STATUS_REQUEST_NOT_SUPPORTED;
    } else if (request->offset != 0) {
        response_status = GATT_STATUS_INVALID_OFFSET;
    } else if (request->value == NULL || request->length != BLE_CCCD_VALUE_LEN) {
        response_status = GATT_STATUS_INVALID_ATTRIBUTE_VALUE_LENGTH;
    } else {
        /* CCCD is a little-endian 16-bit bitmask. / CCCD 是小端序的 16 位位图。 */
        cccd_value = (uint16_t)request->value[0] | ((uint16_t)request->value[1] << BLE_UUID_HIGH_BYTE_SHIFT);
        /* Accept only disabled (0x0000) or indication enabled (0x0002). / 仅接受禁用或使能指示。 */
        if (cccd_value != 0 && cccd_value != BLE_CCCD_INDICATE_ENABLED) {
            response_status = GATT_STATUS_VALUE_NOT_ALLOWED;
        }
    }

    if (request->need_rsp) {
        /* A CCCD Write Request must be acknowledged before changing local state. / CCCD 写请求需先应答再更新本地状态。 */
        ble_uart_bridge_response_t response = {request->request_id, response_status, 0, NULL, 0};
        (void)ble_uart_bridge_send_response(server_id, conn_id, &response);
    }
    if (response_status != GATT_STATUS_SUCCESS) {
        osal_printk("%s invalid CCCD write, status=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, response_status);
        return;
    }

    /* Update the subscription gate only after value validation succeeds. / 仅在校验成功后更新订阅门控。 */
    g_hello_notify_enabled = (cccd_value == BLE_CCCD_INDICATE_ENABLED);
    osal_printk("%s UART RX indication CCCD %s\r\n", BLE_UART_BRIDGE_SERVER_LOG,
                g_hello_notify_enabled ? "enabled" : "disabled");
    if (g_hello_notify_enabled) {
        /* The initial indication confirms the data path and starts the client handshake. / 首个指示用于确认通道并启动客户端握手。 */
        g_handshake_indication_pending = true;
        ret = ble_uart_bridge_server_send_notification(HELLO_MESSAGE, sizeof(HELLO_MESSAGE) - 1);
        if (ret != ERRCODE_BT_SUCCESS) {
            g_handshake_indication_pending = false;
        }
    } else {
        g_handshake_indication_pending = false;
        /* Preserve any unconfirmed UART bytes until the peer subscribes again. */
        ble_uart_bridge_ble_send_complete(ERRCODE_BT_FAIL);
    }
    ble_uart_bridge_ble_state_changed();
}

/**
 * @if Eng
 * @brief Validates and queues one data characteristic write.
 * @else
 * @brief 校验一条数据特征写请求并将其加入 UART 发送队列。
 * @endif
 */
static uint8_t ble_uart_bridge_process_data_write(const gatts_req_write_cb_t *request)
{
    if (request->is_prep) {
        return GATT_STATUS_REQUEST_NOT_SUPPORTED;
    }
    if (request->offset != 0) {
        return GATT_STATUS_INVALID_OFFSET;
    }
    if (request->handle != g_data_handle) {
        return GATT_STATUS_INVALID_HANDLE;
    }
    if (request->value == NULL || request->length == 0 ||
        request->length > BLE_UART_BRIDGE_PROPERTY_MAX_LEN) {
        return GATT_STATUS_INVALID_ATTRIBUTE_VALUE_LENGTH;
    }
    if (ble_uart_bridge_uart_enqueue(request->value, request->length) != ERRCODE_BT_SUCCESS) {
        /* Report backpressure when the UART queue has no room. / UART 队列空间不足时返回资源不足。 */
        return GATT_STATUS_INSUFFICIENT_RESOURCES;
    }

    /* Update the readable cache only after the complete fragment is queued for UART. / 完整分片成功入队后再更新可读缓存。 */
    (void)memset_s(g_property_value, sizeof(g_property_value), 0, sizeof(g_property_value));
    if (memcpy_s(g_property_value, sizeof(g_property_value), request->value, request->length) != EOK) {
        return GATT_STATUS_UNLIKELY_ERROR;
    }
    g_property_value_len = request->length;
    return GATT_STATUS_SUCCESS;
}

/**
 * @if Eng
 * @brief Sends an ATT response when the peer used a Write Request.
 * @else
 * @brief 当对端使用写请求时发送 ATT 应答。
 * @endif
 */
static void ble_uart_bridge_send_write_response(uint8_t server_id,
                                                uint16_t conn_id,
                                                const gatts_req_write_cb_t *request,
                                                uint8_t response_status)
{
    ble_uart_bridge_response_t response;
    errcode_t response_ret;

    if (!request->need_rsp) {
        return;
    }
    response = (ble_uart_bridge_response_t){request->request_id, response_status, 0, NULL, 0};
    response_ret = ble_uart_bridge_send_response(server_id, conn_id, &response);
    if (response_ret != ERRCODE_BT_SUCCESS) {
        /* A failed ATT response stalls the client's single-flight Write Request queue. / ATT 应答失败会阻塞客户端的单请求发送队列。 */
        osal_printk("%s write response failed: ret=0x%x, request_id=%u, offset=%u, authorize=%u, prepare=%u\r\n",
                    BLE_UART_BRIDGE_SERVER_LOG, response_ret, request->request_id, request->offset,
                    request->need_authorize, request->is_prep);
    }
}

/**
 * @if Eng
 * @brief Queues data characteristic writes for UART transmission.
 * @else
 * @brief 将数据特征写入内容加入 UART 发送队列。
 * @endif
 */
static void ble_uart_bridge_write_request_cb(uint8_t server_id,
                                             uint16_t conn_id,
                                             gatts_req_write_cb_t *request,
                                             errcode_t status)
{
    uint8_t response_status;

    if (status != ERRCODE_BT_SUCCESS) {
        /* Preserve the ATT request metadata when the stack reports a callback error. / 协议栈回调异常时保留 ATT 请求元数据。 */
        osal_printk("%s write callback failed: ret=0x%x, request_id=%u, need_rsp=%u, authorize=%u, prepare=%u\r\n",
                    BLE_UART_BRIDGE_SERVER_LOG, status, request->request_id, request->need_rsp,
                    request->need_authorize, request->is_prep);
        response_status = GATT_STATUS_UNLIKELY_ERROR;
    } else {
        osal_printk("%s write request received, handle=0x%04x, len=%u\r\n", BLE_UART_BRIDGE_SERVER_LOG,
                    request->handle, request->length);
        if (request->handle == g_notify_cccd_handle) {
            /* CCCD writes configure indications and are not UART payload. / CCCD 写用于配置指示，不属于 UART 载荷。 */
            ble_uart_bridge_handle_cccd_write(server_id, conn_id, request);
            return;
        }
        response_status = ble_uart_bridge_process_data_write(request);
    }

    /* Write Commands skip this response, while Write Requests receive the mapped status. / 写命令无响应，写请求返回映射状态。 */
    ble_uart_bridge_send_write_response(server_id, conn_id, request, response_status);
    if (response_status == GATT_STATUS_SUCCESS) {
        /* Mirror the cached-value state into future advertisements for reconnect recovery. / 将缓存状态同步到后续广播以支持重连恢复。 */
        ble_uart_bridge_server_set_adv_default_state(
            g_property_value_len == sizeof(DEFAULT_VALUE) - 1 &&
            memcmp(g_property_value, DEFAULT_VALUE, sizeof(DEFAULT_VALUE) - 1) == 0);
        osal_printk("%s BLE write queued to UART TX: bytes=%u\r\n", BLE_UART_BRIDGE_SERVER_LOG,
                    g_property_value_len);
    } else {
        osal_printk("%s write rejected, status=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, response_status);
    }
}

/**
 * @if Eng
 * @brief Adds the readable and writable UART data characteristic.
 * @else
 * @brief 添加支持读写的 UART 数据特征。
 * @endif
 */
static errcode_t ble_uart_bridge_add_data_characteristic(void)
{
    bt_uuid_t data_uuid = {0};
    gatts_add_chara_info_t characteristic = {0};
    gatts_add_character_result_t data_result = {0};

    ble_uart_bridge_uuid16(BLE_UART_BRIDGE_DATA_UUID, &data_uuid);
    characteristic.chara_uuid = data_uuid;
    /* Support both control Write Requests and high-throughput UART Write Commands. / 同时支持控制写请求和高吞吐 UART 写命令。 */
    characteristic.properties = GATT_CHARACTER_PROPERTY_BIT_READ | GATT_CHARACTER_PROPERTY_BIT_WRITE |
                                GATT_CHARACTER_PROPERTY_BIT_WRITE_NO_RSP;
    /* Require an encrypted link; Mode 1 Level 2 triggers Just Works pairing when needed. */
    characteristic.permissions =
        GATT_ATTRIBUTE_PERMISSION_READ | GATT_ATTRIBUTE_PERMISSION_WRITE | GATT_ATTRIBUTE_PERMISSION_ENCRYPTION_NEED;
    characteristic.value = g_property_value;
    characteristic.value_len = g_property_value_len;
    errcode_t ret = gatts_add_characteristic_sync(g_server_id, g_service_handle, &characteristic, &data_result);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    g_data_handle = data_result.value_handle;
    return ERRCODE_BT_SUCCESS;
}

/**
 * @if Eng
 * @brief Adds the UART indication characteristic and its CCCD.
 * @else
 * @brief 添加 UART 指示特征及其 CCCD。
 * @endif
 */
static errcode_t ble_uart_bridge_add_notify_characteristic(void)
{
    bt_uuid_t notify_uuid = {0};
    bt_uuid_t cccd_uuid = {0};
    gatts_add_chara_info_t characteristic = {0};
    gatts_add_character_result_t notify_result = {0};
    gatts_add_desc_info_t descriptor = {0};
    uint8_t cccd_value[BLE_CCCD_VALUE_LEN] = {0};

    ble_uart_bridge_uuid16(BLE_UART_BRIDGE_NOTIFY_UUID, &notify_uuid);
    characteristic.chara_uuid = notify_uuid;
    /* Indications provide an explicit confirmation used to advance the UART RX ring safely. / 指示确认用于安全推进 UART 接收队列。 */
    characteristic.properties = GATT_CHARACTER_PROPERTY_BIT_INDICATE;
    characteristic.permissions = GATT_ATTRIBUTE_PERMISSION_READ | GATT_ATTRIBUTE_PERMISSION_ENCRYPTION_NEED;
    characteristic.value = (uint8_t *)HELLO_MESSAGE;
    characteristic.value_len = sizeof(HELLO_MESSAGE) - 1;
    errcode_t ret = gatts_add_characteristic_sync(g_server_id, g_service_handle, &characteristic, &notify_result);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    g_notify_handle = notify_result.value_handle;

    /* CCCD lets the client explicitly enable or disable indication delivery. / CCCD 允许客户端显式控制指示发送。 */
    ble_uart_bridge_uuid16(BLE_UART_BRIDGE_CCCD_UUID, &cccd_uuid);
    descriptor.desc_uuid = cccd_uuid;
    descriptor.permissions = GATT_ATTRIBUTE_PERMISSION_READ | GATT_ATTRIBUTE_PERMISSION_WRITE |
                             GATT_ATTRIBUTE_PERMISSION_ENCRYPTION_NEED;
    descriptor.value = cccd_value;
    descriptor.value_len = sizeof(cccd_value);
    ret = gatts_add_descriptor_sync(g_server_id, g_service_handle, &descriptor, &g_notify_cccd_handle);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    return ERRCODE_BT_SUCCESS;
}

/**
 * @if Eng
 * @brief Registers and starts the UART bridge GATT service.
 * @else
 * @brief 注册并启动 UART 透传 GATT 服务。
 * @endif
 */
static errcode_t ble_uart_bridge_add_gatt_service(void)
{
    bt_uuid_t app_uuid = {0};
    bt_uuid_t service_uuid = {0};

    /* Register the application before creating attributes owned by its server ID. / 创建属性前先注册应用并获取服务端 ID。 */
    ble_uart_bridge_uuid16(BLE_UART_BRIDGE_SERVICE_UUID, &app_uuid);
    errcode_t ret = gatts_register_server(&app_uuid, &g_server_id);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    ret = gatts_set_mtu_size(g_server_id, BLE_UART_BRIDGE_PREFERRED_MTU);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    ble_uart_bridge_uuid16(BLE_UART_BRIDGE_SERVICE_UUID, &service_uuid);
    ret = gatts_add_service_sync(g_server_id, &service_uuid, true, &g_service_handle);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    /* Build the service in dependency order: service, data value, indication value, then CCCD. / 按依赖顺序构建服务。 */
    ret = ble_uart_bridge_add_data_characteristic();
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }
    ret = ble_uart_bridge_add_notify_characteristic();
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }

    osal_printk("%s service ready: service=0x%04x data=0x%04x notify=0x%04x notify_cccd=0x%04x\r\n",
                BLE_UART_BRIDGE_SERVER_LOG, g_service_handle, g_data_handle, g_notify_handle, g_notify_cccd_handle);
    return gatts_start_service(g_server_id, g_service_handle);
}

/**
 * @if Eng
 * @brief Starts advertising after the GATT service becomes available.
 * @else
 * @brief 在 GATT 服务就绪后启动广播。
 * @endif
 */
static void ble_uart_bridge_service_start_cb(uint8_t server_id, uint16_t handle, errcode_t status)
{
    if (server_id != g_server_id || handle != g_service_handle) {
        return;
    }
    if (status != ERRCODE_BT_SUCCESS) {
        osal_printk("%s service start failed: 0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, status);
        return;
    }
    /* Advertising starts only after every characteristic and descriptor is active. / 全部特征和描述符生效后才开始广播。 */
    if (ble_uart_bridge_server_start_adv() == ERRCODE_BT_SUCCESS) {
        osal_printk("%s advertising started: ble_uart_bridge_server\r\n", BLE_UART_BRIDGE_SERVER_LOG);
    } else {
        osal_printk("%s advertising start failed\r\n", BLE_UART_BRIDGE_SERVER_LOG);
    }
}

/**
 * @if Eng
 * @brief Tracks connection state and restarts advertising after disconnection.
 * @else
 * @brief 跟踪连接状态并在断开后重新启动广播。
 * @endif
 */
static void ble_uart_bridge_conn_state_cb(uint16_t conn_id,
                                          bd_addr_t *addr,
                                          gap_ble_conn_state_t conn_state,
                                          gap_ble_pair_state_t pair_state,
                                          gap_ble_disc_reason_t reason)
{
    (void)addr;
    (void)pair_state;
    if (conn_state == GAP_BLE_STATE_CONNECTED) {
        /* CCCD subscription is connection-specific and must start disabled on every link. / CCCD 订阅属于单次连接，重连后需重置。 */
        g_conn_id = conn_id;
        g_connected = true;
        g_hello_notify_enabled = false;
        g_handshake_indication_pending = false;
        g_att_mtu = SDK_BLE_MTU_MIN;
        osal_printk("%s connected, conn_id=0x%04x\r\n", BLE_UART_BRIDGE_SERVER_LOG, conn_id);
        if (gatts_exchange_mtu_req(conn_id, BLE_UART_BRIDGE_PREFERRED_MTU) != ERRCODE_BT_SUCCESS) {
            osal_printk("%s MTU exchange request failed\r\n", BLE_UART_BRIDGE_SERVER_LOG);
        }
    } else if (conn_state == GAP_BLE_STATE_DISCONNECTED) {
        /* Fail the in-flight indication without consuming its bytes. / 将在途指示标记失败但不消费数据。 */
        /* The worker can retry the same bytes after reconnecting. / 重连后任务可重试相同数据。 */
        g_connected = false;
        g_hello_notify_enabled = false;
        g_handshake_indication_pending = false;
        g_att_mtu = SDK_BLE_MTU_MIN;
        ble_uart_bridge_ble_send_complete(ERRCODE_BT_FAIL);
        ble_uart_bridge_ble_state_changed();
        /* Resume discoverability automatically after the active link is released. / 当前连接释放后自动恢复可发现状态。 */
        osal_printk("%s disconnected, reason=0x%x, re-advertising\r\n", BLE_UART_BRIDGE_SERVER_LOG, reason);
        (void)ble_uart_bridge_server_start_adv();
    }
}

static void ble_uart_bridge_mtu_changed_cb(uint8_t server_id, uint16_t conn_id, uint16_t mtu_size, errcode_t status)
{
    if (server_id != g_server_id || conn_id != g_conn_id || status != ERRCODE_BT_SUCCESS ||
        mtu_size < SDK_BLE_MTU_MIN) {
        return;
    }
    g_att_mtu = mtu_size;
    osal_printk("%s ATT MTU updated: %u\r\n", BLE_UART_BRIDGE_SERVER_LOG, mtu_size);
    ble_uart_bridge_ble_state_changed();
}

/**
 * @if Eng
 * @brief Reports completion of one confirmed UART-data indication.
 * @else
 * @brief 上报一包 UART 数据指示的确认结果。
 * @endif
 */
static void ble_uart_bridge_indication_confirm_cb(uint8_t server_id, uint16_t conn_id, errcode_t status)
{
    /* Ignore confirmations belonging to another server instance or an obsolete connection. / 忽略其他实例或旧连接的确认。 */
    if (server_id == g_server_id && conn_id == g_conn_id) {
        if (g_handshake_indication_pending) {
            g_handshake_indication_pending = false;
            ble_uart_bridge_ble_state_changed();
            return;
        }
        ble_uart_bridge_ble_send_complete(status);
    }
}

/**
 * @if Eng
 * @brief Handles pairing completion and removes stale pairing information on failure.
 * @else
 * @brief 处理配对完成事件，并在失败时删除陈旧配对信息。
 * @endif
 */
static void ble_uart_bridge_pair_result_cb(uint16_t conn_id, const bd_addr_t *addr, errcode_t status)
{
    osal_printk("%s pair complete, conn_id=0x%04x, status=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, conn_id, status);
    if (status != ERRCODE_BT_SUCCESS) {
        /* A failed bond is removed so the next connection can negotiate fresh keys. / 删除失败绑定，便于下次重新协商密钥。 */
        osal_printk("%s remove stale pair, ret=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, gap_ble_remove_pair(addr));
    }
}

static void ble_uart_bridge_enable_cb(uint8_t status)
{
    g_ble_enable_status = status;
    if (g_ble_enable_sem_ready) {
        osal_sem_up(&g_ble_enable_sem);
    }
}

/**
 * @if Eng
 * @brief Configures security, the local address, and the GATT service after BLE is enabled.
 * @else
 * @brief BLE 使能后配置安全参数、本地地址与 GATT 服务。
 * @endif
 */
static errcode_t ble_uart_bridge_configure_and_start(void)
{
    gap_ble_sec_params_t security = {0};
    errcode_t ret;
    /* Encode the retained cache state before advertising begins. / 开始广播前编码保留缓存状态。 */
    ble_uart_bridge_server_set_adv_default_state(g_property_value_len == sizeof(DEFAULT_VALUE) - 1 &&
                                                 memcmp(g_property_value, DEFAULT_VALUE, sizeof(DEFAULT_VALUE) - 1) ==
                                                     0);
    /* Use Just Works pairing because the board exposes no input or display. / 单板无输入和显示能力，使用 Just Works 配对。 */
    security.bondable = 1;
    security.io_capability = GAP_BLE_IO_CAPABILITY_NOINPUTNOOUTPUT;
    security.sc_enable = 0;
    security.sc_mode = GAP_BLE_GAP_SECURITY_MODE1_LEVEL2;
    ret = gap_ble_set_sec_param(&security);
    if (ret != ERRCODE_BT_SUCCESS) {
        osal_printk("%s security config failed: 0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, ret);
        return ret;
    }
    /* A fixed sample address makes reconnect behavior deterministic during development. / 固定案例地址便于调试重连行为。 */
    ret = gap_ble_set_local_addr(&g_ble_uart_bridge_addr);
    if (ret != ERRCODE_BT_SUCCESS) {
        osal_printk("%s local address config failed: 0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, ret);
        return ret;
    }
    ret = ble_uart_bridge_add_gatt_service();
    osal_printk("%s init %s, ret=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, ret == ERRCODE_BT_SUCCESS ? "ok" : "failed",
                ret);
    return ret;
}

/**
 * @if Eng
 * @brief Registers GAP and GATT server callbacks used by this sample.
 * @else
 * @brief 注册本案例使用的 GAP 和 GATT 服务端回调。
 * @endif
 */
static errcode_t ble_uart_bridge_register_callbacks(void)
{
    gap_ble_callbacks_t gap_callbacks = {0};
    gatts_callbacks_t gatt_callbacks = {0};
    errcode_t ret;

    /* GAP callbacks own stack lifecycle, connection state, and pairing. / GAP 回调管理协议栈、连接和配对。 */
    gap_callbacks.conn_state_change_cb = ble_uart_bridge_conn_state_cb;
    gap_callbacks.pair_result_cb = ble_uart_bridge_pair_result_cb;
    ret = gap_ble_register_callbacks(&gap_callbacks);
    if (ret != ERRCODE_BT_SUCCESS) {
        return ret;
    }

    /* GATT callbacks serve attributes and close the indication flow-control loop. / GATT 回调处理属性并闭合指示流控。 */
    gatt_callbacks.start_service_cb = ble_uart_bridge_service_start_cb;
    gatt_callbacks.read_request_cb = ble_uart_bridge_read_request_cb;
    gatt_callbacks.write_request_cb = ble_uart_bridge_write_request_cb;
    gatt_callbacks.mtu_changed_cb = ble_uart_bridge_mtu_changed_cb;
    gatt_callbacks.indicate_confirm_cb = ble_uart_bridge_indication_confirm_cb;
    return gatts_register_callbacks(&gatt_callbacks);
}

/**
 * @if Eng
 * @brief Sends an indication using the specified characteristic handle.
 * @else
 * @brief 使用指定特征句柄发送指示。
 * @endif
 */
static errcode_t ble_uart_bridge_send_value_notification(uint16_t handle,
                                                         const uint8_t *data,
                                                         uint16_t len,
                                                         const char *name)
{
    gatts_ntf_ind_t notification = {0};
    errcode_t ret;
    /* Reject data until the link and configured payload bounds are valid. / 连接或载荷边界无效时拒绝发送。 */
    if (!g_connected || data == NULL || len == 0 || len > BLE_UART_BRIDGE_BLE_PAYLOAD_MAX_LEN) {
        return ERRCODE_BT_FAIL;
    }
    notification.attr_handle = handle;
    notification.value = (uint8_t *)data;
    notification.value_len = len;
    /* The characteristic property selects indication semantics for this API call. / 该接口依据特征属性执行指示发送。 */
    ret = gatts_notify_indicate(g_server_id, g_conn_id, &notification);
    if (ret != ERRCODE_BT_SUCCESS) {
        osal_printk("%s %s failed: 0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, name, ret);
    }
    return ret;
}

/**
 * @if Eng
 * @brief Sends one UART data fragment to the connected data receiving role.
 * @else
 * @brief 向已连接的数据接收端发送一段 UART 数据。
 * @endif
 */
errcode_t ble_uart_bridge_server_send_notification(const uint8_t *data, uint16_t len)
{
    /* Do not enqueue an ATT indication until the peer has enabled its CCCD. / 对端未使能 CCCD 时不发送 ATT 指示。 */
    if (!g_hello_notify_enabled) {
        return ERRCODE_BT_FAIL;
    }
    return ble_uart_bridge_send_value_notification(g_notify_handle, data, len, "notification");
}

bool ble_uart_bridge_server_can_send(void)
{
    return g_connected && g_hello_notify_enabled && !g_handshake_indication_pending;
}

uint16_t ble_uart_bridge_server_get_payload_max(void)
{
    uint16_t mtu = g_att_mtu;
    uint16_t payload_max;

    if (mtu <= BLE_ATT_PROTOCOL_OVERHEAD) {
        return 0;
    }
    payload_max = (uint16_t)(mtu - BLE_ATT_PROTOCOL_OVERHEAD);
    return payload_max > BLE_UART_BRIDGE_BLE_PAYLOAD_MAX_LEN ?
        BLE_UART_BRIDGE_BLE_PAYLOAD_MAX_LEN : payload_max;
}

/**
 * @if Eng
 * @brief Initializes GATT server callbacks and enables the BLE stack.
 * @else
 * @brief 初始化 GATT 服务端回调并使能 BLE 协议栈。
 * @endif
 */
errcode_t ble_uart_bridge_server_init(void)
{
    bts_dev_manager_callbacks_t manager_callbacks = {0};
    errcode_t ret;

    (void)osal_msleep(BLE_UART_BRIDGE_SERVER_STARTUP_DELAY_MS);
    if (osal_sem_init(&g_ble_enable_sem, 0) != OSAL_SUCCESS) {
        return ERRCODE_BT_FAIL;
    }
    g_ble_enable_status = BT_ENABLE_DISABLE_FAIL;
    g_ble_enable_sem_ready = true;
    manager_callbacks.ble_enable_cb = ble_uart_bridge_enable_cb;
    ret = bts_dev_manager_register_callbacks(&manager_callbacks);
    if (ret != ERRCODE_BT_SUCCESS) {
        g_ble_enable_sem_ready = false;
        osal_sem_destroy(&g_ble_enable_sem);
        return ret;
    }

    ret = enable_ble();
    osal_printk("%s enable request ret=0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, ret);
    if (ret == ERRCODE_BT_SUCCESS &&
        osal_sem_down_timeout(&g_ble_enable_sem, BLE_UART_BRIDGE_ENABLE_TIMEOUT_MS) != OSAL_SUCCESS) {
        ret = ERRCODE_BT_FAIL;
    }
    g_ble_enable_sem_ready = false;
    osal_sem_destroy(&g_ble_enable_sem);
    if (ret != ERRCODE_BT_SUCCESS || g_ble_enable_status != BT_ENABLE_DISABLE_SUCCESS) {
        osal_printk("%s BLE enable failed: request=0x%x, status=%u\r\n", BLE_UART_BRIDGE_SERVER_LOG,
                    ret, g_ble_enable_status);
        return ret != ERRCODE_BT_SUCCESS ? ret : ERRCODE_BT_FAIL;
    }

    ret = ble_uart_bridge_register_callbacks();
    if (ret != ERRCODE_BT_SUCCESS) {
        osal_printk("%s callback registration failed: 0x%x\r\n", BLE_UART_BRIDGE_SERVER_LOG, ret);
        (void)disable_ble();
        return ret;
    }
    ret = ble_uart_bridge_configure_and_start();
    if (ret != ERRCODE_BT_SUCCESS) {
        (void)disable_ble();
    }
    return ret;
}
