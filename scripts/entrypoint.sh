#!/bin/bash

cd "${WORK_DIR}"/Marlin/ || exit &&
  pio run -e "${PIO_BOARD}" &&
  cp "${WORK_DIR}"/Marlin/.pio/build/"${PIO_BOARD}"/firmware-*bin \
    "${FIRMWARE_BIN_DIR}"
