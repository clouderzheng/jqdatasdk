import jqdatasdk
import login
import excel_util
from jqdatasdk import  finance
login.login()

#获取限售解禁数据
def get_locked_stock(stock_list, start_date, end_date, forward_count):
    return jqdatasdk.get_locked_shares(stock_list, start_date, end_date, forward_count)

# data = get_locked_stock("603568.XSHG","2019-06-06",None,30)
# print(data)

#受限股份实际解禁日期
def get_limit_stock_unlock(stock_list,pub_date ,limit = 10):
    query = jqdatasdk.query(finance.STK_LIMITED_SHARES_UNLIMIT).filter(finance.STK_LIMITED_SHARES_UNLIMIT.code=='603568.XSHG',finance.STK_LIMITED_SHARES_UNLIMIT.pub_date>pub_date).limit(limit)
    return finance.run_query(query)
stock_name = "603568.XSHG"
# data = get_limit_stock_unlock(stock_name,"2019-01-01")
# excel_util.outprint_excel(data.columns,data,"stock_unlock_"+stock_name)
# 股东股份质押
def get_share_holder_pledge(stock_list,pub_date ,limit = 10):
    query = jqdatasdk.query(finance.STK_SHARES_PLEDGE).filter(finance.STK_SHARES_PLEDGE.code==stock_list,finance.STK_SHARES_PLEDGE.pub_date>pub_date).limit(limit)
    return finance.run_query(query)

data = get_share_holder_pledge(stock_name,"2017-01-01")
excel_util.outprint_excel(data.columns,data,"stock_pledge_"+stock_name)

query = jqdatasdk.query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date>='2019-06-01').limit(10)
df = finance.run_query(query)

print(df.company_name,df.code,df.report_date,df.bonus_type,df.board_plan_pub_date,df.board_plan_bonusnote)

