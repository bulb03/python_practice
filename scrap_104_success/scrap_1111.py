#依舊有bug
"""抓了20筆資料，明明設定limit=3，且還是沒有東西寫入
我是想說，既然要做文字雲了，那要每個職業都各自一個檔案比較好做文字雲，如此一來，每個職業可以抓更多職缺
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

wd = webdriver.Edge()

job = ["系統分析與設計工程師"]#,"專案經理","韌體工程師","電玩軟體程式工程師","MIS網管人員","MIS工程師","巨量資料分析師","資訊安全工程師","網路安全分析師","網路管理工程師","產品設備維修工程師","資訊及通訊操作技術人員","電腦網路及系統技術人員","網站技術人員","多媒體動畫設計人員","遊戲設計人員","網站多媒體程式開發人員","廣告行銷企劃人員","品牌企劃人員","網路行銷人員"]

#各職業的專屬檔案
file_name = []

#顯示skill和else_skill的記憶體位址
def show_memory_place(skill,else_skill):
	print(str(id(skill)),str(id(else_skill)))
	pass


#先建立好檔案名稱
def set_file_name(job,file_name):
	count = 0
	for i in job:
		file_name.append("C://Users//apple//Desktop//test//1111//test2_"+str(count)+".txt")
		count += 1
	return file_name

#將職稱寫進它專屬的檔案
def make_file(file_name,work):
	with open(file_name,"a+") as textfile:
		work_ = str(work)+"\n"
		textfile.write(work)

#爬下來的資料寫進檔案
"""def write_into_file(file_name,count_data,skill_,else_skill_):
	print(str(id(skill_)),str(skill_))
	print(str(id(else_skill_)),str(else_skill_))
	print("--------------\n")
	with open(file_name,"a+") as textfile:
		skill="skill:",str(skill_)
		else_skill="else_skill:",str(else_skill_)
		no = str(str(count_data)),"\n"
		textfile.write(no)
		textfile.write(skill_)
		textfile.write(else_skill_)
		textfile.write("-------------------------------------\n")"""

#取得各職稱底下的職缺URL
def get_jobs_url(work):
	url_list = []

	url = "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks="+work

	wd.get(url)

	html = wd.execute_script("return document.documentElement.outerHTML")

	the_page = BeautifulSoup(html,"html.parser")

	time.sleep(1)
	#抓每個職位的十個工作
	data = the_page.find('div',{'id':'jbwrap'}).find('section',{'id':'content'}).find('article',{'id':'jbList'}).find('ul',{'class':'halfbox'}).findAll('li',{'class':'digest'},limit=5)
	try:
		for i in data:
			target_url = i.find('div',{'class':'jbInfo'}).find('div',{'class':'jbInfoin'}).find('h3').find('a')
			url_list.append("https:"+target_url.attrs['href'])
	except AttributeError as error:
		print(error)
		pass
	#print("length of url_list:",str(len(url_list)))
	return url_list

#取得職缺的所需技能
def get_skill(i):
	skill = " "
	else_skill = " "
	count = 0

	wd.get(i)
	html = wd.execute_script("return document.documentElement.outerHTML")
	the_page = BeautifulSoup(html,"html.parser")
	try:
		time.sleep(1)
		data = the_page.find('div',{'id':'descriptin'}).find('section',{'id':'incontent'}).find('div',{'id':'c1'}).find('div',{'class':'floatL w65'}).find('article',{'class':'boxsize'}).find('ul',{'class':'dataList'})
		data_ = data.findAll('li')

		if len(data_)==7:
			#<p>抓不到
			#print(data_[6])
			skill = data_[5].find('div',{'class':'listContent'}).get_text()
			time.sleep(1)
			skill += " \n"
			#ㄟ，姓顏的，你真的很可憐，蠢到沒藥醫，他媽<div class="listContent">的是一個<li>裡面只有一個而已，你原本是在next_sibling三小?			
			else_skill = data_[6].find('div',{'class':'listContent'}).get_text()
			else_skill += " \n"
		elif len(data_)==5:
			time.sleep(1)
			#<p>抓不到
			skill = data_[4].find('div',{'class':'listContent'}).get_text()
			skill += " \n"
		else:
			pass
	except AttributeError as error:
		pass

	return skill,else_skill

#取得檔案名稱
file_name = set_file_name(job,file_name)

career_count = 0

for work in job:
	count_data = 1

	#建立檔案
	make_file(file_name[career_count],work)

	#取得每個職業url
	url_list = get_jobs_url(work)

	#抓每個工作的需求技能
	for i in url_list:
		#取得工作技能
		skill,else_skill=get_skill(i)
		time.sleep(1)
		try:
			print(file_name[career_count])
			print(str(id(skill)),str(skill))
			print(str(id(else_skill)),str(else_skill))
			print("--------------\n")
			#python的write()，會將資料先寫在硬碟的緩存區中，等到時間到了或緩存區滿了，才會把資料寫入檔案內
			with open(file_name[career_count],"a+") as textfile:
				skill_="skill: "+str(skill)+"\n"
				else_skill_="else_skill: "+str(else_skill)+"\n"
				no = str(count_data)+"\n"
				textfile.write(no)
				textfile.write(skill_)
				textfile.write(else_skill_)
				#這行就是用來強制將緩存區內容寫入檔案內
				textfile.flush()
				textfile.write("-------------------------------------\n")
		except:
			pass
		count_data += 1
		
	career_count+=1
