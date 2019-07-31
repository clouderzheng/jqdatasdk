import login
import jqdatasdk as jq
import Time_Util
import excel_util
import stock_constants
import xlwt
import datetime
login.login()



# 300146.XSHE
"""获取指定股票历史数据"""
def get_stock_daily_history(security ,end_date , start_date = None,count = None):


    """间隔时间大于0 使用间隔 否则默认使用截止日期"""
    if(count != None):
        return jq.get_price(security, end_date= end_date,  frequency="daily",fq="pre",count=count)
    else:
        return jq.get_price(security, start_date=start_date, end_date=end_date, frequency="daily",fq="pre")

# security = "300146.XSHE"
#
#
# current_date = Time_Util.get_before_date_time(1)
# last_date = Time_Util.get_before_date_time(21)
# #获取 20天数据
# stock_price_info = get_stock_daily_history(security , current_date , count = 20)
# print(stock_price_info)
# average_20_price = stock_price_info['close'].mean()
# average_10_price = stock_price_info['close'][-10:].mean()
# average_5_price = stock_price_info['close'][-5:].mean()
#
# print(round(average_20_price,2))
# print(round(average_10_price,2) )
# print(round(average_5_price,2))

"""获取股票均线数据"""
def get_average_stock_data(security, end_date, start_date, count) :
    """获取历史数据"""
    stock_price_info = get_stock_daily_history(security, end_date, start_date, count)

    """获取最后一天收盘价 未结束就是当日价"""
    last_day_price = round(stock_price_info['close'][-1], 2)
    """获取20日均线值"""
    average_20_price = round(stock_price_info['close'].mean(), 2)
    """获取10日均线值"""
    average_10_price = round(stock_price_info['close'][-10:].mean(), 2)
    """获取5日均线值"""
    average_5_price = round(stock_price_info['close'][-5:].mean(), 2)

    data_result = {}
    data_result['last_day_price'] = last_day_price
    data_result['average_20_price'] = average_20_price
    data_result['average_10_price'] = average_10_price
    data_result['average_5_price'] = average_5_price
    """计算均线基于最后交易日偏差率 负数表示 均线 落下方  正数在上方"""
    data_result['average_20_price_rate'] = round(((average_20_price - last_day_price )/ last_day_price),2)
    data_result['average_10_price_rate'] = round(((average_10_price - last_day_price ) / last_day_price),2)
    data_result['average_5_price_rate'] = round(((average_5_price - last_day_price) / last_day_price),2)

    data_result['flag'] = (data_result['average_5_price_rate'] > 0) & (data_result['average_10_price_rate']  > 0) & ( data_result['average_20_price_rate'] > 0)
    if(data_result['flag']):
        data_result['flag'] = 1
    else:
        data_result['flag'] = 0
    return data_result


path = stock_constants.STOCK_PATH+"jq_store.xls"

current_date = Time_Util.get_before_date_time()


all_stock_data = excel_util.get_excel_data(path)
sheet = all_stock_data.sheets()[0]

workbook = xlwt.Workbook()
write_sheet = workbook.add_sheet("average strategy")

header = ['code','name','last_day_price','average_5_price','average_10_price','average_20_price',\
          'average_5_price_rate','average_10_price_rate','average_20_price_rate' ,'flag']


print("begin --->" +str(datetime.datetime.today()))
"""添加表头"""
for col in range(len(header)):
    write_sheet.write(0,col,header[col])

"""减一跳过表头"""
for row in range(sheet.nrows - 1):
    security = sheet.cell_value(row + 1, 0)
    data_result = get_average_stock_data(security, current_date, None, 20)
    data_result['code'] = sheet.cell_value(row + 1, 0)
    data_result['name'] = sheet.cell_value(row + 1, 1)

    for col in range(len(data_result)):
        write_sheet.write(row + 1, col, data_result[header[col]])
workbook.save(stock_constants.STOCK_PATH+"average_strategy"+".xls")

print("end --->" +str(datetime.datetime.today()))