#!/usr/bin/python3

"""
Edits firmware config files
"""
from os import chdir, environ, rmdir
from subprocess import run
from pathlib import Path

# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"

FIRMWARE_BIN_DIR = environ["FIRMWARE_BIN_DIR"]
PIO_DIR = environ["PIO_DIR"]
PIO_BOARD_ENV = environ["PIO_BOARD_ENV"]

PROJECT_DIR = Path(f"{PIO_DIR}{MARLIN_FIRMWARE_REPO}/")
chdir(PROJECT_DIR)
BUILD_DIR = Path(f"{PROJECT_DIR}/.pio/build/")
rmdir(BUILD_DIR)

run(["pio", "run", "-e", PIO_BOARD_ENV],
    check=True)
run(["cp", f"{BUILD_DIR}{PIO_BOARD_ENV}/firmware-*.bin", FIRMWARE_BIN_DIR],
    check=True)
