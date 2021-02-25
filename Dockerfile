FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia \
PIO_DIR=/platformio/ \
FIRMWARE_BIN_DIR=/firmware/ \
GIT_BRANCH=bugfix-2.0.x \
PIO_BOARD_ENV=STM32F103RET6_creality

RUN mkdir ${PIO_DIR} ${FIRMWARE_BIN_DIR} && \
apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
git \
python3 \
python3-pip \
python3-distutils \
python-is-python3

ADD scripts/entrypoint.sh \
scripts/clone_fw_repos.py \
scripts/config_mixer.py \
scripts/config_editor.py \
/usr/local/bin/

RUN pip3 install -U platformio

WORKDIR ${PIO_DIR}

RUN clone_fw_repos.py
RUN config_mixer.py
RUN config_editor.py

ENTRYPOINT entrypoint.sh
