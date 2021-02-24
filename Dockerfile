FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
TZ=Europe/Sofia

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
software-properties-common \
apt-transport-https \
wget \
curl \
vim \
git \
# VS Code various requisites
python3-distutils \
libx11-xcb-dev \
libasound2

# Add VS Code repo and install it
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - && \
add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" && \
apt-get update && \
apt-get install -y code

# Create and use VS Code user
RUN useradd -ms /bin/bash vscode
USER vscode
WORKDIR /home/vscode/

# Install VS Code Extensions for Marlin
RUN code --install-extension ms-vscode.cpptools && \
code --install-extension platformio.platformio-ide && \
code --install-extension marlinfirmware.auto-build && \
code --list-extensions

# Clone MarlinFirmware and Configurations repos
# Import configs for Creality - Ender 3 Pro - v4.2.7 Board
RUN git clone -b bugfix-2.0.x https://github.com/MarlinFirmware/Marlin.git && \
git clone https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder.git && \
cp /home/vscode/Marlin-Firmware-Builder/configs/* /home/vscode/Marlin/Marlin/ && \
####################################
# platformio.ini
####################################
sed -i -e 's/default_envs = .*/default_envs = STM32F103RET6_creality/g' /home/vscode/Marlin/platformio.ini

