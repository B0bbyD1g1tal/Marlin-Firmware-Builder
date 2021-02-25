#!/usr/bin/env bash

cd "${PIO_DIR}Marlin/" && \
rm -rf ./.pio/build/ && \
pio run -e "${PIO_BOARD_ENV}" && \
cp ./.pio/build/"${PIO_BOARD_ENV}"/firmware-*.bin "${FIRMWARE_BIN_DIR}"
