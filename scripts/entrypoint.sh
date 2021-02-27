#!/bin/bash
###############################################################################
set -e
set -x
###############################################################################
# Build and copy firmware-*.bin
###############################################################################
BINARY_FILE_NAME=\
$(echo "$MODEL" | tr -d " ")-"${BOARD}"-"${GIT_BRANCH}"-$(date +"%d-%b-%y").bin

cd "${WORK_DIR}"/Marlin/ || exit &&
  pio run -e "${PIO_BOARD}" &&
  cp "${WORK_DIR}"/Marlin/.pio/build/"${PIO_BOARD}"/firmware-*bin \
    "${FIRMWARE_BIN_DIR}"/"${BINARY_FILE_NAME}"
###############################################################################
# TODO Branch &| PIO Board &| Printer selection to be done here

# TODO -check-branches-and- just checkout the selected

# TODO move to entrypoint
# Copy selected printer configs to PIO project
#copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
#         dirs_exist_ok=True)

# TODO move to entrypoint
# Set Default ENV in platformio.ini
#DEFAULT_PIO_ENV = 'default_envs = '
#run(['sed', '-i', '-e',
#     f's^{DEFAULT_PIO_ENV}.*^{DEFAULT_PIO_ENV}{environ["PIO_BOARD"]}^',
#     f'{PIO_PROJECT}/platformio.ini'],
#    check=True)
# TODO move to entrypoint