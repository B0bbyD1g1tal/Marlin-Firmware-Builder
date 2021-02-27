#!/bin/bash
###############################################################################
set -e
set -x
###############################################################################
cd "${WORK_DIR}"/Marlin/ || exit &&
  pio run -e "${PIO_BOARD}" &&
  cp "${WORK_DIR}"/Marlin/.pio/build/"${PIO_BOARD}"/firmware-*bin \
    "${FIRMWARE_BIN_DIR}"
###############################################################################
# TODO Branch &| PIO Board &| Printer selection to be done here
