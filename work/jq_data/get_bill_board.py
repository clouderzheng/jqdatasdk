import jqdatasdk
import login
import excel_util
login.login()
data = jqdatasdk.get_billboard_list("603568.XSHG",start_date ="2019-06-25", end_date = "2019-07-04", count = None)
print(data)
# print(data.iloc[1,1])
excel_util.outprint_excel(data.columns,data,"bill_board_603568")