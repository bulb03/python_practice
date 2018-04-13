from excel_ import excel_
from test_function import test_function

class Utils:

	def __init__(self):
		super(Utils, self).__init__()
		self.test_function = test_function()

	#判斷前置測試是否通過
	def whether_pass_pre(self,pre_test,store_dict):
		i = 0
		fail_pass_title = ""

		#若前置測試項目在store_dict裡，出現失敗的0的話，就將前置測試項目名稱寫入fail_pass_title
		while i < len(pre_test):
			if store_dict[pre_test[i]]==0:
				fail_pass_title += pre_test[i]+","
				i += 1
			else:
				i += 1
				continue

		#若前置測試皆成功，就回傳1和空的前置測試失敗項目名稱
		if fail_pass_title == "":
			return 1,""
		else:
			return 0,fail_pass_title

	#判斷該用哪個測試函數
	def judge(self,test_title,i,row_data,excel_be_written,excel_,store_dict):
		is_success=0
		if test_title[int(i)]=='A-1':
			is_success = self.test_function.login_test(row_data.cell(9,0).value)#幹你娘，到底誰說可以不用在函數名稱後加括號
		
			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))
		
		elif test_title[int(i)]=='B-1':
			is_success = self.test_function.logout_test()
		
			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))
		
		elif test_title[int(i)]=='C-1':
			is_success = self.test_function.register_test(row_data.cell(9,0).value)
		
			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))	