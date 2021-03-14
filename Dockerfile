ARG MARLIN_GIT_BRANCH="bugfix-2.0.x"
ARG BASE_IMAGE=ubuntu
ARG UBUNTU_VERSION=20.04
ARG PYTHON_VERSION=3.8
ARG TZ=Europe/Sofia
ARG MAINTAINER=B0bbyD1g1tal

FROM ${BASE_IMAGE}:${UBUNTU_VERSION}

ARG MARLIN_GIT_BRANCH
ARG BASE_IMAGE
ARG UBUNTU_VERSION
ARG PYTHON_VERSION
ARG TZ
ARG MAINTAINER
ARG DEBIAN_FRONTEND=noninteractive

ENV WORK_DIR=/Marlin-Firmware-Builder/ \
FIRMWARE_BIN_DIR=/firmware/ \
MARLIN_GIT_BRANCH=${MARLIN_GIT_BRANCH} \
TZ=${TZ} \
MAINTAINER=${MAINTAINER}

LABEL project=Marlin-Firmware-Builder \
OS=${BASE_IMAGE}:${UBUNTU_VERSION} \
Python=${PYTHON_VERSION} \
Timezone=${TZ} \
Marlin-GitHub-Branch=${MARLIN_GIT_BRANCH} \
maintainer=${MAINTAINER}

RUN env && \
apt-get update && \
#apt-get upgrade -y && \
apt-get install --no-install-recommends -y \
python${PYTHON_VERSION} \
python-is-python3 \
python3-pip \
python3-distutils && \
pip3 install platformio requests --no-cache-dir && \
rm -rf /var/lib/apt/lists/* && \
useradd -ms /bin/bash ${MAINTAINER} && \
mkdir ${WORK_DIR} ${FIRMWARE_BIN_DIR} && \
chown ${MAINTAINER} ${WORK_DIR} ${FIRMWARE_BIN_DIR}

ADD scripts/ /usr/local/bin/
USER ${MAINTAINER}
WORKDIR ${WORK_DIR}
RUN build_bootstrapper.py

ENTRYPOINT firmware_builder.py
