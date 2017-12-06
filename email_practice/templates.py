import os  #小寫

#讀取欲開啟檔案的路徑
def get_template_path(path):
	#os.path.join：讓讀取的檔案路經符合該作業系統的格式
	#os.getcwd()：讀取現在的檔案的路徑(get current work directory)
	file_path = os.path.join(os.getcwd(), path)

	#若此路徑是錯誤的或不存在，丟出例外，否則，回傳檔案路徑
	if not os.path.isfile(file_path):
		raise Exception("This is not a template path")
	return file_path

#開啟並讀取檔案
def get_template(path):
	#open就是開檔
	#read就是讀檔
	file_path = get_template_path(path)
	return open(file_path).read()  

file_ = 'template/email_message.txt'

print(get_template(file_))

#以現在的檔案為例：os.getcwd()會得到C:\Program Files\Sublime Text 3\email