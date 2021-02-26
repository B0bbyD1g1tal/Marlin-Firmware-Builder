FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ="Europe/Sofia" \
MANUFACTURER="Creality" \
MODEL="Ender-3 Pro" \
BOARD="CrealityV427" \
PIO_BOARD_ENV="STM32F103RET6_creality" \
GIT_BRANCH="bugfix-2.0.x" \
PYTHON_VERSION="3.9" \
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
scripts/config-calibrator.sh \
scripts/build_bootstrapper.py \
/usr/local/bin/

RUN pip3 install -U platformio

RUN build_bootstrapper.py && \
config-calibrator.sh

ENTRYPOINT entrypoint.sh
