import xlrd

path = input("请输入excel文件路径:")
workbook = xlrd.open_workbook(path)#打开.xlsx文件
sheet = workbook.sheet_by_index(0)#拿到表格1，sheet1的表
for row in range(sheet.nrows):
    print()
    for col in range(sheet.ncols):
        print("%7s" % sheet.row(row)[col].value, '\t', end='')#遍历输出
        #print("%7s" % sheet.col(col)[row].value, '\t', end = '')
        #print("%7s" % sheet.cell(row, col).value, '\t', end = '')
        
