#!/usr/bin/env bash

###############################################################################
#==============================================================================
# Set script variables
#==============================================================================
###############################################################################
AUTHOR="B0bby D1g1tal"
# sed separator set to ^
SED="^"

set -e
set -x

###############################################################################
# Marlin Github repositories and branch
###############################################################################
MARLIN_GITHUB_URL="https://github.com/MarlinFirmware/"
MARLIN_FW_REPO="Marlin"
MARLIN_CONFIG_REPO="Configurations"

###############################################################################
# Manufacturer, Printer, Board
###############################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Names should be the same as in the Configurations repository path:
# https://github.com/MarlinFirmware/Configurations/tree/$GIT_BRANCH/config/examples/$MANUFACTURER/$MODEL/$BOARD/*.h
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MANUFACTURER="Creality"
MODEL="Ender-3\ Pro"
BOARD="CrealityV427"

###############################################################################
# Marlin Firmware and Configurations local paths
###############################################################################
CONFIGS_PATH="${PIO_DIR}${MARLIN_CONFIG_REPO}/config/examples/${MANUFACTURER}/${MODEL}/${BOARD}/"
MARLIN_PIO_PATH="${PIO_DIR}${MARLIN_FW_REPO}/Marlin/"

###############################################################################
#==============================================================================
# Clone Marlin Firmware and Configurations repositories
# and copy Printer's configurations
#==============================================================================
###############################################################################
git clone -b "${GIT_BRANCH}" "${MARLIN_GITHUB_URL}${MARLIN_FW_REPO}.git" && \
git clone -b "${GIT_BRANCH}" "${MARLIN_GITHUB_URL}${MARLIN_CONFIG_REPO}.git" &&\
cp "${CONFIGS_PATH}*" "${MARLIN_PIO_PATH}"

###############################################################################
#==============================================================================
# Editing Printer's configuration files
#==============================================================================
###############################################################################

###############################################################################
# platformio.ini
###############################################################################
DEFAULT_ENVS="default_envs = "
sed -i -e "s${SED}${DEFAULT_ENVS}.*${SED}${DEFAULT_ENVS}${PIO_BOARD_ENV}${SED}" "${PIO_DIR}${MARLIN_FW_REPO}/platformio.ini"

###############################################################################
# Configuration.h
###############################################################################
STRING_CONFIG_H_AUTHOR="#define STRING_CONFIG_H_AUTHOR"
sed -i -e "s${SED}${STRING_CONFIG_H_AUTHOR} \"(.*,${SED}${STRING_CONFIG_H_AUTHOR} \"(${AUTHOR},${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

SERIAL_PORT_2="#define SERIAL_PORT_2"
sed -i -e "s//${SED}${SERIAL_PORT_2}.*${SED}${SERIAL_PORT_2} 3${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

BLTOUCH="#define BLTOUCH"
sed -i -e "s${SED}//${BLTOUCH}${SED}${BLTOUCH}${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

AUTO_BED_LEVELING_BILINEAR="#define AUTO_BED_LEVELING_BILINEAR"
sed -i -e "s${SED}//${AUTO_BED_LEVELING_BILINEAR}${SED}${AUTO_BED_LEVELING_BILINEAR}${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

Z_SAFE_HOMING="#define Z_SAFE_HOMING"
sed -i -e "s${SED}//${Z_SAFE_HOMING}${SED}${Z_SAFE_HOMING}${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

NOZZLE_TO_PROBE_OFFSET="#define NOZZLE_TO_PROBE_OFFSET"
sed -i -e "s${SED}${NOZZLE_TO_PROBE_OFFSET} { 10, 10, 0 }${SED}${NOZZLE_TO_PROBE_OFFSET} { -42, -10, 0 }${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

GRID_MAX_POINTS_X="#define GRID_MAX_POINTS_X"
sed -i -e "s${SED}${GRID_MAX_POINTS_X} .${SED}${GRID_MAX_POINTS_X} 5${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

XY_PROBE_SPEED="#define XY_PROBE_SPEED"
sed -i -e "s${SED}${XY_PROBE_SPEED} .*${SED}${XY_PROBE_SPEED} (150*60)${SED}" "${MARLIN_PIO_PATH}/Configuration.h"

###############################################################################
# Configuration_adv.h
###############################################################################
PROBE_OFFSET_WIZARD="#define PROBE_OFFSET_WIZARD"
sed -i -e "s${SED}//${PROBE_OFFSET_WIZARD}${SED}${PROBE_OFFSET_WIZARD}${SED}" "${MARLIN_PIO_PATH}/Configuration_adv.h"

PROBE_OFFSET_WIZARD_START_Z="#define PROBE_OFFSET_WIZARD_START_Z"
sed -i -e "s${SED}//${PROBE_OFFSET_WIZARD_START_Z}${SED}${PROBE_OFFSET_WIZARD_START_Z}${SED}" "${MARLIN_PIO_PATH}/Configuration_adv.h"

BABYSTEP_ZPROBE_OFFSET="#define BABYSTEP_ZPROBE_OFFSET"
sed -i -e "s${SED}//${BABYSTEP_ZPROBE_OFFSET}${SED}${BABYSTEP_ZPROBE_OFFSET}${SED}" "${MARLIN_PIO_PATH}/Configuration_adv.h"

###############################################################################
#-----------------------------------------------------------------------------#
###############################################################################
