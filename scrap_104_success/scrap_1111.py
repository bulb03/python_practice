#依舊有bug
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

wd = webdriver.Chrome()

url_list = []

job = ["系統分析與設計工程師"]

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
			for j in i.findAll('div',{'class':'jbInfo'}):
				time.sleep(1)	
				for k in j.findAll('div',{'class':'jbInfoin'}):
					time.sleep(1)	
					for l in k.find('h3').findAll('a',limit=5):
						url_list.append("https:"+l.attrs['href'])
	except AttributeError as error:
		print(error)
		pass

	#抓每個工作的需求技能
	for i in url_list:
		skill = " "
		else_skill = " "
		count = 0

		"""		
		with open("test2.csv","a") as a:
			a.write(work)"""

		wd.get(i)
		html = wd.execute_script("return document.documentElement.outerHTML")
		the_page = BeautifulSoup(html,"html.parser")
		try:
			time.sleep(1)
			data = the_page.find('div',{'class':'descriptin'}).find('section',{'id':'incontent'}).find('div',{'id':'c1'}).find('div',{'class':'floatL w65'}).find('article',{'class':'boxsize'}).find('ul',{'class':'dataList'})
			time.sleep(1)
			for i in data.findAll('li'):
				if count < 5:
					count += 1
					continue
				elif count==5:
					time.sleep(1)
					skill = i.find('div',{'class':'listContent'}).get_text()
					skill += "\n"
					count += 1
					print(skill)
				else:
					for j in i.find('div',{'class':'listContent'}).next_sibling.findAll('p'):
						time.sleep(1)
						else_skill += j
					else_skill += "\n"
					print(else_skill)
					count += 1
		except AttributeError as error:
			print(error)
			pass

"""		with open("test2.csv","a") as a:
			a.write(skill)
			a.write(else_skill)
			a.write("--------------------------------\n")"""
