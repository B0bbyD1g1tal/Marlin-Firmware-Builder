#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
by the specified Git-Branch if passed

Bootstraps PlatformIO default environment
sets environment for the specified Board if passed
"""

from os import environ, chdir
from shutil import copytree
from subprocess import run
from pathlib import Path

###############################################################################
# Marlin
###############################################################################
MARLIN_FIRMWARE_REPO = 'git@github.com:MarlinFirmware/Marlin.git'
MARLIN_CONFIG_REPO = 'git@github.com:MarlinFirmware/Configurations.git'
# By default is pulling from 2.0.x Stable branch
git_firmware = ['git', 'clone', MARLIN_FIRMWARE_REPO]
git_configs = ['git', 'clone', MARLIN_CONFIG_REPO]
# TODO Get list of available branches and check against them !
# remote_branches = run(["git", "branch", "-r"]) kind of ...
# default_branch = "origin/HEAD -> origin/2.0.x"
if environ["GIT_BRANCH"]:
    git_firmware = ['git', 'clone', '-b', environ["GIT_BRANCH"],
                    MARLIN_FIRMWARE_REPO]
    git_configs = ['git', 'clone', '-b', environ["GIT_BRANCH"],
                   MARLIN_CONFIG_REPO]
# Clone Marlin repositories
chdir(Path(environ["WORK_DIR"]))
run(git_firmware, check=True)
run(git_configs, check=True)
# Add the specified 3D-Printer config in PIO project, if all ENVs are available
# TODO images must be tagged with printer's name if used # pylint: disable=fixme
# TODO inspect case of 2 different printers on build and runtime # pylint: disable=fixme
if environ["MANUFACTURER"] and environ["MODEL"] and environ["BOARD"]:
    MARLIN_PRINTER_CONFIG = Path(
        f'{environ["WORK_DIR"]}{MARLIN_CONFIG_REPO}/config/examples/'
        f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')
    PIO_CONFIGS = Path(f'{environ["WORK_DIR"]}/Marlin/Marlin/')
    copytree(MARLIN_PRINTER_CONFIG, PIO_CONFIGS,
             dirs_exist_ok=True)

###############################################################################
# Platform IO
###############################################################################
PIO_PROJECT = Path(f'{environ["WORK_DIR"]}Marlin/')
# Set the default board environment in platformio.ini
if environ['PIO_BOARD']:
    PIO_DEFAULT_ENV = 'default_envs = '
    run(['sed', '-i', '-e',
         f's^{PIO_DEFAULT_ENV}.*^{PIO_DEFAULT_ENV}{environ["PIO_BOARD"]}^',
         f'{PIO_PROJECT}/platformio.ini'],
        check=True)
# Prune project and prepare for build
chdir(PIO_PROJECT)
run(['pio', 'system', 'prune', '-f'],
    check=True)
run(['pio', 'run', '--target', 'clean'],
    check=True)
###############################################################################
