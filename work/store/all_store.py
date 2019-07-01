import requests
import re
import  xlwt
data = requests.get("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery11240621523061976336_1561470880627&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)%7D)&cmd=C._A&st=(ChangePercent)&sr=-1&p=183&ps=4000&_=1561470880665")

# print(data.text)
# data = re.search(r"{(.*)}",data.text,re.M|re.I)
# print(data.group(1))
#数据按照股票分组
result = re.findall(r'\"([^\"]*)\"',data.text)

#创建workbook  即 excel

work = xlwt.Workbook()
#创建sheet
sheet = work.add_sheet("store")

sheet.write(0,0,"股票代码")
sheet.write(0,1,'股票名称')
sheet.write(0,2,"股票编号")

#遍历股票信息保存
for row,val in enumerate(result):
    sheet.write(row+1,2,row+1)
    arry = val.split(",")
    for col in range(2):
        sheet.write(row+1,col,arry[col+1].replace("*ST",""))
work.save("all_store.xls")

