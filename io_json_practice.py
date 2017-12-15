import simplejson as json
import os

file_path = "C://Users//apple//Desktop//ages.json"

def write_into(data):
	with open("C://Users//apple//Desktop//test.txt","a+") as textfile:
		age = "ages:",str(data["ages"])
		sex = "sex:",str(data["sex"])
		#textfile.write()一次只能給一個參數
		textfile.write(str(age))
		textfile.write(str(sex))
		textfile.close()

#判斷該路徑的檔案是否存在或是否有資料
if os.path.isfile(file_path) and os.stat(file_path).st_size != 0:

	#將json檔的資料寫入txt檔內
		
	#雖然他多寫r+，但實際結果感覺一樣
	#old_file = open(file_path,"r+")
	old_file = open(file_path)
	
	#json.loads()：從json檔讀資料後，將其從str轉換成dictionary
	#順帶一提，read會回傳str
	#data = json.loads(old_file.read())

	#json.load()：直接從json檔讀資料，因此，可以說他具備read()的功能
	data = json.load(old_file)
	write_into(data)


else:
	#如果json檔不存在，就新增一個，然後幫他寫入資料
	old_file = open(file_path,"w+")

	#資料要寫成這樣，才能存入，但有時還是會出現simplejson.errors.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
	data = {"ages":20,
			"sex":"male"}

	#以json檔的資料格式寫入新創造的json檔
	#json.dumps則是單純將資料轉乘json格式並回傳資料
	old_file.write(json.dumps(data))
	
	#將json檔的資料寫入txt檔內
	
	#雖然他多寫r+，但實際結果感覺一樣
	#old_file = open(file_path,"r+")
	old_file = open(file_path)
	
	#json.loads()：從json檔讀資料後，將其從str轉換成dictionary
	#順帶一提，read會回傳str
	#data = json.loads(old_file.read())

	#json.load()：直接從json檔讀資料，因此，可以說他具備read()的功能
	data = json.load(old_file)
	write_into(data)






	#也是可以用json.dump()的方式
	
	#從json檔讀資料並以json格式傳入
	#data0 = json.loads(old_file.read())

	#目的檔案物件
	#textfile = open("C://Users//apple//Desktop//test.txt","w+")
	
	#json.dump則可以將要輸入的json格式資料寫入目的檔案物件
	#json.dump(data0,textfile)
