FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia \
PIO_DIR="/platformio/" \
FIRMWARE_BIN_DIR="/firmware/" \
GIT_BRANCH="bugfix-2.0.x" \
PIO_BOARD_ENV="STM32F103RET6_creality"

RUN mkdir ${FIRMWARE_BIN_DIR} && \
apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
software-properties-common \
apt-transport-https \
curl \
python3 \
python3-pip \
python3-distutils \
python-is-python3

ADD ./get_configs.sh ./entrypoint.sh /usr/local/bin/

RUN pip install -U platformio

WORKDIR=

RUN platformio update && \
platformio lib update

ENTRYPOINT ["entrypoint.sh"]
