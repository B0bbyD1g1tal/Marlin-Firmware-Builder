ARG BASE_IMAGE=ubuntu
ARG UBUNTU_VERSION=20.04


ARG PYTHON_VERSION=3.8
ARG TIMEZONE=Europe/London
ARG MARLIN_GIT_BRANCH="bugfix-2.0.x"
ARG AUTHOR=B0bbyD1g1tal
ARG DEBIAN_FRONTEND=noninteractive

FROM ${BASE_IMAGE}:${UBUNTU_VERSION}


ENV MARLIN_BRANCH=${MARLIN_GIT_BRANCH} \
WORK_DIR=/Marlin-Firmware-Builder/ \
FIRMWARE_BIN_DIR=/firmware/ \
#MANUFACTURER="Creality" \
#MODEL="Ender-3 Pro" \
#BOARD="CrealityV427" \
#PIO_BOARD="STM32F103RET6_creality" \
#CUSTOM_FIRMWARE_SETTINGS="BLTouch and faster z homing" \
#PRINTER_IMAGE="${MANUFACTURER}-${MODEL}, \
#${BOARD}:${PIO_BOARD} \
#${CUSTOM_FIRMWARE_SETTINGS}" \
TZ=${TIMEZONE} \
UBUNTU_BASE=${BASE_IMAGE}:${UBUNTU_VERSION} \
PYTHON=${PYTHON_VERSION} \
MAINTAINER=${AUTHOR}

LABEL project="Marlin-Firmware-Builder" \
OS="${UBUNTU_BASE}" \
Python="${PYTHON}" \
Timezone="${TZ}" \
Marlin-GitHub-Branch="${MARLIN_BRANCH}" \
3D-Printer.Manufacturer="${MANUFACTURER}" \
3D-Printer.Model="${MODEL}" \
3D-Printer.Board="${BOARD}" \
3D-Printer.PIO-Board="${PIO_BOARD}" \
3D-Printer.Full-Name="${PRINTER_IMAGE}" \
Custom-Firmware-Settings="${CUSTOM_FIRMWARE_SETTINGS}" \
maintainer="${MAINTAINER}"

ADD scripts/ /usr/local/bin/

RUN env && apt-get update && \
#apt-get upgrade -y && \
apt-get install --no-install-recommends -y \
#python${PYTHON_VERSION} \
python-is-python3 \
python3-pip \
python3-distutils \
git && \
pip3 install --no-cache-dir platformio && \
rm -rf /var/lib/apt/lists/* && \
useradd -ms /bin/bash ${MAINTAINER}

RUN mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
chown ${MAINTAINER} ${WORK_DIR} ${FIRMWARE_BIN_DIR}

USER ${MAINTAINER}
WORKDIR ${WORK_DIR}

RUN build_bootstrapper.py

ENTRYPOINT firmware_builder.py
