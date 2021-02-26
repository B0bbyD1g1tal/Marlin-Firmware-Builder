#!/bin/bash

cd "${WORK_DIR}"/Marlin/ || exit &&
  pio run -e "${PIO_BOARD_ENV}" &&
  cp "${WORK_DIR}"/Marlin/.pio/build/"${PIO_BOARD_ENV}"/firmware-*bin \
    "${FIRMWARE_BIN_DIR}"
