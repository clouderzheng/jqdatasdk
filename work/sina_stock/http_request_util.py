import requests
from bs4 import  BeautifulSoup
#自定义http请求工具类  封装为bs4格式
def get_request_data(url):
    url_date = requests.get(url)
    url_date.encoding = "utf-8"
    soup = BeautifulSoup(url_date.text, 'html.parser')
    return soup