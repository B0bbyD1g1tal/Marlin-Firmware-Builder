#!/bin/bash

FIRMWARE_BIN="${WORK_DIR}/Marlin/.pio/build/${PIO_BOARD_ENV}/firmware-*bin"

cd "${WORK_DIR}"/Marlin/ || exit &&
  pio run -e "${PIO_BOARD_ENV}" &&
  cp "${FIRMWARE_BIN}" "${FIRMWARE_BIN_DIR}"
