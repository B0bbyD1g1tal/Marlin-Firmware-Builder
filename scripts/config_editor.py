#!/usr/bin/python3

"""
Edits firmware config files
"""

from os import chdir, environ
from subprocess import run
from pathlib import Path

# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"

PIO_BOARD_ENV = environ["PIO_BOARD_ENV"]
PIO_DIR = environ["PIO_DIR"]
PIO_PATH = Path(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/Marlin/")

AUTHOR = "B0bby D1g1tal"  # Maybe ${USER} ...
SED = "^"

# Configuration.h
STRING_CONFIG_H_AUTHOR = "#define STRING_CONFIG_H_AUTHOR"
run(["sed", "-i", "-e",
     f"s{SED}{STRING_CONFIG_H_AUTHOR} \"(.*,{SED}{STRING_CONFIG_H_AUTHOR} \"({AUTHOR},{SED}",  # noqa: E501 pylint: disable=C0301
     f"{PIO_PATH}/Configuration.h"],
    check=True)

SERIAL_PORT_2 = "#define SERIAL_PORT_2"
run(["sed", "-i", "-e",
     f"s{SED}//{SERIAL_PORT_2} .*{SED}{SERIAL_PORT_2} 3{SED}",
     f"{PIO_PATH}/Configuration.h"],
    check=True)

BLTOUCH = "#define BLTOUCH"
run(["sed", "-i", "-e",
     f"s{SED}//{BLTOUCH}{SED}{BLTOUCH}{SED}",
     f"{PIO_PATH}/Configuration.h"],
    check=True)

AUTO_BED_LEVELING_BILINEAR = "#define AUTO_BED_LEVELING_BILINEAR"
run(["sed", "-i", "-e",
     f"s{SED}//{AUTO_BED_LEVELING_BILINEAR}{SED}{AUTO_BED_LEVELING_BILINEAR}{SED}",  # noqa: E501
     f"{PIO_PATH}/Configuration.h"],
    check=True)

Z_SAFE_HOMING = "#define Z_SAFE_HOMING"
run(["sed", "-i", "-e",
     f"s{SED}//{Z_SAFE_HOMING}{SED}{Z_SAFE_HOMING}{SED}",
     f"{PIO_PATH}/Configuration.h"],
    check=True)

GRID_MAX_POINTS_X = "#define GRID_MAX_POINTS_X"
run(["sed", "-i", "-e",
     f"s{SED}{GRID_MAX_POINTS_X}.*{SED}{GRID_MAX_POINTS_X} 5{SED}",
     f"{PIO_PATH}/Configuration.h"],
    check=True)

XY_PROBE_SPEED = "#define XY_PROBE_SPEED"
run(["sed", "-i", "-e",
     f"s{SED}{XY_PROBE_SPEED} .*{SED}{XY_PROBE_SPEED} (150*60){SED}",
     f"{PIO_PATH}/Configuration.h"],
    check=True)

# Configuration_adv.h
PROBE_OFFSET_WIZARD = "#define PROBE_OFFSET_WIZARD"
run(["sed", "-i", "-e",
     f"s{SED}//{PROBE_OFFSET_WIZARD}{SED}{PROBE_OFFSET_WIZARD}{SED}",
     f"{PIO_PATH}/Configuration_adv.h"],
    check=True)

PROBE_OFFSET_WIZARD_START_Z = "#define PROBE_OFFSET_WIZARD_START_Z"
run(["sed", "-i", "-e",
     f"s{SED}//{PROBE_OFFSET_WIZARD_START_Z}{SED}{PROBE_OFFSET_WIZARD_START_Z}{SED}",  # noqa: E501
     f"{PIO_PATH}/Configuration_adv.h"],
    check=True)

BABYSTEP_ZPROBE_OFFSET = "#define BABYSTEP_ZPROBE_OFFSET"
run(["sed", "-i", "-e",
     f"s{SED}//{BABYSTEP_ZPROBE_OFFSET}{SED}{BABYSTEP_ZPROBE_OFFSET}{SED}{PIO_PATH}/Configuration_adv.h"],  # noqa: E501 pylint: disable=C0301
    check=True)

# set default env in platformio.ini
DEFAULT_ENVS = "default_envs = "
run(["sed", "-i", "-e",
     f"s{SED}{DEFAULT_ENVS}.*{SED}{DEFAULT_ENVS}{PIO_BOARD_ENV}{SED}",
     f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/platformio.ini"],
    check=True)
# Prepare env for build
chdir(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}")
run(["pio", "run", "--target", "clean"],
    check=True)
