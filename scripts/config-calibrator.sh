#!/bin/bash
###############################################################################
set -e
set -x
###############################################################################
PIO_CONFIGS_DIR="${WORK_DIR}/Marlin/Marlin/"
###############################################################################
STRING_CONFIG_H_AUTHOR="#define STRING_CONFIG_H_AUTHOR"
sed -i -e \
  "s^${STRING_CONFIG_H_AUTHOR} \"(.*,^${STRING_CONFIG_H_AUTHOR} \"(${AUTHOR},^" \
  "${PIO_CONFIGS_DIR}"Configuration.h
###############################################################################
# Custom config settings
###############################################################################
# The following are for Creality Ender3 Pro v4.2.7 and enabling BLTouch
###############################################################################
if [[ "${CUSTOM_CONFIG}" == 'yes' ]]; then
  # Configuration.h
  #############################################################################
  SERIAL_PORT_2="#define SERIAL_PORT_2"
  SERIAL_PORT_2_VALUE="3"
  sed -i -e \
    "s^//${SERIAL_PORT_2} .*^${SERIAL_PORT_2} ${SERIAL_PORT_2_VALUE}^" \
    "${PIO_CONFIGS_DIR}"Configuration.h
  #############################################################################
  BLTOUCH="#define BLTOUCH"
  sed -i -e \
    "s^//${BLTOUCH}^${BLTOUCH}^" \
    "${PIO_CONFIGS_DIR}"Configuration.h
  #############################################################################
  AUTO_BED_LEVELING_BILINEAR="#define AUTO_BED_LEVELING_BILINEAR"
  sed -i -e \
    "s^//${AUTO_BED_LEVELING_BILINEAR}^${AUTO_BED_LEVELING_BILINEAR}^" \
    "${PIO_CONFIGS_DIR}"/Configuration.h
  #############################################################################
  Z_SAFE_HOMING="#define Z_SAFE_HOMING"
  sed -i -e \
    "s^//${Z_SAFE_HOMING}^${Z_SAFE_HOMING}^" \
    "${PIO_CONFIGS_DIR}"/Configuration.h
  #############################################################################
  GRID_MAX_POINTS_X="#define GRID_MAX_POINTS_X"
  GRID_MAX_POINTS_X_VALUE="5"
  sed -i -e \
    "s^${GRID_MAX_POINTS_X}.*^${GRID_MAX_POINTS_X} ${GRID_MAX_POINTS_X_VALUE}^" \
    "${PIO_CONFIGS_DIR}"/Configuration.h
  #############################################################################
  XY_PROBE_SPEED="#define XY_PROBE_SPEED"
  XY_PROBE_SPEED_VALUE="(150*60)"
  sed -i -e \
    "s^${XY_PROBE_SPEED} .*^${XY_PROBE_SPEED} ${XY_PROBE_SPEED_VALUE}^" \
    "${PIO_CONFIGS_DIR}"/Configuration.h
  #############################################################################

  # Configuration_adv.h
  #############################################################################
  PROBE_OFFSET_WIZARD="#define PROBE_OFFSET_WIZARD"
  sed -i -e \
    "s^//${PROBE_OFFSET_WIZARD}^${PROBE_OFFSET_WIZARD}^" \
    "${PIO_CONFIGS_DIR}"/Configuration_adv.h
  #############################################################################
  PROBE_OFFSET_WIZARD_START_Z="#define PROBE_OFFSET_WIZARD_START_Z"
  sed -i -e \
    "s^//${PROBE_OFFSET_WIZARD_START_Z}^${PROBE_OFFSET_WIZARD_START_Z}^" \
    "${PIO_CONFIGS_DIR}"/Configuration_adv.h
  #############################################################################
  BABYSTEP_ZPROBE_OFFSET="#define BABYSTEP_ZPROBE_OFFSET"
  sed -i -e \
    "s^//${BABYSTEP_ZPROBE_OFFSET}^${BABYSTEP_ZPROBE_OFFSET}^" \
    "${PIO_CONFIGS_DIR}"/Configuration_adv.h
  #############################################################################
fi
###############################################################################
echo "Yesterday I was clever, so I wanted to change the world.
Today I am wise, so I am changing myself.
Rumi"
# Just googled "changes quotes" result marking the successful script execution.
###############################################################################
