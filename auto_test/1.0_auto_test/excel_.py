import xlrd
from xlutils.copy import copy

class excel_():
	def __init__(self, file_name,file_sheet_name,test_title):
		super(excel_, self).__init__()
		self.file_name = file_name
		self.file_sheet_name = file_sheet_name
		self.test_title = test_title

	def open_(self):
		return xlrd.open_workbook(self.file_name)

	def write_(self,the_whole_excel):
		return copy(the_whole_excel)

	#寫入結果至excel
	def write_the_fault(self,excel_be_written,is_success,store_dict,test_title,fail_pass,index):
		excel_be_written_ = excel_be_written.get_sheet(int(index))
		#測試成功
		if is_success==1:
			excel_be_written_.write(6,0,"pass")# 列，行
			excel_be_written_.write(7,0,1)
			store_dict[test_title] = 1
			print("success")
		#測試失敗
		elif is_success==0:
			excel_be_written_.write(6,0,"fail")
			excel_be_written_.write(7,0,0)
			store_dict[test_title] = 0
			print("fail")
		#測試未進行，因有前置測試未成功
		else:
			excel_be_written_.write(6,0,"because "+fail_pass+" doesn't pass, so stop testing this function")
			excel_be_written_.write(7,0,2)
			store_dict[test_title] = 0
			print("pre_test_fail")		

		#存檔
		excel_be_written.save("PlanningandManage.xls")	


#======因應xlrd的寫入功能一點屁用都沒有之解法=======
# 故選擇了xlutils
# 此外，副檔名目前只能設成xls，不然寫不進去