#!/usr/bin/python3.8

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
# Copy Configurations to Marlin Repository
###############################################################################
BRANCH = environ["MARLIN_GIT_BRANCH"]
configs_branch = 'import-2.0.x' if BRANCH == '2.0.x' else BRANCH

PROJECT_DIR = Path(environ["WORK_DIR"])
MARLIN_FW = Path(f'{PROJECT_DIR}/Marlin-{BRANCH}/')
MARLIN_CONFIGS = Path(f'{PROJECT_DIR}/Configurations-{configs_branch}/')

MARLIN_PRINTER_CONFIG = \
    Path(f'{MARLIN_CONFIGS}/config/examples/'
         f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')
PIO_CONFIGS = Path(f'{MARLIN_FW}/Marlin/')

copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
         dirs_exist_ok=True)

###############################################################################
# Platform IO Environment
###############################################################################
conf = Path(f'{MARLIN_PRINTER_CONFIG}/Configuration.h')
conf_adv = Path(f'{MARLIN_PRINTER_CONFIG}/Configuration_adv.h')
pins = Path(f'{MARLIN_FW}/Marlin/src/pins/pins.h')

motherboard = ''
pio = ''
with open(conf, 'r') as config:
    for line in config:
        if '#define MOTHERBOARD' in line:
            motherboard = line.strip().split(' ')[-1].replace('BOARD_', '')

with open(pins, 'r') as pin:
    for line in pin:
        if motherboard in line:
            pio = line.split()[-1].replace('env:', '')

print(motherboard)
print(pio)

run(['pio', 'run', '--target', 'clean' '-e' f'{pio}'], check=True)
run(['pio', 'system', 'prune', '-f'], check=True)

###############################################################################
# Custom Config
###############################################################################
if "CUSTOM_FIRMWARE_SETTINGS" in environ and \
        environ["CUSTOM_FIRMWARE_SETTINGS"]:
    run('config-calibrator.sh', check=True)

###############################################################################
# Build and deliver
###############################################################################
run(['pio', 'run', '-e', f'{pio}'], check=True)

BUILD_DIR = Path(f'{MARLIN_FW}/.pio/build/{pio}/')
BINARY_FILE_NAME = f'{environ["MODEL"].replace(" ", "")}-\
{environ["BOARD"] if environ["BOARD"] else "X"}_\
{environ["MARLIN_GIT_BRANCH"]}_\
{datetime.now().strftime("%d-%b-%y_%H%M")}'

copyfile(f'{BUILD_DIR.glob("firmware-*bin")}',
         f'{environ["FIRMWARE_BIN_DIR"]}/{BINARY_FILE_NAME}')
