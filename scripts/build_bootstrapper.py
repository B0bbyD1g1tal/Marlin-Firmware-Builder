#!/usr/bin/python3.8

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch
"""
import sys
from os import environ, chdir
from subprocess import run
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
from requests import get

###############################################################################
# Marlin GitHub Repositories
###############################################################################
PROJECT_DIR = Path(environ["WORK_DIR"])

MARLIN_GITHUB_URL = 'https://github.com/MarlinFirmware/'
MARLIN_BRANCHES = ["2.0.x", "bugfix-2.0.x"]

if "MARLIN_GIT_BRANCH" in environ and \
        environ["MARLIN_GIT_BRANCH"] in MARLIN_BRANCHES:
    BRANCH = environ["MARLIN_GIT_BRANCH"]

    MARLIN_FIRMWARE_REPO = \
        f'{MARLIN_GITHUB_URL}Marlin/archive/{BRANCH}.zip'
    # Configurations' Stable branch is import-2.0.x instead of 2.0.x
    MARLIN_CONFIG_REPO = \
        f'{MARLIN_GITHUB_URL}Configurations/archive/' \
        f'{"import-2.0.x" if BRANCH == "2.0.x" else BRANCH}.zip'

    fw_repo = get(MARLIN_FIRMWARE_REPO)
    fw_zip = ZipFile(BytesIO(fw_repo.content))
    fw_zip.extractall(PROJECT_DIR)

    conf_repo = get(MARLIN_CONFIG_REPO)
    conf_zip = ZipFile(BytesIO(conf_repo.content))
    conf_zip.extractall(PROJECT_DIR)
else:
    sys.exit('No "MARLIN_GIT_BRANCH" in ENVs !')
# Bootstrap PIO for Ender 3 Pro v4.2.7 or most 32bit boards using STM32
chdir(Path(f'{PROJECT_DIR}/Marlin-{environ["MARLIN_GIT_BRANCH"]}/'))
run(['pio', 'run', '-t', 'clean', '-e', 'STM32F103RET6_creality'], check=True)
