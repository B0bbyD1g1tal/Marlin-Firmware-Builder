#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch

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

# Platform IO Project bootstrap
PIO_PROJECT = Path(
    f'{environ["WORK_DIR"]}{MARLIN_FIRMWARE_REPO}/')
# Replace Default ENV in platformio.ini
if environ["PIO_BOARD"]:
    PIO_DEFAULT_ENV = 'default_envs = '
    run(['sed', '-i', '-e',
         f's^{PIO_DEFAULT_ENV}.*^{PIO_DEFAULT_ENV}{environ["PIO_BOARD"]}^',
         f'{PIO_PROJECT}/platformio.ini'],
        check=True)

# Prune and prepare for build
chdir(PIO_PROJECT)
run(["pio", "system", "prune", "-f"],
    check=True)
run(["pio", "run", "--target", "clean"],
    check=True)
