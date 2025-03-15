import xlrd
import xlwt
loc=('demo1.xlsx')
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
data=[sheet.cell_val(1,col) for col in range(sheet.ncols)]
wb1=xlwt.Workbook()
sheet1=wb1.add_sheet('dummy')
for index,value in enumerate(data):
    sheet1.write(0,index,value)
wb1.save(loc)
help(xlwt)
 
