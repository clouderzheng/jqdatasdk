import xlrd
import re
work = xlrd.open_workbook("all_store.xls")
sheets = work.sheets()
sign = ""
for sheet in sheets:
    print(sheet.name)
    rows = sheet.nrows
    cols = sheet.ncols
    for row in range(1,rows):
        # print(sheet.row_values(row))
        # print()
        sign = sign +sheet.cell(row,0).value+"|"
print(sign)

temp = "300362|002667|300105|002591|300536|600988|300414|603863|600639|300029|002939|603738|002237|600547|601038|300460"

param = "300105  600918  002939  1112d fsffs 222  600547"
result = re.findall(temp,param)
print(len(param))
print(result)
print(len(result))