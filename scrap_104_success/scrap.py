#依舊有bug
"""抓了20筆資料，明明設定limit=3，且還是沒有東西寫入
我是想說，既然要做文字雲了，那要每個職業都各自一個檔案比較好做文字雲，如此一來，每個職業可以抓更多職缺
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

wd = webdriver.Firefox()

url_list = []

job = ["系統分析與設計工程師","專案經理","韌體工程師","電玩軟體程式工程師","MIS網管人員","MIS工程師","巨量資料分析師","資訊安全工程師","網路安全分析師","網路管理工程師","產品設備維修工程師","資訊及通訊操作技術人員","電腦網路及系統技術人員","網站技術人員","多媒體動畫設計人員","遊戲設計人員","網站多媒體程式開發人員","廣告行銷企劃人員","品牌企劃人員","網路行銷人員"]

#各職業的專屬檔案
file_name = []

def set_file_name(job,file_name):
	count = 0
	for i in job:
		file_name.append("C://Users//apple//Desktop//test//1111//test2_"+str(count)+".txt")

def make_file(file_name,work):
	with open(file_name,"w") as textfile:
		textfile.write(work)

def write_into_file(file_name,count_data,skill,else_skill):
	with open(file_name,"a") as textfile:
		textfile.write(str(count_data))
		textfile.write(skill)
		textfile.write(else_skill)
		textfile.write("-------------------------------------\n")

def show_memory_place(skill,else_skill):
	print(str(id(skill)),str(id(else_skill)))

def get_jobs_url():
	url = "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks="+work

	wd.get(url)

	html = wd.execute_script("return document.documentElement.outerHTML")

	the_page = BeautifulSoup(html,"html.parser")

	time.sleep(1)
	#抓每個職位的十個工作
	data = the_page.findAll('li',{'class':'digest'})
	try:
		for i in data:
			time.sleep(1)
			for j in i.find('div',{'class':'jbInfo'}).find('div',{'class':'jbInfoin'}).find('h3').findAll('a',limit=3):
				url_list.append("https:"+j.attrs['href'])
	except AttributeError as error:
		print(error)
		pass

	return url_list

def get_skill(i):
	skill = " "
	else_skill = " "
	count = 0

	wd.get(i)
	html = wd.execute_script("return document.documentElement.outerHTML")
	the_page = BeautifulSoup(html,"html.parser")
	try:
		time.sleep(1)
		data = the_page.find('div',{'id':'descriptin'}).find('section',{'id':'incontent'}).find('div',{'id':'c1'}).find('div',{'class':'floatL.w65'}).find('article',{'class':'boxsize'}).find('ul',{'class':'dataList'})
		for i in data.findAll('li'):
			if count < 6:
					count += 1
			elif count == 6:
				time.sleep(1)
				skill = i.find('div',{'class':'listContent'}).get_text()
				skill += " \n"
				count += 1
			else:
				for j in i.find('div',{'class':'listContent'}).next_sibling.findAll('p'):
					time.sleep(1)
					else_skill += j.text
					else_skill += " \n"
				count += 1
	except AttributeError as error:
		pass

	print(skill)
	print(else_skill)
	print("-------------------------------------\n")

	return skill,else_skill


	file_name = make_file(job)

set_file_name(job,file_name)

for work in job:

	career_count = 0
		
	count_data = 1

	#取得每個職業url
	url_list = get_jobs_url()

	#抓每個工作的需求技能
	for i in url_list:
		make_file(file_name[career_count],work)

		#取得工作技能
		skill,else_skill=get_skill(i)

		print(skill)
		print(else_skill)
		show_memory_place(skill,else_skill)

		try:
			show_memory_place(skill,else_skill)
			write_into_file(file_name[career_count],count_data,skill,else_skill)
			show_memory_place(skill,else_skill)
		except:
			pass
		count_data += 1
	career_count+=1


#sublime基礎熱鍵：https://blog.shinychang.net/2014/01/09/Sublime%20Text%20%E5%9F%BA%E7%A4%8E%E7%86%B1%E9%8D%B5%E8%A1%A8/


