import requests
from bs4 import  BeautifulSoup
html = requests.get("http://guba.eastmoney.com/news,zf,844116887.html")
data =  BeautifulSoup(html.text, "html.parser")
hrefs = data.select(".zwstock a")

for href in hrefs:

    print(href.get("href"),href.text)

    http://guba.eastmoney.com / news, zf, 844116887.html
    http: // guba.eastmoney.com / news, zf, 844274089.
    html`