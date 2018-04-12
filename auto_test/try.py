import xlrd

i = 0

file_name = "test.xls"

sheet_name = ['login','logout']

the_whole_excel = xlrd.open_workbook(file_name)

while i < len(sheet_name):
	row_data = the_whole_excel.sheet_by_name(sheet_name[i])

	print(type(row_data.cell(3,0).value))

	i += 1