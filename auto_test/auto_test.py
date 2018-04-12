import xlrd
import time
from xlutils.copy import copy
from selenium import webdriver
from urllib.request import urlopen

#寫入結果至excel
def write_the_fault(excel_be_written,is_success,store_dict,test_title,fail_pass,index):
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
	excel_be_written.save("test.xls")

#登入測試
def login_test():
	try:
		wd = webdriver.Chrome()
		wd.get("http://localhost/membersystem/member.html")

		time.sleep(1)

		account = wd.find_element_by_xpath("/html/body/form/div/input[1]")
		time.sleep(1)
		account.clear
		account.send_keys("admin")

		pwd = wd.find_element_by_xpath("/html/body/form/div/input[2]")
		time.sleep(1)
		pwd.clear
		pwd.send_keys("admin")

		wd.find_element_by_xpath("/html/body/form/div/input[3]").click()
		time.sleep(1)
		return 1

	except Exception as e:
		print(e)
		return 0

	wd.quit()

#登出測試
def logout_test():
	try:
		wd = webdriver.Chrome()
		wd.get("http://localhost/membersystem/member.html")

		time.sleep(1)

		account = wd.find_element_by_xpath("/html/body/form/div/input[1]")
		time.sleep(1)
		account.clear
		account.send_keys("admin")

		pwd = wd.find_element_by_xpath("/html/body/form/div/input[2]")
		time.sleep(1)
		pwd.clear
		pwd.send_keys("admin")

		wd.find_element_by_xpath("/html/body/form/div/input[3]").click()
		time.sleep(1)

		wd.find_element_by_xpath("/html/body/a[3]").click()
		time.sleep(1)
		return 1

	except Exception as e:
		print(e)
		return 0

	wd.quit()

#判斷前置測試是否通過
def whether_pass_pre(pre_test,store_dict):
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
def judge(test_title,i):
	is_success=0
	if test_title[int(i)]=='A-1':
		is_success = login_test()#幹你娘，到底誰說可以不用在函數名稱後加括號
	
		write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))
	
	elif test_title[int(i)]=='B-1':
		is_success = logout_test()
	
		write_the_fault(excel_be_written,is_success,store_dict,test_title[i],"",int(i))

i = 0

store_dict = {
	'A-1':0,
	'B-1':0
}

#測試檔案的名稱
file_name = "test.xls"

#測試功能的sheet名稱
sheet_name = ['login','logout']

#測試名稱
test_title = ['A-1','B-1']

#開啟測試檔案
the_whole_excel = xlrd.open_workbook(file_name)

#寫入測試檔案所需物件
excel_be_written = copy(the_whole_excel)

#開始測試
while i < len(sheet_name):
	#取得欲測試功能的sheet
	row_data = the_whole_excel.sheet_by_name(sheet_name[i])

	#檢查是否有前置測試需做
	if int(row_data.cell(3,0).value):
		#取得前置測試所有名稱
		pre_test_ = row_data.cell_value(8,0)
		#將測試名稱分開存入pre_test這list裡
		pre_test = pre_test_.split(',')
		#檢查是否全部前置測試都成功運作
		pre_test_pass,fail_pass = whether_pass_pre(pre_test,store_dict)
		#判斷前置測試是否都成功
		if pre_test_pass:
			judge(test_title,i)
		else:
			#若有一項前置測試失敗，直接跳過目前的測試，在測試檔案裡寫上失敗
			write_the_fault(excel_be_written,2,store_dict,test_title[i],fail_pass,i)
	else:
		judge(test_title,i)
	i += 1


#======因應xlrd的寫入功能一點屁用都沒有之解法=======
# 故選擇了xlutils
# 此外，副檔名目前只能設成xls，不然寫不進去
#======字串的比較放在if裡的失敗=========
# 以字串是否相同來當作ifelse的條件
# 出現不明失敗
# 反正就是不能
# 所以我在測試檔案裡加了是否有前置測試代碼
# 1就是有 0就是沒有


