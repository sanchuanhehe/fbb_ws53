#===============================================================================
# @brief    CMake file for the BLE MQTT gateway sample.
# Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2023-2026.
#===============================================================================
if(CONFIG_SAMPLE_SUPPORT_BLE_GATEWAY_SERVER_SAMPLE)
    set(SOURCES ${SOURCES} ${CMAKE_CURRENT_SOURCE_DIR}/ble_gateway.c)
    add_subdirectory_if_exist(ble_gateway_server)
endif()

set(SOURCES "${SOURCES}" PARENT_SCOPE)
set(PUBLIC_HEADER "${PUBLIC_HEADER}" "${CMAKE_CURRENT_SOURCE_DIR}/inc" PARENT_SCOPE)
