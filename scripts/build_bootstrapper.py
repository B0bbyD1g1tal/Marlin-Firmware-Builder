#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch

Copies the Configurations into the PlatformIO Project
for the specified Manufacturer / 3D Printer / Board

Bootstraps PlatformIO build
for the selected Board
"""

from os import environ, chdir
from subprocess import run
from pathlib import Path

# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"

PIO_PROJECT = Path(
    f'{environ["WORK_DIR"]}{MARLIN_FIRMWARE_REPO}/')
PIO_CONFIGS = Path(
    f'{PIO_PROJECT}/Marlin/')
MARLIN_PRINTER_CONFIG = Path(
    f'{environ["WORK_DIR"]}{MARLIN_CONFIG_REPO}/config/examples/'
    f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')

# Clone Marlin repositories
chdir(environ["WORK_DIR"])
run(['git', 'clone', '-b',
     environ['GIT_BRANCH'],
     f'{MARLIN_GITHUB_URL}{MARLIN_FIRMWARE_REPO}.git'],
    check=True)
run(['git', 'clone', '-b',
     environ['GIT_BRANCH'],
     f'{MARLIN_GITHUB_URL}{MARLIN_CONFIG_REPO}.git'],
    check=True)

# Prune and prepare for build
chdir(PIO_PROJECT)
run(["pio", "system", "prune", "-f"],
    check=True)
run(["pio", "run", "--target", "clean"],
    check=True)
# TODO gather more info about boards listed as default_envs in PIO
# TODO goal: bootstrap all envs, without setting specific one
