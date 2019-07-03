import jqdatasdk
import  login

login.login()

def get_locked_stock(stock_list, start_date, end_date, forward_count):
    return jqdatasdk.get_locked_shares(stock_list, start_date, end_date, forward_count)

# data = get_locked_stock("601066.XSHG","2019-06-06",None,30)
# print(data)