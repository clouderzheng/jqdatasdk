import jqdatasdk
import login
import xlwt
login.login()

#获取所有股票信息
data = jqdatasdk.get_all_securities(["stock"])
#  display_name   name start_date   end_date   type
stocks = list(data.name)
#股票代码
code_list = data.index

#股票名称
name_list = data.display_name

#股票首字母大写
short_name_list = data.name

#股票上市时间
start_date_list = data.start_date

# 股票结束时间
end_date_list = data.end_date

#创建workbook
workbook = xlwt.Workbook()

sheet = workbook.add_sheet('store')


#创建excel头
sheet.write(0,0,"股票代码")
sheet.write(0,1,"股票名称")
sheet.write(0,2,"股票首字母")
sheet.write(0,3,"股票开始时间")
sheet.write(0,4,"股票结束时间")

for row in range(0,len(code_list)):

    sheet.write(row + 1,0,code_list[row])
    sheet.write(row + 1,1,name_list[row])
    sheet.write(row + 1,2,short_name_list[row])
    sheet.write(row + 1,3,start_date_list[row])
    sheet.write(row + 1,4,end_date_list[row])
workbook.save("jq_store.xls")