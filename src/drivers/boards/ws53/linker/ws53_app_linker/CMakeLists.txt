#===============================================================================
# @brief    cmake file
# Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2022-2022. All rights reserved.
#===============================================================================
set(COMPONENT_NAME "ws53_app_lds")

if(NOT ${COMPONENT_NAME} IN_LIST TARGET_COMPONENT)
    return()
endif()

set(LDS_HEADER
    ${ROOT_DIR}/drivers/boards/${CHIP}/board_config
    ${ROOT_DIR}/drivers/boards/${CHIP}/memory_config/include
    ${ROOT_DIR}/drivers/boards/${CHIP}/memory_config/include/product
    ${ROOT_DIR}/drivers/chips/${CHIP}/include
    ${ROOT_DIR}/drivers/chips/${CHIP}/include/${CORE}
    ${ROOT_DIR}/middleware/utils/common_headers
    ${OUTPUT_ROOT}/${CHIP}/${CORE}/${BUILD_TARGET_NAME}
    CACHE INTERNAL "" FORCE
)

set(PUBLIC_HEADER ${CMAKE_CURRENT_SOURCE_DIR})
set(LINK_SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/linker.prelds" CACHE INTERNAL "" FORCE)
build_component()
