import requests
url_data = requests.get("http://iguba.eastmoney.com/myfollowperson")
print(url_data.text)