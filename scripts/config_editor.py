#!/usr/bin/python3

"""
Edits firmware configuration files
"""

from os import environ
from subprocess import run
from pathlib import Path

# flake8: noqa: E501
# pylint: disable=C0301

PIO_PROJECT_DIR = Path(
    f'{environ["WORK_DIR"]}{environ["MARLIN_FIRMWARE_REPO"]}/')
PIO_CONFIGS_DIR = Path(
    f'{PIO_PROJECT_DIR}/Marlin/')

# Configuration.h
STRING_CONFIG_H_AUTHOR = '#define STRING_CONFIG_H_AUTHOR'
run(['sed', '-i', '-e',
     f's^{STRING_CONFIG_H_AUTHOR} \"(.*,^{STRING_CONFIG_H_AUTHOR} \"({environ["AUTHOR"]},^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

SERIAL_PORT_2 = '#define SERIAL_PORT_2'
SERIAL_PORT_2_VALUE = "3"
run(['sed', '-i', '-e',
     f's^//{SERIAL_PORT_2} .*^{SERIAL_PORT_2} {SERIAL_PORT_2_VALUE}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

BLTOUCH = '#define BLTOUCH'
run(['sed', '-i', '-e',
     f's^//{BLTOUCH}^{BLTOUCH}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

AUTO_BED_LEVELING_BILINEAR = '#define AUTO_BED_LEVELING_BILINEAR'
run(['sed', '-i', '-e',
     f's^//{AUTO_BED_LEVELING_BILINEAR}^{AUTO_BED_LEVELING_BILINEAR}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

Z_SAFE_HOMING = '#define Z_SAFE_HOMING'
run(['sed', '-i', '-e',
     f's^//{Z_SAFE_HOMING}^{Z_SAFE_HOMING}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

GRID_MAX_POINTS_X = '#define GRID_MAX_POINTS_X'
GRID_MAX_POINTS_X_VALUE = "5"
run(['sed', '-i', '-e',
     f's^{GRID_MAX_POINTS_X}.*^{GRID_MAX_POINTS_X} {GRID_MAX_POINTS_X_VALUE}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

XY_PROBE_SPEED = '#define XY_PROBE_SPEED'
XY_PROBE_SPEED_VALUE = "(150*60)"
run(['sed', '-i', '-e',
     f's^{XY_PROBE_SPEED} .*^{XY_PROBE_SPEED} {XY_PROBE_SPEED_VALUE}^',
     f'{PIO_CONFIGS_DIR}/Configuration.h'],
    check=True)

# Configuration_adv.h
PROBE_OFFSET_WIZARD = '#define PROBE_OFFSET_WIZARD'
run(['sed', '-i', '-e',
     f's^//{PROBE_OFFSET_WIZARD}^{PROBE_OFFSET_WIZARD}^',
     f'{PIO_CONFIGS_DIR}/Configuration_adv.h'],
    check=True)

PROBE_OFFSET_WIZARD_START_Z = '#define PROBE_OFFSET_WIZARD_START_Z'
run(['sed', '-i', '-e',
     f's^//{PROBE_OFFSET_WIZARD_START_Z}^{PROBE_OFFSET_WIZARD_START_Z}^',
     f'{PIO_CONFIGS_DIR}/Configuration_adv.h'],
    check=True)

BABYSTEP_ZPROBE_OFFSET = '#define BABYSTEP_ZPROBE_OFFSET'
run(['sed', '-i', '-e',
     f's^//{BABYSTEP_ZPROBE_OFFSET}^{BABYSTEP_ZPROBE_OFFSET}^',
     f'{PIO_CONFIGS_DIR}/Configuration_adv.h'],
    check=True)
