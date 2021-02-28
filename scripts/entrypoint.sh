#!/bin/bash
###############################################################################
set -e
set -x
###############################################################################
BINARY_FILE_NAME=$(echo "${MODEL}" | tr -d " ")-"${BOARD}"-"${MARLIN_GIT_BRANCH}"-$(date +"%d-%b-%y").bin
###############################################################################
# Marlin git-branch
###############################################################################
current-branch="$(git rev-parse --abbrev-ref HEAD)"

cd "${WORK_DIR}"/Configurations/ || exit &&
  git checkout "${MARLIN_GIT_BRANCH}" &&
  cd "${WORK_DIR}"/Marlin/ || exit &&
  git checkout "${MARLIN_GIT_BRANCH}"

current-branch="$(git rev-parse --abbrev-ref HEAD)"
###############################################################################
# Manufacturer & Printer & Board selection
###############################################################################
cp \
  "${WORK_DIR}"/Configurations/config/examples/"${MANUFACTURER}"/"${MODEL}"/"${BOARD}"/*.h \
  "${WORK_DIR}"/Marlin/Marlin/
###############################################################################
# config-calibrator.sh
###############################################################################
bash config-calibrator.sh
###############################################################################
# Build firmware-*.bin
###############################################################################
pio run -e "${PIO_BOARD}"
###############################################################################
# Copy firmware-*.bin to delivery folder
###############################################################################
cp "${WORK_DIR}"/Marlin/.pio/build/"${PIO_BOARD}"/firmware-*bin \
  "${FIRMWARE_BIN_DIR}"/"${BINARY_FILE_NAME}"
###############################################################################
