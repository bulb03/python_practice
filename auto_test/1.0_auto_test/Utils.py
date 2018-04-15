from excel_ import excel_
from test_function import test_function

class Utils:

	def __init__(self):
		record={
			'success':0,
			'fail':0,
			'pre_test_fail':0
		}
		record_title={
			'success':"",
			'fail':"",
			'pre_test_fail':""
		}
		super(Utils, self).__init__()
		self.test_function = test_function()
		self.record = record
		self.record_title = record_title

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

	def record_num_of_fault(self,is_success,data):
		if is_success==1:
			self.record['success'] += 1
			self.record_title['success'] += data+","
		elif is_success==2:
			self.record['pre_test_fail'] += 1
			self.record_title['pre_test_fail'] += data+","
		else:
			self.record['fail'] += 1
			self.record_title['fail'] += data+","

	#判斷該用哪個測試函數
	def judge(self,test_title,i,row_data,excel_be_written,excel_,store_dict):
		is_success=0
		
		if test_title[int(i)]=='A-1-1':
			is_success = self.test_function.login_regionalcenter_test(row_data.cell(9,0).value)

			self.record_num_of_fault(is_success,test_title[int(i)])
		
			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))	

		elif test_title[int(i)]=='B-1-1':
			is_success = self.test_function.logout_regionalcenter_test()
		
			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))				

		elif test_title[int(i)]=='C-1-1':
			is_success = self.test_function.meetinglist_rev_regionalcenter_test(row_data.cell(9,0).value)
		
			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='D-1-1':
			is_success = self.test_function.meetinglist_add_regionalcenter_test(row_data.cell(9,0).value)

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='E-1-1':
			is_success = self.test_function.meetinglist_del_regionalcenter_test()

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))			

		elif test_title[int(i)]=='C-1-2':
			is_success = self.test_function.edulecture_rev_regionalcenter_test(row_data.cell(9,0).value)

			self.record_num_of_fault(is_success,test_title[int(i)])
		
			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='D-1-2':
			is_success = self.test_function.edulecture_add_regionalcenter_test(row_data.cell(9,0).value)

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='E-1-2':
			is_success = self.test_function.edulecture_del_regionalcenter_test()

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='C-1-3':
			is_success = self.test_function.visit_rec_rev_regionalcenter_test(row_data.cell(9,0).value)
		
			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='D-1-3':
			is_success = self.test_function.visit_rec_add_regionalcenter_test(row_data.cell(9,0).value)

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

		elif test_title[int(i)]=='E-1-3':
			is_success = self.test_function.visit_rec_del_regionalcenter_test()

			self.record_num_of_fault(is_success,test_title[int(i)])

			excel_.write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))