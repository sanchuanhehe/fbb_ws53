#===============================================================================
# @brief    CMake file for the BLE Hello sample.
# Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2023-2026.
#===============================================================================
if(DEFINED CONFIG_SAMPLE_SUPPORT_BLE_UART_BRIDGE_SERVER_SAMPLE)
    set(SOURCES ${SOURCES} ${CMAKE_CURRENT_SOURCE_DIR}/ble_uart_bridge.c)
    add_subdirectory_if_exist(ble_uart_bridge_server)
endif()

set(SOURCES "${SOURCES}" PARENT_SCOPE)
set(PUBLIC_HEADER "${PUBLIC_HEADER}" "${CMAKE_CURRENT_SOURCE_DIR}" PARENT_SCOPE)
