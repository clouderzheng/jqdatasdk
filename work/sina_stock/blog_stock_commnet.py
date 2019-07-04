import requests
import  http_request_util
#获取新浪首页数据
sina_home_page = "https://finance.sina.com.cn/stock/"
soup = http_request_util.get_request_data(sina_home_page)

#筛选出热门博客
_a_blog = soup.select("ul.clearfix li a")

for a in _a_blog:
    print(a["href"],a.text)
