import jqdatasdk
import  login
login.login()

#获取天数据 时间 开盘价 收盘价 最高 最低 成交量 成交额

#日数据
# data = jqdatasdk.get_price("600218.XSHG", start_date='2019-06-06', end_date='2019-07-01', frequency='daily', fields=None, skip_paused=False, fq='pre')
# 分钟数据
# data = jqdatasdk.get_price("600218.XSHG", start_date='2019-07-01 9:00:00', end_date='2019-07-01 15:00:00', frequency='1m', fields=None, skip_paused=False, fq='pre')

# 五档行情
# data = jqdatasdk.get_ticks("600218.XSHG",start_dt="2019-07-01", end_dt="2019-07-01", count=None)

data  = jqdatasdk.get_money_flow("600218.XSHG", start_date="2019-06-06", end_date="2019-07-01", fields=None, count=None)
print(data.columns)
