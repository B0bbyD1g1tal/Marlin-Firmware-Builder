from requests import get

url = 'https://github.com/MarlinFirmware/Marlin/archive/2.0.7.2.zip'

r = get(url, allow_redirects=True)

with open("marlin-fw", "w") as fw:
    fw.write(r.content)
