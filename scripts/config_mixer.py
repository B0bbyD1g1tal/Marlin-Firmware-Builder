#!/usr/bin/python3

"""
Adds configuration files for specific 3D Printer,
listed in examples in Configurations repository.

Names should be the same as in the Configurations repository path:
https://github.com/MarlinFirmware/Configurations...
.../tree/$GIT_BRANCH/config/examples/$MANUFACTURER/$MODEL/$BOARD/*.h
"""

from os import environ
from pathlib import Path
from shutil import copytree

MANUFACTURER = "Creality"
MODEL = "Ender-3 Pro"
BOARD = "CrealityV427"

# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"

PIO_DIR = environ["PIO_DIR"]
PIO_PATH = Path(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/Marlin/")
CONFIGS_PATH = Path(
    f"{PIO_DIR}{MARLIN_CONFIG_REPO}/config/examples/"
    f"{MANUFACTURER}/{MODEL}/{BOARD}/")

copytree(CONFIGS_PATH,
         PIO_PATH,
         dirs_exist_ok=True)
