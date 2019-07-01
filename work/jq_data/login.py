import jqdatasdk
# data = jqdatasdk.get_price(security="000001.XSHE",frequency="1m")
# print(__vers?on__)

#
# print(jqdatasdk.get_all_securities())
# print(data)

def login():
    # jqdatasdk.logout()
    jqdatasdk.auth("13350865639", "yun13350865639")

    print(jqdatasdk.__version__)
    print(jqdatasdk.get_query_count())
# jqdatasdk.logout()