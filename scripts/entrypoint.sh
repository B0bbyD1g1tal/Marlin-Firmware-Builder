#!/bin/bash

FIRMWARE_BIN="${PIO_PROJECT_DIR}.pio/build/${PIO_BOARD_ENV}/firmware-*bin"

pio run -e "${PIO_BOARD_ENV}"

cp "${FIRMWARE_BIN}" "${FIRMWARE_BIN_DIR}"
