FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
MANUFACTURER="Creality" \
MODEL="Ender-3 Pro" \
BOARD="CrealityV427" \
PIO_BOARD_ENV="STM32F103RET6_creality" \
GIT_BRANCH="bugfix-2.0.x" \
TZ="Europe/Sofia" \
PYTHON_VERSION="3.9" \
MARLIN_GITHUB_URL="https://github.com/MarlinFirmware/" \
MARLIN_FIRMWARE_REPO="Marlin" \
MARLIN_CONFIG_REPO="Configurations" \
WORK_DIR="/platformio/" \
FIRMWARE_BIN_DIR="/firmware/" \
AUTHOR="B0bby D1g1tal"

LABEL maintainer=${AUTHOR}

RUN mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
git \
python${PYTHON_VERSION} \
python3-pip \
python3-distutils \
python-is-python3

ADD scripts/entrypoint.sh \
scripts/process_fw_repos.py \
scripts/config_editor.py \
/usr/local/bin/

RUN pip3 install -U platformio

WORKDIR ${WORK_DIR}

RUN process_fw_repos.py && \
config_editor.py

ENTRYPOINT entrypoint.sh
