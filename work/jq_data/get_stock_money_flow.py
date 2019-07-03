import jqdatasdk
import  login
import xlwt
login.login()

#查询指定时间类股票的资金流向
def stock_flow(security_list,beginTime,endTime,count):
    return jqdatasdk.get_money_flow(security_list, start_date=beginTime, end_date=endTime, fields=None, count=count)

data = stock_flow("600218.XSHG","2019-06-06","2019-07-01",None)

workbook = xlwt.Workbook()
sheet  = workbook.add_sheet("capital_flow")

sheet_header = ["日期","股票代码","涨跌幅(%)","主力净额(万)","主力净占比(%)","超大单净额(万)","超大单净占比(%)","大单净额(万)",\
                "大单净占比(%)","中单净额(万)","中单净占比(%)","小单净额(万)","小单净占比(%)"]

heander = data.columns
# 制作表头
for index,val in enumerate(heander):
    sheet.write(0,index,val)
    sheet.write(1, index, sheet_header[index])

for row in range(0,len(data)):
    for col in range(0,len(heander)):
        sheet.write(row +2 ,col,data.iloc[row,col])

workbook.save("capital_flow.xls")