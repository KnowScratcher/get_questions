import requests
from bs4 import BeautifulSoup
import urllib.parse
import pathlib
import os

for j in range(1,90):
    a = requests.get(f"http://192.168.62.56/exam/query.asp?Page={j}")

    soup = BeautifulSoup(a.content,"html5lib")
    urls = soup.find_all("a")

    if not os.path.exists("out"):
        pathlib.Path("out").mkdir(parents=True)

    for i in urls:
        href:str = i['href']
        print(f"processing: http://192.168.62.56/exam/{urllib.parse.quote_plus(href)}")
        file = requests.get(f"http://192.168.62.56/exam/{urllib.parse.quote_plus(href)}")
        print(href)
        if not href.startswith("http") and "." in href:
            print(f"dir: out/{'/'.join(href.split('/')[:-1])}")
            if not os.path.exists("out/"+"/".join(href.split("/")[:-1])) and not "." in "/".join(href.split("/")[:-1]) and len(href.split("/")[:-1])!=0:
                print(f"makeing dir: out/{'/'.join(href.split('/')[:-1])}")
                pathlib.Path("out/"+"/".join(href.split("/")[:-1])).mkdir(parents=True)
            with open(f"out/{href}","wb") as f:
                f.write(file.content)
        else:
            print(f"{href} starts with a http")