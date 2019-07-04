import jqdatasdk
import login
import excel_util
login.login()

# stock_code = "603568.XSHG"
stock_code = "000300.XSHG"
# data = jqdatasdk.get_security_info(stock_code)

data = jqdatasdk.get_index_weights(index_id="000001.XSHG", date="2019-07-04")
print(data)