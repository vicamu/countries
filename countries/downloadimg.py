import requests as res

res = res.get("https://restcountries.eu/data/esp.svg").content

with open("img.svg", "wb") as file:
    file.write(res)