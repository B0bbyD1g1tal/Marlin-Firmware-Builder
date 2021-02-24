#!/usr/bin/env bash

ENDER_3_PRO_V427_REPO="https://raw.githubusercontent.com/MarlinFirmware/Configurations/bugfix-2.0.x/config/examples/Creality/Ender-3%20Pro/CrealityV427/"
CONFIG_FILES="Configuration.h Configuration_adv.h _Bootscreen.h _Statusscreen.h"

for config in $CONFIG_FILES; do
  echo "Downloading ${ENDER_3_PRO_V427_REPO}/${config}"
  curl -Ls "${ENDER_3_PRO_V427_REPO}${config}" -o "./configs/${config}"
done


####################################
# Configuration.h
####################################
sed -i -e 's^#define STRING_CONFIG_H_AUTHOR "(.*,^#define STRING_CONFIG_H_AUTHOR \"(B0bbyD1g1tal,^g' ./configs/Configuration.h

sed -i -e 's^//#define BLTOUCH^#define BLTOUCH^g' ./configs/Configuration.h
sed -i -e 's^//#define AUTO_BED_LEVELING_BILINEAR^#define AUTO_BED_LEVELING_BILINEAR^g' ./configs/Configuration.h
sed -i -e 's^//#define Z_SAFE_HOMING^#define Z_SAFE_HOMING^g' ./configs/Configuration.h
sed -i -e 's^#define NOZZLE_TO_PROBE_OFFSET { 10, 10, 0 }^#define NOZZLE_TO_PROBE_OFFSET { -42, -10, 0 }^g' ./configs/Configuration.h
sed -i -e 's^  #define GRID_MAX_POINTS_X 3^  #define GRID_MAX_POINTS_X 5^g' ./configs/Configuration.h
sed -i -e 's^#define XY_PROBE_SPEED (133*60)^#define XY_PROBE_SPEED (150*60)^g' ./configs/Configuration.h

####################################
# Configuration_adv.h
####################################
sed -i -e 's^    //#define PROBE_OFFSET_WIZARD^    #define PROBE_OFFSET_WIZARD^g' ./configs/Configuration_adv.h
sed -i -e 's^      //#define PROBE_OFFSET_WIZARD_START_Z^      #define PROBE_OFFSET_WIZARD_START_Z^g' ./configs/Configuration_adv.h
sed -i -e 's^  //#define BABYSTEP_ZPROBE_OFFSET^  #define BABYSTEP_ZPROBE_OFFSET^g' ./configs/Configuration_adv.h
