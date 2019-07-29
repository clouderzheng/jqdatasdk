import login
import jqdatasdk as jq
import excel_util
login.login()


# 300146.XSHE

def get_stock_daily_history(security , start_date, end_date, frequency):

    """获取指定股票历史数据"""
    return jq.get_price(security, start_date=start_date, end_date=end_date, frequency=frequency,fq="pre")

security = "300146.XSHE"

start_date = "2010-12-01"
end_date = "2011-01-31"
frequency = "daily"

stock_list = get_stock_daily_history(security , start_date, end_date, frequency)

print(stock_list)
print(stock_list.index[0])

excel_util.outprint_excel(stock_list.columns,stock_list,"300146-history")
