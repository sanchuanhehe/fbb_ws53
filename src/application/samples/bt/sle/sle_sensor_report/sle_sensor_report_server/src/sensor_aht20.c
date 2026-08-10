/**
 * Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2026. All rights reserved.
 *
 * Description: AHT20 sensor adapter used by the SLE sensor report sample. \n
 */

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include "i2c.h"
#include "pinctrl.h"
#include "soc_osal.h"
#include "sensor_aht20.h"

#define SENSOR_HW_LOG                         "[sensor hw]"

#define SENSOR_I2C_BUS                        I2C_BUS_0
#define SENSOR_I2C_BAUDRATE                   100000U
#define SENSOR_I2C_HSCODE                     0U
#define SENSOR_I2C_SCL_PIN                    S_MGPIO21
#define SENSOR_I2C_SDA_PIN                    S_MGPIO22
#define SENSOR_I2C_PIN_MODE                   PIN_MODE_3

#define AHT20_I2C_ADDRESS                     0x38U
#define AHT20_STATUS_COMMAND                  0x71U
#define AHT20_INITIALIZE_COMMAND              0xBEU
#define AHT20_INITIALIZE_ARG0                 0x08U
#define AHT20_INITIALIZE_ARG1                 0x00U
#define AHT20_TRIGGER_COMMAND                 0xACU
#define AHT20_TRIGGER_ARG0                    0x33U
#define AHT20_TRIGGER_ARG1                    0x00U
#define AHT20_STATUS_BUSY_MASK                0x80U
#define AHT20_STATUS_CALIBRATED_MASK          0x08U
#define AHT20_RESPONSE_LENGTH                 7U
#define AHT20_CRC_INDEX                       6U
#define AHT20_CRC_POLYNOMIAL                  0x31U
#define AHT20_CRC_INITIAL                     0xFFU
#define AHT20_RAW_DENOMINATOR                 1048576ULL
#define AHT20_POWER_ON_DELAY_MS               100U
#define AHT20_STATUS_DELAY_MS                 5U
#define AHT20_CALIBRATION_DELAY_MS            20U
#define AHT20_MEASUREMENT_DELAY_MS            80U
#define AHT20_BUSY_RETRY_DELAY_MS             10U
#define AHT20_BUSY_RETRY_COUNT                3U
#define AHT20_TEMPERATURE_MIN_X100            (-4000)
#define AHT20_TEMPERATURE_MAX_X100            8500

#define BMP280_ADDRESS_LOW                    0x76U
#define BMP280_ADDRESS_HIGH                   0x77U
#define BMP280_CHIP_ID_REGISTER               0xD0U
#define BMP280_CHIP_ID                        0x58U
#define BMP280_PROBE_DELAY_MS                 500U

#define SENSOR_FAILURE_LOG_PERIOD             10U

static bool g_i2c_ready = false;
static bool g_sensor_ready = false;
static bool g_sensor_was_ready = false;
static bool g_failure_pending = false;
static bool g_bmp280_probe_done = false;
static uint32_t g_consecutive_failures = 0;

static errcode_t sensor_i2c_write(uint16_t address, uint8_t *buffer, uint32_t length)
{
    i2c_data_t data = {0};
    data.send_buf = buffer;
    data.send_len = length;
    return uapi_i2c_master_write(SENSOR_I2C_BUS, address, &data);
}

static errcode_t sensor_i2c_read(uint16_t address, uint8_t *buffer, uint32_t length)
{
    i2c_data_t data = {0};
    data.receive_buf = buffer;
    data.receive_len = length;
    return uapi_i2c_master_read(SENSOR_I2C_BUS, address, &data);
}

static errcode_t sensor_i2c_read_register(uint16_t address, uint8_t reg, uint8_t *value)
{
    i2c_data_t data = {0};
    data.send_buf = &reg;
    data.send_len = sizeof(reg);
    data.receive_buf = value;
    data.receive_len = sizeof(*value);
    return uapi_i2c_master_writeread(SENSOR_I2C_BUS, address, &data);
}

static errcode_t sensor_record_failure(const char *stage, errcode_t ret)
{
    g_sensor_ready = false;
    g_failure_pending = true;
    g_consecutive_failures++;
    if ((g_consecutive_failures == 1U) ||
        ((g_consecutive_failures % SENSOR_FAILURE_LOG_PERIOD) == 0U)) {
        osal_printk("%s read failed: stage=%s, err=0x%x, consecutive=%u\r\n", SENSOR_HW_LOG, stage,
                    (unsigned int)ret, (unsigned int)g_consecutive_failures);
    }
    return ret;
}

static errcode_t sensor_i2c_init(void)
{
    errcode_t ret;

#if defined(CONFIG_PINCTRL_SUPPORT_IE)
    ret = uapi_pin_set_ie(SENSOR_I2C_SCL_PIN, PIN_IE_1);
    if (ret != ERRCODE_SUCC) {
        return ret;
    }
    ret = uapi_pin_set_ie(SENSOR_I2C_SDA_PIN, PIN_IE_1);
    if (ret != ERRCODE_SUCC) {
        return ret;
    }
#endif

    ret = uapi_pin_set_mode(SENSOR_I2C_SCL_PIN, SENSOR_I2C_PIN_MODE);
    if (ret != ERRCODE_SUCC) {
        return ret;
    }
    ret = uapi_pin_set_mode(SENSOR_I2C_SDA_PIN, SENSOR_I2C_PIN_MODE);
    if (ret != ERRCODE_SUCC) {
        return ret;
    }

    ret = uapi_i2c_master_init(SENSOR_I2C_BUS, SENSOR_I2C_BAUDRATE, SENSOR_I2C_HSCODE);
    if ((ret != ERRCODE_SUCC) && (ret != ERRCODE_I2C_ALREADY_INIT)) {
        return ret;
    }

    g_i2c_ready = true;
    (void)osal_msleep(AHT20_POWER_ON_DELAY_MS);
    osal_printk("%s i2c ready: bus=0, scl=GPIO21, sda=GPIO22, rate=%u\r\n", SENSOR_HW_LOG,
                SENSOR_I2C_BAUDRATE);
    return ERRCODE_SUCC;
}

static void sensor_probe_bmp280(void)
{
    static const uint8_t addresses[] = {BMP280_ADDRESS_LOW, BMP280_ADDRESS_HIGH};
    bool detected = false;

    for (uint32_t i = 0; i < (sizeof(addresses) / sizeof(addresses[0])); i++) {
        uint8_t chip_id = 0;
        errcode_t ret = sensor_i2c_read_register(addresses[i], BMP280_CHIP_ID_REGISTER, &chip_id);
        if ((ret == ERRCODE_SUCC) && (chip_id == BMP280_CHIP_ID)) {
            osal_printk("%s bmp280 detected: addr=0x%02x, id=0x%02x (pressure disabled)\r\n", SENSOR_HW_LOG,
                        addresses[i], chip_id);
            detected = true;
        } else if (ret == ERRCODE_SUCC) {
            osal_printk("%s device at addr=0x%02x has id=0x%02x, not BMP280\r\n", SENSOR_HW_LOG,
                        addresses[i], chip_id);
        } else {
            osal_printk("%s bmp280 probe failed: addr=0x%02x, err=0x%x\r\n", SENSOR_HW_LOG,
                        addresses[i], (unsigned int)ret);
        }
    }
    if (!detected) {
        osal_printk("%s bmp280 not detected at 0x76/0x77 (pressure disabled)\r\n", SENSOR_HW_LOG);
    }
    g_bmp280_probe_done = true;
}

static errcode_t aht20_read_status(uint8_t *status, const char **failure_stage)
{
    uint8_t command = AHT20_STATUS_COMMAND;
    *failure_stage = "status-command";
    errcode_t ret = sensor_i2c_write(AHT20_I2C_ADDRESS, &command, sizeof(command));
    if (ret != ERRCODE_SUCC) {
        return ret;
    }
    (void)osal_msleep(AHT20_STATUS_DELAY_MS);
    *failure_stage = "status-read";
    return sensor_i2c_read(AHT20_I2C_ADDRESS, status, sizeof(*status));
}

static errcode_t aht20_wait_idle(uint8_t *status, const char **failure_stage)
{
    errcode_t ret;
    for (uint32_t i = 0; i < AHT20_BUSY_RETRY_COUNT; i++) {
        ret = aht20_read_status(status, failure_stage);
        if (ret != ERRCODE_SUCC) {
            return ret;
        }
        if ((*status & AHT20_STATUS_BUSY_MASK) == 0U) {
            return ERRCODE_SUCC;
        }
        (void)osal_msleep(AHT20_BUSY_RETRY_DELAY_MS);
    }
    *failure_stage = "status-busy";
    return ERRCODE_I2C_TIMEOUT;
}

static errcode_t aht20_calibrate(void)
{
    uint8_t status = 0;
    const char *failure_stage = "status-command";
    errcode_t ret = aht20_wait_idle(&status, &failure_stage);
    if (ret != ERRCODE_SUCC) {
        return sensor_record_failure(failure_stage, ret);
    }
    if ((status & AHT20_STATUS_CALIBRATED_MASK) != 0U) {
        return ERRCODE_SUCC;
    }

    uint8_t command[] = {AHT20_INITIALIZE_COMMAND, AHT20_INITIALIZE_ARG0, AHT20_INITIALIZE_ARG1};
    ret = sensor_i2c_write(AHT20_I2C_ADDRESS, command, sizeof(command));
    if (ret != ERRCODE_SUCC) {
        return sensor_record_failure("calibration-command", ret);
    }
    (void)osal_msleep(AHT20_CALIBRATION_DELAY_MS);

    ret = aht20_wait_idle(&status, &failure_stage);
    if (ret != ERRCODE_SUCC) {
        return sensor_record_failure(failure_stage, ret);
    }
    if ((status & AHT20_STATUS_CALIBRATED_MASK) == 0U) {
        return sensor_record_failure("not-calibrated", ERRCODE_FAIL);
    }
    return ERRCODE_SUCC;
}

static uint8_t aht20_crc8(const uint8_t *data, uint32_t length)
{
    uint8_t crc = AHT20_CRC_INITIAL;
    for (uint32_t i = 0; i < length; i++) {
        crc ^= data[i];
        for (uint32_t bit = 0; bit < 8U; bit++) {
            if ((crc & 0x80U) != 0U) {
                crc = (uint8_t)((crc << 1U) ^ AHT20_CRC_POLYNOMIAL);
            } else {
                crc <<= 1U;
            }
        }
    }
    return crc;
}

static errcode_t aht20_read_response(uint8_t response[AHT20_RESPONSE_LENGTH])
{
    errcode_t ret;
    for (uint32_t i = 0; i < AHT20_BUSY_RETRY_COUNT; i++) {
        ret = sensor_i2c_read(AHT20_I2C_ADDRESS, response, AHT20_RESPONSE_LENGTH);
        if (ret != ERRCODE_SUCC) {
            return ret;
        }
        if ((response[0] & AHT20_STATUS_BUSY_MASK) == 0U) {
            return ERRCODE_SUCC;
        }
        (void)osal_msleep(AHT20_BUSY_RETRY_DELAY_MS);
    }
    return ERRCODE_I2C_TIMEOUT;
}

errcode_t sensor_aht20_init(void)
{
    if (g_sensor_ready) {
        return ERRCODE_SUCC;
    }

    if (!g_i2c_ready) {
        errcode_t ret = sensor_i2c_init();
        if (ret != ERRCODE_SUCC) {
            return sensor_record_failure("i2c-init", ret);
        }
    }
    if (!g_bmp280_probe_done) {
        /* Keep the one-shot probe log clear of concurrent RF calibration output. */
        (void)osal_msleep(BMP280_PROBE_DELAY_MS);
        sensor_probe_bmp280();
    }

    errcode_t ret = aht20_calibrate();
    if (ret != ERRCODE_SUCC) {
        return ret;
    }

    g_sensor_ready = true;
    return ERRCODE_SUCC;
}

errcode_t sensor_aht20_read(int16_t *temperature_x100, uint8_t *humidity_percent)
{
    if ((temperature_x100 == NULL) || (humidity_percent == NULL)) {
        return ERRCODE_INVALID_PARAM;
    }

    errcode_t ret = sensor_aht20_init();
    if (ret != ERRCODE_SUCC) {
        return ret;
    }

    uint8_t command[] = {AHT20_TRIGGER_COMMAND, AHT20_TRIGGER_ARG0, AHT20_TRIGGER_ARG1};
    ret = sensor_i2c_write(AHT20_I2C_ADDRESS, command, sizeof(command));
    if (ret != ERRCODE_SUCC) {
        return sensor_record_failure("trigger", ret);
    }
    (void)osal_msleep(AHT20_MEASUREMENT_DELAY_MS);

    uint8_t response[AHT20_RESPONSE_LENGTH] = {0};
    ret = aht20_read_response(response);
    if (ret != ERRCODE_SUCC) {
        return sensor_record_failure("measurement-read", ret);
    }
    if ((response[0] & AHT20_STATUS_CALIBRATED_MASK) == 0U) {
        return sensor_record_failure("calibration-lost", ERRCODE_FAIL);
    }
    if (aht20_crc8(response, AHT20_CRC_INDEX) != response[AHT20_CRC_INDEX]) {
        return sensor_record_failure("crc", ERRCODE_FAIL);
    }

    uint32_t humidity_raw = ((uint32_t)response[1] << 12U) |
                            ((uint32_t)response[2] << 4U) |
                            ((uint32_t)response[3] >> 4U);
    uint32_t temperature_raw = (((uint32_t)response[3] & 0x0FU) << 16U) |
                               ((uint32_t)response[4] << 8U) |
                               (uint32_t)response[5];

    uint64_t humidity_scaled = ((uint64_t)humidity_raw * 100ULL + (AHT20_RAW_DENOMINATOR / 2ULL)) /
                               AHT20_RAW_DENOMINATOR;
    if (humidity_scaled > 100ULL) {
        humidity_scaled = 100ULL;
    }
    int32_t temperature_scaled = (int32_t)(((uint64_t)temperature_raw * 20000ULL +
                                            (AHT20_RAW_DENOMINATOR / 2ULL)) /
                                           AHT20_RAW_DENOMINATOR) - 5000;
    if ((temperature_scaled < AHT20_TEMPERATURE_MIN_X100) ||
        (temperature_scaled > AHT20_TEMPERATURE_MAX_X100)) {
        return sensor_record_failure("range", ERRCODE_FAIL);
    }

    *temperature_x100 = (int16_t)temperature_scaled;
    *humidity_percent = (uint8_t)humidity_scaled;

    if (!g_sensor_was_ready) {
        osal_printk("%s aht20 compatible device ready\r\n", SENSOR_HW_LOG);
        g_sensor_was_ready = true;
    }
    if (g_failure_pending) {
        osal_printk("%s sensor recovered\r\n", SENSOR_HW_LOG);
        g_failure_pending = false;
    }
    g_consecutive_failures = 0;
    return ERRCODE_SUCC;
}
