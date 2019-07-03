import jqdatasdk
import login
import excel_util
login.login()
data = jqdatasdk.get_billboard_list(stock_list=None, end_date = '2019-07-02', count = 1)
print(data)
# print(data.iloc[1,1])
excel_util.outprint_excel(data.columns,data,"bill_board")