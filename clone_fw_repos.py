#!/usr/bin/python3

from os import chdir, environ
from subprocess import run

"""
Clone Marlin Firmware 
and Configurations repositories 
by branch
"""
# https://github.com/MarlinFirmware
MARLIN_GITHUB_URL = "https://github.com/MarlinFirmware/"
# git@github.com:MarlinFirmware/Marlin.git
MARLIN_FIRMWARE_REPO = "Marlin"
# git@github.com:MarlinFirmware/Configurations.git
MARLIN_CONFIG_REPO = "Configurations"
# bugfix-2.0.x is set by default
GIT_BRANCH = environ["GIT_BRANCH"]

chdir(environ["PIO_DIR"])
run(["git", "clone", "-b",
     f"{GIT_BRANCH}",
     f"{MARLIN_GITHUB_URL}{MARLIN_FIRMWARE_REPO}.git"])
run(["git", "clone", "-b",
     f"{GIT_BRANCH}",
     f"{MARLIN_GITHUB_URL}{MARLIN_CONFIG_REPO}.git"])
