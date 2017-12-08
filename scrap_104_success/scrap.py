#依舊有bug
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

wd = webdriver.Chrome()

url_list = []

job = ["系統分析與設計工程師","專案經理","韌體工程師","電玩軟體程式工程師","MIS網管人員","MIS工程師","巨量資料分析師","資訊安全工程師","網路安全分析師","網路管理工程師","產品設備維修工程師","資訊及通訊操作技術人員","電腦網路及系統技術人員","網站技術人員","多媒體動畫設計人員","遊戲設計人員","網站多媒體程式開發人員","廣告行銷企劃人員","品牌企劃人員","網路行銷人員"]

for work in job:

	url = "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks="+work

	wd.get(url)

	html = wd.execute_script("return document.documentElement.outerHTML")

	the_page = BeautifulSoup(html,"html.parser")

	"""重大發現：findAll必須切開寫，不能夠x.findAll(...).findAll(...)
	"""
	time.sleep(1)
	#抓每個職位的十個工作
	data = the_page.findAll('li',{'class':'digest'})
	try:
		for i in data:
			time.sleep(1)
			for j in i.find('div',{'class':'jbInfo'}).find('div',{'class':'jbInfoin'}).find('h3').findAll('a',limit=10):
				url_list.append("https:"+j.attrs['href'])
	except AttributeError as error:
		print(error)
		pass

	#抓每個工作的需求技能
	for i in url_list:
		skill = " "
		else_skill = " "
		count = 0
		count_data = 1

		with open("test2.csv","a") as a:
			a.write(work)

		wd.get(i)
		html = wd.execute_script("return document.documentElement.outerHTML")
		the_page = BeautifulSoup(html,"html.parser")
		try:
			time.sleep(1)
			data = the_page.find('div',{'id':'descriptin'}).find('section',{'id':'incontent'}).find('div',{'id':'c1'}).find('div',{'class':'floatL w65'}).find('article',{'class':'boxsize'}).find('ul',{'class':'dataList'})
			for i in data.findAll('li'):
					if count < 6:
						count += 1
					elif count==6:
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
		try:
			with open("test2.csv","a") as a:
				a.write(str(count_data))
				a.write(skill)
				a.write(else_skill)
				a.write("--------------------------------\n")
		except:
			pass
