/**
 * Copyright (c) HiSilicon (Shanghai) Technologies Co., Ltd. 2026. All rights reserved.
 *
 * Description: AHT20 sensor adapter used by the SLE sensor report sample. \n
 */

#ifndef SENSOR_AHT20_H
#define SENSOR_AHT20_H

#include <stdint.h>
#include "errcode.h"

/**
 * @brief Initializes I2C0 and verifies that an AHT20-compatible sensor is ready.
 */
errcode_t sensor_aht20_init(void);

/**
 * @brief Reads one checked AHT20 sample.
 * @param temperature_x100 Temperature in degrees Celsius multiplied by 100.
 * @param humidity_percent Relative humidity rounded to an integer percentage.
 */
errcode_t sensor_aht20_read(int16_t *temperature_x100, uint8_t *humidity_percent);

#endif /* SENSOR_AHT20_H */
