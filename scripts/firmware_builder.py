#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch if passed

Bootstraps PlatformIO default environment
sets environment for the specified Board if passed
"""
from datetime import datetime
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

# is_branch_ok = "MARLIN_GIT_BRANCH" in environ and \
#                environ["MARLIN_GIT_BRANCH"] and \
#                environ["MARLIN_GIT_BRANCH"] == current_git_branch
# is_printer_ok = "MANUFACTURER" in environ and environ["MANUFACTURER"] and \
#                 "MODEL" in environ and environ["MODEL"] and \
#                 "BOARD" in environ and environ["BOARD"] and \
#                 "PIO_BOARD" in environ and environ["PIO_BOARD"]
# if is_branch_ok and is_printer_ok:
#     copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
#              dirs_exist_ok=True)
#
#     PIO_DEFAULT_ENV = 'default_envs = '
#     run(['sed', '-i', '-e',
#          f's^{PIO_DEFAULT_ENV}.*^{PIO_DEFAULT_ENV}{environ["PIO_BOARD"]}^',
#          f'{PIO_PROJECT}/platformio.ini'],
#         check=True)

if "CUSTOM_FIRMWARE_SETTINGS" in environ and \
        environ["CUSTOM_FIRMWARE_SETTINGS"]:
    run('config-calibrator.sh', check=True)

run(['pio', 'run', '-e', environ["PIO_BOARD"]], check=True)

BUILD_DIR = Path(f'{PIO_PROJECT}/.pio/build/{environ["PIO_BOARD"]}/')
BINARY_FILE_NAME = f'{environ["MODEL"].replace(" ", "")}-\
{environ["BOARD"]}-\
{environ["MARLIN_GIT_BRANCH"]}-\
{datetime.now().strftime("%d-%b-%y_%H%M")}'

copyfile(f'{BUILD_DIR.glob("firmware-*bin")}',
         Path(f'{environ["FIRMWARE_BIN_DIR"]}/{BINARY_FILE_NAME}'))
