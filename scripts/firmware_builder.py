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
from shutil import copytree, copyfile

###############################################################################
#
###############################################################################
PIO_PROJECT = Path(f'{environ["WORK_DIR"]}Marlin/')
PIO_CONFIGS = Path(f'{PIO_PROJECT}/Marlin/')
MARLIN_PRINTER_CONFIG = Path(
    f'{environ["WORK_DIR"]}/Configurations/config/examples/'
    f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')

chdir(PIO_PROJECT)
current_git_branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                         check=True)
branch_ok = "MARLIN_GIT_BRANCH" in environ and \
            environ["MARLIN_GIT_BRANCH"] == current_git_branch

if branch_ok and \
        "MANUFACTURER" in environ and \
        "MODEL" in environ and \
        "BOARD" in environ and \
        "PIO_BOARD" in environ and \
        "PRINTER_IMAGE" not in environ:
    copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
             dirs_exist_ok=True)

    PIO_DEFAULT_ENV = 'default_envs = '
    run(['sed', '-i', '-e',
         f's^{PIO_DEFAULT_ENV}.*^{PIO_DEFAULT_ENV}{environ["PIO_BOARD"]}^',
         f'{PIO_PROJECT}/platformio.ini'],
        check=True)

if "PRINTER_IMAGE" in environ and \
        "CUSTOM_FIRMWARE_SETTINGS" in environ and \
        environ["CUSTOM_FIRMWARE_SETTINGS"]:
    run('config-calibrator.sh', check=True)

run(['pio', 'run', '-e', environ["PIO_BOARD"]], check=True)

BUILD_DIR = Path(f'{PIO_PROJECT}/.pio/build/{environ["PIO_BOARD"]}/')
copyfile(f'{BUILD_DIR.glob("firmware-*bin")}',
         Path(environ["FIRMWARE_BIN_DIR"]))
