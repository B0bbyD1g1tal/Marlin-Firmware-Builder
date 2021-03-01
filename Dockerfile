ARG BASE_IMAGE=ubuntu
ARG UBUNTU_VESION=20.04
ARG PYTHON_VERSION=3.8
ARG TZ=Europe/Sofia
ARG DEBIAN_FRONTEND=noninteractive
ARG MAINTAINER=B0bbyD1g1tal

FROM ${BASE_IMAGE}:${UBUNTU_VESION}

ARG DEBIAN_FRONTEND=${DEBIAN_FRONTEND}

ENV MARLIN_GIT_BRANCH=${MARLIN_GIT_BRANCH} \
BASE_IMAGE=${BASE_IMAGE} \
UBUNTU_VESION=${UBUNTU_VESION} \
PYTHON_VERSION=${PYTHON_VERSION} \
TZ=${TZ} \
MANUFACTURER="Creality" \
MODEL="Ender-3 Pro" \
BOARD="CrealityV427" \
PIO_BOARD="STM32F103RET6_creality" \
CUSTOM_FIRMWARE_SETTINGS="BLTouch and faster z homing" \
FIRMWARE_BIN_DIR=/firmware/ \
WORK_DIR=/Marlin-Firmware-Builder/ \
MAINTAINER=${MAINTAINER}

LABEL project="Marlin-Firmware-Builder" \
base-image="${BASE_IMAGE}" \
base-image.version="${UBUNTU_VESION}" \
OS="${BASE_IMAGE}:${UBUNTU_VESION}" \
Python="${PYTHON_VERSION}" \
Timezone="${TZ}" \
Marlin-GitHub-Branch="${MARLIN_GIT_BRANCH}" \
3D-Printer.Manufacturer="${MANUFACTURER}" \
3D-Printer.Model="${MODEL}" \
3D-Printer.Board="${BOARD}" \
3D-Printer.PIO-Board="${PIO_BOARD}" \
3D-Printer.Full-Name="${MANUFACTURER}-${MODEL}, ${BOARD}:${PIO_BOARD}" \
Custom-Firmware-Settings="${CUSTOM_FIRMWARE_SETTINGS}" \
maintainer="${MAINTAINER}"

ADD scripts/ /usr/local/bin/

RUN useradd -ms /bin/bash ${MAINTAINER}
RUN mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
chown ${MAINTAINER} ${WORK_DIR} ${FIRMWARE_BIN_DIR}

RUN apt-get update && \
#apt-get upgrade -y && \
apt-get install --no-install-recommends -y \
python${PYTHON_VERSION} \
python-is-python3 \
python3-pip \
python3-distutils \
git && \
rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir platformio

USER ${MAINTAINER}
WORKDIR ${WORK_DIR}

RUN build_bootstrapper.py

ENTRYPOINT entrypoint.sh
