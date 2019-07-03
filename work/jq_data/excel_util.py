import xlwt

#自定义输出excel方法
def outprint_excel(header,data,sheetName):
    #创建excel
    workbook = xlwt.Workbook()
    #创建sheet
    sheet = workbook.add_sheet(sheetName)
    #遍历输出表头
    for col in range(0,len(header)):
        sheet.write(0,col,header[col])
    #遍历输出数据
    for row in range(0,len(data.index)):

        for col in range(0, len(header)):

            sheet.write(row + 1, col, str(data.iloc[row, col]))
    workbook.save(sheetName+".xls")