import login
import jqdatasdk as jq
import Time_Util
login.login()


# 300146.XSHE

def get_stock_daily_history(security , start_date , end_date = None ,count = 0):

    """获取指定股票历史数据"""
    if(count > 0):
        """间隔时间大于0 使用间隔 否则默认使用截止日期"""
        return jq.get_price(security, start_date=start_date,  frequency="daily",fq="pre",count=count)
    else:
        return jq.get_price(security, start_date=start_date, end_date=end_date, frequency="daily",fq="pre")

security = "300146.XSHE"

current_date = Time_Util.get_before_date_time(1)
last_date = Time_Util.get_before_date_time(21)

stock_price_info = get_stock_daily_history(security , last_date , count=20)
print(stock_price_info)
average_20_day = stock_price_info['close'].mean()
print(average_20_day)

