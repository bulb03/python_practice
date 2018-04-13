from excel_ import excel_
from Utils import Utils

i = 0
judgement = "Y"


#儲存測試是否成功(用於檢查前置測試的)
store_dict = {
	'A-1':0,
	'B-1':0,
	'C-1':0
}

#測試檔案的名稱
file_name = "test.xls"

#測試功能的sheet名稱
sheet_name = ['login','logout','register']

#測試名稱
test_title = ['A-1','B-1','C-1']

excel__ = excel_(file_name,sheet_name,test_title)

utils = Utils()

#開啟測試檔案
the_whole_excel = excel__.open_()

#寫入測試檔案所需物件
excel_be_written = excel__.write_(the_whole_excel)

#開始測試
while i < len(sheet_name):
	#取得欲測試功能的sheet
	row_data = the_whole_excel.sheet_by_name(sheet_name[i])

	#檢查是否有前置測試需做
	if int(row_data.cell(3,0).value):
		#取得前置測試所有名稱
		pre_test_ = row_data.cell(8,0).value
		#將測試名稱分開存入pre_test這list裡
		pre_test = pre_test_.split(',')
		#檢查是否全部前置測試都成功運作
		pre_test_pass,fail_pass = utils.whether_pass_pre(pre_test,store_dict)
		#判斷前置測試是否都成功
		if pre_test_pass:
			utils.judge(test_title,i,row_data,excel_be_written,excel__,store_dict)
		else:
			#若有一項前置測試失敗，直接跳過目前的測試，在測試檔案裡寫上失敗
			excel__.write_the_fault(excel_be_written,2,store_dict,test_title[i],fail_pass,i)
	else:
		utils.judge(test_title,i,row_data,excel_be_written,excel__,store_dict)
	i += 1

#======字串的比較放在if裡的失敗=========
# 以字串是否相同來當作ifelse的條件
# 出現不明失敗
# 反正就是不能當作條件
# 所以我在測試檔案裡加了是否有前置測試代碼
# 1就是有 0就是沒有


