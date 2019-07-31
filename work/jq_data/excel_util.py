import xlwt
import xlrd
import stock_constants
#自定义输出excel方法
def outprint_excel(header,data,sheetName):
    #创建excel
    workbook = xlwt.Workbook()

    index = data.index
    #创建sheet
    sheet = workbook.add_sheet(sheetName)

    # 输出索引
    sheet.write(0,0,"index")

    #遍历输出表头
    for col in range(0,len(header)):
        sheet.write(0,col + 1,header[col])
    #遍历输出数据
    for row in range(0,len(data.index)):
        sheet.write(row + 1, 0, str(index[row]))
        for col in range(0, len(header)):
            sheet.write(row + 1, col + 1, str(data.iloc[row, col]))
    workbook.save(stock_constants.STOCK_PATH+sheetName+".xls")

"""读取excel数据 原样返回"""
def get_excel_data(path):
    data = xlrd.open_workbook(path)
    return data
# data = get_excel_data("jq_store.xls")
# sheet = data.sheets()[0]
# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.cell(1,1))