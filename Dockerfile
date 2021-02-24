FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia \
MARLIN_FIRMWARE_REPO=https://github.com/MarlinFirmware/Marlin.git \
MARLIN_CONFIG_REPO=https://github.com/MarlinFirmware/Configurations.git \
ENDER_3_PRO_V427_CONFIG_FILES=Configurations/config/examples/Creality/Ender-3\ Pro/CrealityV427/


RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
software-properties-common \
apt-transport-https \
wget \
git \
python3 \
python3-distutils \
libx11-xcb-dev \
libasound2

RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - && \
add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" && \
apt-get install -y code

RUN useradd -ms /bin/bash vscode
USER vscode
WORKDIR /home/vscode/

RUN code --install-extension MarlinFirmware.auto-build && \
code --list-extensions

RUN git clone https://github.com/MarlinFirmware/Marlin.git && \
git clone https://github.com/MarlinFirmware/Configurations.git && \
cp /home/vscode/Configurations/config/examples/Creality/Ender-3\ Pro/CrealityV427/* /home/vscode/Marlin/Marlin/
