import requests
from bs4 import BeautifulSoup
import  re
import xlwt
data = requests.get("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery11240949503730119142_1561385255779&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)%7D)&cmd=C.2&st=(ChangePercent)&sr=-1&p=1&ps=4000&_=1561385255821")
print(data.text)
# soup = BeautifulSoup(data.text, "html.parser")
# print(soup.title)

#去除前后缀 获取有效数据
find = re.search(r"{(.*)}",data.text,re.M|re.I)
if(find):
    d1 = find.group(1)
else:
    print("no such")

#按照每一个股票一组分组 分号开头 包含除分号之外的数据 即分号分割
find = re.findall(r'\"([^\"]*)\",',d1)

# 实例化一个Workbook()对象(即excel文件)
wbk = xlwt.Workbook()
#创建sheet  参数  sheet名称   是否允许覆盖重写
sheet = wbk.add_sheet("store",cell_overwrite_ok=True)



#格式设置
style = xlwt.XFStyle()#格式信息
font = xlwt.Font()#字体基本设置
font.name = u'微软雅黑'
font.color = 'red'
font.height= 220 #字体大小，220就是11号字体，大概就是11*20得来的吧
style.font = font


#创建excel头
sheet.write(0,0,"股票代码",style)
sheet.write(0,1,"股票名称",style)
sheet.write(0,2,"序号",style)
# print(find[0])
for index,store in enumerate(find):
    arry = store.split(",")
    sheet.write(index+1,2,index+1)
    for col in range(0,2):
        sheet.write(index+1,col,arry[col+1])
wbk.save("store.xls")




