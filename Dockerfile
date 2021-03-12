ARG BASE_IMAGE=ubuntu
ARG UBUNTU_VERSION=20.04
ARG PYTHON_VERSION=3.8
ARG MARLIN_GIT_BRANCH="bugfix-2.0.x"
ARG TZ=Europe/Sofia
ARG MAINTAINER=b0bbyd1g1tal@protonmail.com

FROM ubuntu:${UBUNTU_VERSION}

ARG BASE_IMAGE
ARG UBUNTU_VERSION
ARG PYTHON_VERSION
ARG MARLIN_GIT_BRANCH
ARG TZ
ARG MAINTAINER

ARG DEBIAN_FRONTEND=noninteractive

ENV WORK_DIR=/Marlin-Firmware-Builder/ \
FIRMWARE_BIN_DIR=/firmware/ \
PIO_BOARD="STM32F103RET6_creality" \
BOARD="CrealityV427" \
MODEL="Ender-3 Pro" \
MANUFACTURER="Creality" \
CUSTOM_FIRMWARE_SETTINGS="BLTOUCH, PROBE_OFFSET_WIZARD, XY_PROBE_SPEED" \
MARLIN_GIT_BRANCH=${MARLIN_GIT_BRANCH} \
TZ=${TZ}
MAINTAINER=${MAINTAINER}

LABEL maintainer=b0bbyd1g1tal@protonmail.com \
project="Marlin-Firmware-Builder" \
OS="${BASE_IMAGE}:${UBUNTU_VERSION}" \
Python="${PYTHON_VERSION}" \
Timezone="${TZ}" \
Marlin-GitHub-Branch="${MARLIN_GIT_BRANCH}" \
3D-Printer.Manufacturer="${MANUFACTURER}" \
3D-Printer.Model="${MODEL}" \
3D-Printer.Board="${BOARD}" \
3D-Printer.PIO-Board="${PIO_BOARD}" \
3D-Printer.Image="${PRINTER_IMAGE}" \
Custom-Firmware-Settings="${CUSTOM_FIRMWARE_SETTINGS}"

#ADD scripts/ /usr/local/bin/
#
#RUN env && \
#apt-get update && \
##apt-get upgrade -y && \
#apt-get install --no-install-recommends -y \
#python${PYTHON_VERSION} \
#python-is-python3 \
#python3-pip \
#python3-distutils \
#git && \
#pip3 install --no-cache-dir platformio && \
#rm -rf /var/lib/apt/lists/* && \
#useradd -ms /bin/bash ${MAINTAINER}
#
#RUN mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
#chown ${MAINTAINER} ${WORK_DIR} ${FIRMWARE_BIN_DIR}
#
#USER ${MAINTAINER}
#WORKDIR ${WORK_DIR}
#
#RUN build_bootstrapper.py
#
#ENTRYPOINT firmware_builder.py
