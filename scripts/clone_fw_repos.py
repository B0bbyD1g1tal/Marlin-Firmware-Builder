#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
"""

from os import chdir, environ
from subprocess import run

# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"

GIT_BRANCH = environ["GIT_BRANCH"]

chdir(environ["PIO_DIR"])
run(["git", "clone", "-b",
     f"{GIT_BRANCH}",
     f"{MARLIN_GITHUB_URL}{MARLIN_FIRMWARE_REPO}.git"],
    check=True)
run(["git", "clone", "-b",
     f"{GIT_BRANCH}",
     f"{MARLIN_GITHUB_URL}{MARLIN_CONFIG_REPO}.git"],
    check=True)
