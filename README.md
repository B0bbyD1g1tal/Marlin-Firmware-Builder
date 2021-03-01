# Marlin-Firmware-Builder
[![Flake8](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/Flake8.yml/badge.svg?event=check_run)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/Flake8.yml)
[![MyPy](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/MyPy.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/MyPy.yml)
[![PyLint](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/PyLint.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/PyLint.yml)
[![ShellCheck](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/ShellCheck.yml/badge.svg)](https://github.com/B0bbyD1g1tal/Marlin-Firmware-Builder/actions/workflows/ShellCheck.yml)

```bash
# Marlin-Firmware-Builder
cd "${Marlin-Firmware-Builder}folder/"

docker run -ti \
-v $(pwd)/firmware/:/firmware/ \
marlin-firmware-builder:latest
```

```bash
# TODO VS-Code 
docker run -ti \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY="unix${DISPLAY}" \
--device /dev/dri \
marlin-firmware-builder-code:latest
```
