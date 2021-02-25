#!/usr/bin/env bash

# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO="Marlin"

cd "${PIO_DIR}${MARLIN_FIRMWARE_REPO}/" &&
  rm -rf ./.pio/build/ &&
  pio run -e "${PIO_BOARD_ENV}" &&
  cp ./.pio/build/"${PIO_BOARD_ENV}"/firmware-*.bin "${FIRMWARE_BIN_DIR}"
