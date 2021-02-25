#!/usr/bin/python3

from os import environ
from pathlib import Path
from shutil import copytree

# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"

"""
Names should be the same as in the Configurations repository path:
https://github.com/MarlinFirmware/Configurations...
.../tree/$GIT_BRANCH/config/examples/$MANUFACTURER/$MODEL/$BOARD/*.h
"""
MANUFACTURER = "Creality"
MODEL = "Ender-3 Pro"
BOARD = "CrealityV427"

PIO_DIR = environ["PIO_DIR"]

CONFIGS_PATH = Path(f"{PIO_DIR}{MARLIN_CONFIG_REPO}/config/examples/{MANUFACTURER}/{MODEL}/{BOARD}/")
PIO_PATH = Path(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/Marlin/")

copytree(CONFIGS_PATH,
         PIO_PATH,
         dirs_exist_ok=True)
