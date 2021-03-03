#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch if passed

Bootstraps PlatformIO default environment
sets environment for the specified Board if passed
"""

from os import environ, chdir
from subprocess import run
from pathlib import Path
from shutil import copytree

###############################################################################
# Marlin
###############################################################################
chdir(Path(environ["WORK_DIR"]))

MARLIN_FIRMWARE_REPO = 'https://github.com/MarlinFirmware/Marlin.git'
MARLIN_CONFIG_REPO = 'https://github.com/MarlinFirmware/Configurations.git'
MARLIN_BRANCHES = ["2.0.x", "bugfix-2.0.x"]

if "MARLIN_GIT_BRANCH" in environ and \
        environ["MARLIN_GIT_BRANCH"] in MARLIN_BRANCHES:
    # Marlin Stable branch is 2.0.x
    git_firmware = ['git', 'clone', '-b', environ["MARLIN_GIT_BRANCH"],
                    MARLIN_FIRMWARE_REPO]
    if environ["MARLIN_GIT_BRANCH"] == "2.0.x":
        # Configurations Stable branch is import-2.0.x
        git_configs = ['git', 'clone', '-b', "import-2.0.x",
                       MARLIN_CONFIG_REPO]
    else:
        git_configs = ['git', 'clone', '-b', environ["MARLIN_GIT_BRANCH"],
                       MARLIN_CONFIG_REPO]
    # Clone Marlin repositories
    run(git_firmware, check=True)
    run(git_configs, check=True)

PIO_PROJECT = Path(f'{environ["WORK_DIR"]}Marlin/')
# Add the specified 3D-Printer configuration and set default Board environment
if environ["MARLIN_GIT_BRANCH"] in MARLIN_BRANCHES and \
        "MANUFACTURER" in environ and \
        "MODEL" in environ and \
        "BOARD" in environ and \
        "PIO_BOARD" in environ:
    MARLIN_PRINTER_CONFIG = Path(
        f'{environ["WORK_DIR"]}/Configurations/config/examples/'
        f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')
    PIO_CONFIGS = Path(f'{PIO_PROJECT}/Marlin/')
    # Copy Marlin 3D-Printer configuration
    copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
             dirs_exist_ok=True)
    # Set PIO Project's default Board environment
    PIO_DEFAULT_ENV = 'default_envs = '
    run(['sed', '-i', '-e',
         f's^{PIO_DEFAULT_ENV}.*^{PIO_DEFAULT_ENV}{environ["PIO_BOARD"]}^',
         f'{PIO_PROJECT}/platformio.ini'],
        check=True)
###############################################################################
# Platform IO
###############################################################################
if environ["MARLIN_GIT_BRANCH"] in MARLIN_BRANCHES:
    chdir(PIO_PROJECT)

    run(['pio', 'run', '--target', 'clean'], check=True)
    run(['pio', 'system', 'prune', '-f'], check=True)

###############################################################################
