FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
software-properties-common \
apt-transport-https \
curl \
nano \
git \
python3-distutils

RUN useradd -ms /bin/bash pio
USER pio
WORKDIR /home/pio/

RUN python3 -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"

RUN git clone -b bugfix-2.0.x https://github.com/MarlinFirmware/Marlin.git && \
git clone https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder.git && \
cp /home/vscode/Marlin-Firmware-Builder/configs/* /home/vscode/Marlin/Marlin/ && \
sed -i -e 's/default_envs = .*/default_envs = STM32F103RET6_creality/g' /home/vscode/Marlin/platformio.ini
