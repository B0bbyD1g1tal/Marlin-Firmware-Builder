# Marlin Firmware Builder
[![PyLint](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/PyLint.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/PyLint.yml)
[![Flake8](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/Flake8.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/Flake8.yml)
[![MyPy](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/MyPy.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/MyPy.yml)
[![ShellCheck](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/ShellCheck.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/ShellCheck.yml)


```bash
docker run -ti \
--env-file builder.env \
-v $(pwd)/firmware/:/firmware/ \
b0bbyd1g1tal/marlin-firmware-builder:latest
```

```bash
docker run -ti -v $(pwd)/firmware/:/firmware/ \
-e MANUFACTURER="Creality" \
MODEL="Ender-3 Pro" \
BOARD="CrealityV427" \
PIO_BOARD="STM32F103RET6_creality" \
CUSTOM_FIRMWARE_SETTINGS="BLTouch and faster z homing" \
b0bbyd1g1tal/marlin-firmware-builder:latest
```