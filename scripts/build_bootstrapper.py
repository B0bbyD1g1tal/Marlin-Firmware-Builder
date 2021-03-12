#!/usr/bin/python3.8

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch
"""

from os import environ
from io import BytesIO
from pathlib import Path
from requests import get
from zipfile import ZipFile

###############################################################################
# Marlin GitHub Repositories
###############################################################################
PROJECT_DIR = Path(environ["WORK_DIR"])
MARLIN_GITHUB_URL = 'https://github.com/MarlinFirmware/'
FW = 'Marlin'
CONF = 'Configurations'
MARLIN_BRANCHES = ["2.0.x", "bugfix-2.0.x"]

if "MARLIN_GIT_BRANCH" in environ and \
        environ["MARLIN_GIT_BRANCH"] in MARLIN_BRANCHES:
    MARLIN_FIRMWARE_REPO = \
        f'{MARLIN_GITHUB_URL}{FW}/archive/{environ["MARLIN_GIT_BRANCH"]}.zip'
    # Configurations Stable branch is import-2.0.x instead of 2.0.x
    MARLIN_CONFIG_REPO = \
        f'{MARLIN_GITHUB_URL}{CONF}/archive/import-2.0.x.zip' if \
        environ["MARLIN_GIT_BRANCH"] == "2.0.x" else \
        f'{MARLIN_GITHUB_URL}{CONF}/archive/{environ["MARLIN_GIT_BRANCH"]}.zip'

    fw_repo = get(MARLIN_FIRMWARE_REPO)
    fw_zip = ZipFile(BytesIO(fw_repo.content))
    fw_zip.extractall(PROJECT_DIR)

    conf_repo = get(MARLIN_CONFIG_REPO)
    conf_zip = ZipFile(BytesIO(conf_repo.content))
    conf_zip.extractall(PROJECT_DIR)
