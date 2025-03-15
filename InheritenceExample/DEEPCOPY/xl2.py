import xlrd
import xlwt

# Open the existing Excel file
loc = 'demo2.xls'  # Ensure it's an .xls file
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# Extract data from the first row (or change to a different row index if needed)
row_index = 0  # Change this to extract a different row
data = [sheet.cell_value(row_index, col) for col in range(sheet.ncols)]

# Create a new workbook and write data
wb1 = xlwt.Workbook()
sheet1 = wb1.add_sheet('dummy')

for index, value in enumerate(data):
    sheet1.write(0, index, value)

# Save to a new .xls file
wb1.save('output.xls')  # Cannot overwrite an .xlsx file
