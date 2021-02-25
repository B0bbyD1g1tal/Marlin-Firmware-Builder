#!/usr/bin/env bash

platformio run -e "${PIO_BOARD_ENV}" &&
  cp "${PIO_DIR}/Marlin/.pio/build/${PIO_BOARD_ENV}/firmware-*.bin" "${FIRMWARE_BIN_DIR}"
