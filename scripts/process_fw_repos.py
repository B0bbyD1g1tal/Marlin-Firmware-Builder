#!/usr/bin/python3

"""
Clones Marlin Firmware and Configurations repositories
"""

from os import environ, chdir
from subprocess import run
from pathlib import Path
from shutil import copytree

PIO_PROJECT_DIR = Path(
    f'{environ["WORK_DIR"]}{environ["MARLIN_FIRMWARE_REPO"]}/')
PIO_CONFIGS_DIR = Path(
    f'{PIO_PROJECT_DIR}/Marlin/')
PRINTER_CONFIG = Path(
    f'{environ["WORK_DIR"]}{environ["MARLIN_CONFIG_REPO"]}/config/examples/'
    f'{environ["MANUFACTURER"]}/{environ["MODEL"]}/{environ["BOARD"]}/')

# Clone Marlin repositories
run(['git', 'clone', '-b',
     environ['GIT_BRANCH'],
     f'{environ["MARLIN_GITHUB_URL"]}{environ["MARLIN_FIRMWARE_REPO"]}.git'],
    check=True)
run(['git', 'clone', '-b',
     environ['GIT_BRANCH'],
     f'{environ["MARLIN_GITHUB_URL"]}{environ["MARLIN_CONFIG_REPO"]}.git'],
    check=True)

# Copy selected printer configs to PIO project
copytree(PRINTER_CONFIG, PIO_CONFIGS_DIR, dirs_exist_ok=True)

# Set Default ENV in platformio.ini
DEFAULT_ENVS = 'default_envs = '
run(['sed', '-i', '-e',
     f's^{DEFAULT_ENVS}.*^{DEFAULT_ENVS}{environ["PIO_BOARD_ENV"]}^',
     f'{PIO_PROJECT_DIR}/platformio.ini'],
    check=True)

chdir(PIO_PROJECT_DIR)
run(["pio", "system", "prune", "-f"])
run(["pio", "run", "--target", "clean"])
