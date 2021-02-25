# Marlin-Firmware-Builder

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
