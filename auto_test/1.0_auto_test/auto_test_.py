from excel_ import excel_
from Utils import Utils

i = 0

#儲存測試是否成功(用於檢查前置測試的)
store_dict = {
	'A-1-1':0,
	'B-1-1':0,
	'C-1-1':0,
	'D-1-1':0,
	'E-1-1':0,
	'C-1-2':0,
	'D-1-2':0,
	'E-1-2':0,
	'C-1-3':0,
	'D-1-3':0,
	'E-1-3':0
}

#測試檔案的名稱
file_name = "PlanningandManage.xls"

#測試功能的sheet名稱
sheet_name = ['login-regionalcenter','logout-regionalcenter','meetinglist_rev-regionalcenter','meetinglist_add-regionalcenter','meetinglist_del-regionalcenter','edulecture_rev-regionalcenter','edulecture_add-regionalcenter','edulecture_del-regionalcenter','visit_rec_rev-regionalcenter','visit_rec_add-regionalcenter','visit_rec_del-regionalcenter']
# sheet_name = ['edulecture_rev-regionalcenter','edulecture_add-regionalcenter','edulecture_del-regionalcenter']

#測試名稱
test_title = ['A-1-1','B-1-1','C-1-1','D-1-1','E-1-1','C-1-2','D-1-2','E-1-2','C-1-3','D-1-3','E-1-3']
# test_title = ['C-1-2','D-1-2','E-1-2']

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
			utils.record_num_of_fault(2)

			utils.record_title['pre_test_fail'] += test_title[i]+","

			#若有一項前置測試失敗，直接跳過目前的測試，在測試檔案裡寫上失敗
			excel__.write_the_fault(excel_be_written,2,store_dict,test_title[i],fail_pass,i)
	else:
		utils.judge(test_title,i,row_data,excel_be_written,excel__,store_dict)
	i += 1

print("success:"+str(utils.record['success'])+" fail:"+str(utils.record['fail'])+" pre_test_fail:"+str(utils.record['pre_test_fail']))

print("success:"+str(utils.record_title['success'])+" fail:"+str(utils.record_title['fail'])+" pre_test_fail:"+str(utils.record_title['pre_test_fail']))

#======字串的比較放在if裡的失敗=========
# 以字串是否相同來當作ifelse的條件
# 出現不明失敗
# 反正就是不能當作條件
# 所以我在測試檔案裡加了是否有前置測試代碼
# 1就是有 0就是沒有


