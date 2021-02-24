# Marlin-Firmware-Builder

```dockerfile
docker run -ti -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/b0bby/fw:/home/vscode/Marlin/.pio/build/ -e DISPLAY="unix${DISPLAY}" --device /dev/dri marlin-firmware-builder /bin/bash
```
