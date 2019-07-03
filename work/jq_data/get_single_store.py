import jqdatasdk
import login

login.login()

#获取单个对象
# data = jqdatasdk.get_security_info("000001.XSHE")
# print(data.name)

# cash = jqdatasdk.get_margincash_stocks()
# print(cash)
locked = jqdatasdk.get_locked_shares(['600218.XSHG'],start_date='2019-04-01', forward_count=500)
print(locked)

df = jqdatasdk.get_index_weights(index_id="000001.XSHG", date="2019-06-28")
print(df)
weight = list(df.weight)
print(weight)


data = jqdatasdk.get_price("600218.XSHG", start_date='2015-01-01', end_date='2015-12-31', frequency='daily', fields=None, skip_paused=False, fq='pre')
print(data)
