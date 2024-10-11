import requests
from bs4 import BeautifulSoup
import urllib.parse
import pathlib

pathlib.Path("./out/subject/test2/").mkdir(parents=True)

a = requests.get("http://192.168.62.56/exam/query.asp?learn_year=no&term=no&degree=%A4G%A6%7E%AF%C5&classification=%A4G%A4T%C3%FE%B2%D5&exam_class=no&subject_name=no&B1=%ACd%B8%DF&pg=%B8%F5%AD%B6")

soup = BeautifulSoup(a.content,"html5lib")
# print(a.encoding)

urls = soup.find_all("a")

print(f"http://192.168.62.56/exam/{urllib.parse.quote_plus(urls[2]['href'])}")

file = requests.get(f"http://192.168.62.56/exam/{urllib.parse.quote_plus(urls[2]['href'])}")

with open("out/test1.docx","wb") as f:
    f.write(file.content)