#!/usr/bin/python3

from os import chdir, environ
from subprocess import run
from pathlib import Path
from shutil import copytree

###############################################################################
# =============================================================================
# Set ENV variables
# =============================================================================
###############################################################################
PIO_DIR = environ["PIO_DIR"]
FIRMWARE_BIN_DIR = environ["FIRMWARE_BIN_DIR"]
PIO_BOARD_ENV = environ["PIO_BOARD_ENV"]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Names should be the same as in the Configurations repository path:
# https://github.com/MarlinFirmware/Configurations/tree/$GIT_BRANCH/config/examples/$MANUFACTURER/$MODEL/$BOARD/*.h
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MANUFACTURER = "Creality"
MODEL = "Ender-3 Pro"
BOARD = "CrealityV427"
###############################################################################
# ==============================================================================
# Set script variables
# ==============================================================================
###############################################################################
AUTHOR = "B0bby D1g1tal"
# sed separator set to ^
SED = "^"
# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"
###############################################################################
# Marlin Firmware and Configurations local paths
###############################################################################
CONFIGS_PATH = Path(f"{PIO_DIR}{MARLIN_CONFIG_REPO}/config/examples/{MANUFACTURER}/{MODEL}/{BOARD}/")
MARLIN_PIO_PATH = Path(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/Marlin/")

copytree(CONFIGS_PATH,
         MARLIN_PIO_PATH,
         dirs_exist_ok=True)

# Prepare env for build
chdir(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}")
run(["pio", "run", "--target", "clean"])

###############################################################################
# ==============================================================================
# Editing Printer's configuration files
# ==============================================================================
###############################################################################

###############################################################################
# platformio.ini
###############################################################################
DEFAULT_ENVS = "default_envs = "
run(["sed", "-i", "-e",
     f"s{SED}{DEFAULT_ENVS}.*{SED}{DEFAULT_ENVS}{PIO_BOARD_ENV}{SED}",
     f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/platformio.ini"])

###############################################################################
# Configuration.h
###############################################################################
STRING_CONFIG_H_AUTHOR = "#define STRING_CONFIG_H_AUTHOR"
run(["sed", "-i", "-e",
     f"s{SED}{STRING_CONFIG_H_AUTHOR} \"(.*,{SED}{STRING_CONFIG_H_AUTHOR} \"({AUTHOR},{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

SERIAL_PORT_2 = "#define SERIAL_PORT_2"
run(["sed", "-i", "-e",
     f"s{SED}//{SERIAL_PORT_2} .*{SED}{SERIAL_PORT_2} 3{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

BLTOUCH = "#define BLTOUCH"
run(["sed", "-i", "-e",
     f"s{SED}//{BLTOUCH}{SED}{BLTOUCH}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

AUTO_BED_LEVELING_BILINEAR = "#define AUTO_BED_LEVELING_BILINEAR"
run(["sed", "-i", "-e",
     f"s{SED}//{AUTO_BED_LEVELING_BILINEAR}{SED}{AUTO_BED_LEVELING_BILINEAR}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

Z_SAFE_HOMING = "#define Z_SAFE_HOMING"
run(["sed", "-i", "-e",
     f"s{SED}//{Z_SAFE_HOMING}{SED}{Z_SAFE_HOMING}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

# NOZZLE_TO_PROBE_OFFSET = "#define NOZZLE_TO_PROBE_OFFSET"
# run(["sed", "-i", "-e",
#                 f"s{SED}{NOZZLE_TO_PROBE_OFFSET}.*{SED}{NOZZLE_TO_PROBE_OFFSET} {-42, -10, 0}{SED}",
#                 f"{MARLIN_PIO_PATH}/Configuration.h"])

GRID_MAX_POINTS_X = "#define GRID_MAX_POINTS_X"
run(["sed", "-i", "-e",
     f"s{SED}{GRID_MAX_POINTS_X}.*{SED}{GRID_MAX_POINTS_X} 5{SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

XY_PROBE_SPEED = "#define XY_PROBE_SPEED"
run(["sed", "-i", "-e",
     f"s{SED}{XY_PROBE_SPEED} .*{SED}{XY_PROBE_SPEED} (150*60){SED}",
     f"{MARLIN_PIO_PATH}/Configuration.h"])

###############################################################################
# Configuration_adv.h
###############################################################################
PROBE_OFFSET_WIZARD = "#define PROBE_OFFSET_WIZARD"
run(["sed", "-i", "-e",
     f"s{SED}//{PROBE_OFFSET_WIZARD}{SED}{PROBE_OFFSET_WIZARD}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

PROBE_OFFSET_WIZARD_START_Z = "#define PROBE_OFFSET_WIZARD_START_Z"
run(["sed", "-i", "-e",
     f"s{SED}//{PROBE_OFFSET_WIZARD_START_Z}{SED}{PROBE_OFFSET_WIZARD_START_Z}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

BABYSTEP_ZPROBE_OFFSET = "#define BABYSTEP_ZPROBE_OFFSET"
run(["sed", "-i", "-e",
     f"s{SED}//{BABYSTEP_ZPROBE_OFFSET}{SED}{BABYSTEP_ZPROBE_OFFSET}{SED}",
     f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

###############################################################################
# --------------------------------------------------------------------------- #
###############################################################################
