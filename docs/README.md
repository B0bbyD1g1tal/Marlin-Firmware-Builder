### Welcome to GitHub Pages about 
# Marlin Firmware Builder
> a project by B0bbyD1g1tal in container

```bash
b0bby@d1g1tal:~$ 0_hello-friend
```

```bash
b0bby@d1g1tal:~/code/Marlin-Firmware-Builder$ docker run -ti \
-v $(pwd)/firmware/:/firmware/ \
b0bbyd1g1tal/marlin-firmware-builder:latest
```
```bash
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [==        ]  17.2% (used 11256 bytes from 65536 bytes)
Flash: [===       ]  34.7% (used 182012 bytes from 524288 bytes)
======================================================================= [SUCCESS] Took 26.44 seconds =======================================================================

Environment             Status    Duration
----------------------  --------  ------------
STM32F103RET6_creality  SUCCESS   00:00:26.438
======================================================================== 1 succeeded in 00:00:26.438 ========================================================================
```
```bash
b0bby@d1g1tal:~/code/Marlin-Firmware-Builder$ ll firmware/
total 208
drwxrwxr-x 2 b0bby b0bby   4096 Feb 27 01:47 ./
drwxrwxr-x 9 b0bby b0bby   4096 Feb 27 01:24 ../
-rwxr-xr-x 1 root  root  182012 Feb 27 01:47 firmware-20210226-234657.bin*
-rw-rw-r-- 1 b0bby b0bby     27 Feb 26 19:31 README.md
b0bby@d1g1tal:~/code/Marlin-Firmware-Builder$ date
Sat 27 Feb 2021 01:47:40 AM EET
```