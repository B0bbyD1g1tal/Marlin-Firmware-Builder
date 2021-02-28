FROM ubuntu:20.04

ENV WORK_DIR="/Marlin-Firmware-Builder /" \
FIRMWARE_BIN_DIR="/firmware/" \
DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia \
#UBUNTU_VESION="20.04" \
#PYTHON_VERSION="3.9" \
#GIT_BRANCH="bugfix-2.0.x" \
#MANUFACTURER="Creality" \
#MODEL="Ender-3 Pro" \
#BOARD="CrealityV427" \
#PIO_BOARD="STM32F103RET6_creality" \
#CUSTOM_CONFIG="yes" \
AUTHOR="B0bby D1g1tal"
#LABEL project="Marlin Firmware Builder"
#LABEL marlin-git-branch="${GIT_BRANCH}"
#LABEL 3d-printer-manufacturer="${MANUFACTURER}"
#LABEL 3d-printer-model="${MODEL}"
#LABEL 3d-printer-board="${BOARD}"
#LABEL pio-board="${PIO_BOARD}"
#LABEL os="${BASE_IMAGE_NAME}:${UBUNTU_VESION}"
#LABEL python-version="python${PYTHON_VERSION}"
#LABEL timezone="${TZ}"
#LABEL maintainer="${AUTHOR}"

RUN mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
python3.9 \
python3-pip \
python3-distutils \
python-is-python3 \
git

ADD scripts/ /

RUN pip3 install -U platformio

RUN /build_bootstrapper.py && \
/config-calibrator.sh

ENTRYPOINT /entrypoint.sh
