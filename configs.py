import pathlib
import shutil
import subprocess

###############################################################################
# =============================================================================
# Set ENV variables
# =============================================================================
###############################################################################

PIO_DIR = "/home/b0bby/code/Marlin-Firmware-Builder/"  # or $(pwd)
GIT_BRANCH = "bugfix-2.0.x"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Names should be the same as in the Configurations repository path:
# https://github.com/MarlinFirmware/Configurations/tree/$GIT_BRANCH/config/examples/$MANUFACTURER/$MODEL/$BOARD/*.h
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MANUFACTURER = "Creality"
MODEL = "Ender-3 Pro"
BOARD = "CrealityV427"

PIO_BOARD_ENV = "STM32F103RET6_creality"
###############################################################################
# ==============================================================================
# Set script variables
# ==============================================================================
###############################################################################
AUTHOR = "B0bby D1g1tal"
# sed separator set to ^
SED = "^"

###############################################################################
# Marlin Github repositories and branch
###############################################################################
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
MARLIN_FW_REPO = "Marlin"
MARLIN_CONFIG_REPO = "Configurations"

###############################################################################
# Marlin Firmware and Configurations local paths
###############################################################################

CONFIGS_PATH = pathlib.Path(f"{PIO_DIR}{MARLIN_CONFIG_REPO}/config/examples/{MANUFACTURER}/{MODEL}/{BOARD}/")
MARLIN_PIO_PATH = pathlib.Path(f"{PIO_DIR}{MARLIN_FW_REPO}/Marlin/")
###############################################################################
# ==============================================================================
# Clone Marlin Firmware and Configurations repositories
# and copy Printer's configurations
# ==============================================================================
###############################################################################
subprocess.run(["git", "clone", "-b", f"{GIT_BRANCH}",
                f"{MARLIN_GITHUB_URL}{MARLIN_FW_REPO}.git"])
subprocess.run(["git", "clone", "-b", f"{GIT_BRANCH}",
                f"{MARLIN_GITHUB_URL}{MARLIN_CONFIG_REPO}.git"])

shutil.copytree(CONFIGS_PATH,
                MARLIN_PIO_PATH,
                dirs_exist_ok=True)

###############################################################################
# ==============================================================================
# Editing Printer's configuration files
# ==============================================================================
###############################################################################

###############################################################################
# platformio.ini
###############################################################################
DEFAULT_ENVS = "default_envs = "
subprocess.run(["sed", "- i", "- e",
                f"s{SED}{DEFAULT_ENVS}.*{SED}{DEFAULT_ENVS}{PIO_BOARD_ENV}{SED}"
                f"{PIO_DIR}{MARLIN_FW_REPO}/platformio.ini"])

###############################################################################
# Configuration.h
###############################################################################
STRING_CONFIG_H_AUTHOR = "#define STRING_CONFIG_H_AUTHOR"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}{STRING_CONFIG_H_AUTHOR} \"(.*,{SED}{STRING_CONFIG_H_AUTHOR} \"({AUTHOR},{SED}"
                f"{MARLIN_PIO_PATH}/Configuration.h"])

SERIAL_PORT_2 = "#define SERIAL_PORT_2"
subprocess.run(["sed", "- i", "- e",
                f"s//{SED}{SERIAL_PORT_2}.*{SED}{SERIAL_PORT_2} 3{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

BLTOUCH = "#define BLTOUCH"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{BLTOUCH}{SED}{BLTOUCH}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

AUTO_BED_LEVELING_BILINEAR = "#define AUTO_BED_LEVELING_BILINEAR"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{AUTO_BED_LEVELING_BILINEAR}{SED}{AUTO_BED_LEVELING_BILINEAR}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

Z_SAFE_HOMING = "#define Z_SAFE_HOMING"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{Z_SAFE_HOMING}{SED}{Z_SAFE_HOMING}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

NOZZLE_TO_PROBE_OFFSET = "#define NOZZLE_TO_PROBE_OFFSET"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}{NOZZLE_TO_PROBE_OFFSET} {10, 10, 0}{SED}{NOZZLE_TO_PROBE_OFFSET} {-42, -10, 0}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

GRID_MAX_POINTS_X = "#define GRID_MAX_POINTS_X"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}{GRID_MAX_POINTS_X} .{SED}{GRID_MAX_POINTS_X} 5{SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

XY_PROBE_SPEED = "#define XY_PROBE_SPEED"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}{XY_PROBE_SPEED} .*{SED}{XY_PROBE_SPEED} (150*60){SED}",
                f"{MARLIN_PIO_PATH}/Configuration.h"])

###############################################################################
# Configuration_adv.h
###############################################################################
PROBE_OFFSET_WIZARD = "#define PROBE_OFFSET_WIZARD"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{PROBE_OFFSET_WIZARD}{SED}{PROBE_OFFSET_WIZARD}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

PROBE_OFFSET_WIZARD_START_Z = "#define PROBE_OFFSET_WIZARD_START_Z"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{PROBE_OFFSET_WIZARD_START_Z}{SED}{PROBE_OFFSET_WIZARD_START_Z}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

BABYSTEP_ZPROBE_OFFSET = "#define BABYSTEP_ZPROBE_OFFSET"
subprocess.run(["sed", "- i", "- e",
                f"s{SED}//{BABYSTEP_ZPROBE_OFFSET}{SED}{BABYSTEP_ZPROBE_OFFSET}{SED}",
                f"{MARLIN_PIO_PATH}/Configuration_adv.h"])

###############################################################################
# -----------------------------------------------------------------------------#
###############################################################################
