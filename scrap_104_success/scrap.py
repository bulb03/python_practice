"""爬蟲非常需要加上time.sleep，不然，跑太快，還沒抓到想抓的資料就換下一頁了
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time

wd = webdriver.Chrome()

data = ["系統分析與設計工程師","專案經理","韌體工程師","電玩軟體程式工程師","MIS網管人員","MIS工程師","巨量資料分析師","資訊安全工程師","網路安全分析師","網路管理工程師","產品設備維修工程師","資訊及通訊操作技術人員","電腦網路及系統技術人員","網站技術人員","多媒體動畫設計人員","遊戲設計人員","網站多媒體程式開發人員","廣告行銷企劃人員","品牌企劃人員","網路行銷人員"]

j = 0

for no in data:
	url = "https://www.104.com.tw/jobs/search/?ro=0&keyword="+no+"&order=7&asc=0&kwop=7&page=1&mode=s&jobsource=n104bank1"
	wd.get(url)
	html = wd.execute_script("return document.documentElement.outerHTML")
	the_page = BeautifulSoup(html,"html.parser")
	time.sleep(1)
	list = the_page.findAll('a',{'class':'js-job-link'},limit=10)
	print(no)
	count_data = 1
	with open("test.csv", "a") as textfile:
		textfile.write(no)
	#開始抓十個職位
	for i in list:
		skill = " "
		workpage = " "
		url = "https:"+i.attrs['href']
		#urlopen(url)所開出來的網頁，在抓工作內容那行會有問題，因為那個p裡面包著br，因此，用urlopen抓的會只抓到最後一行
		#連上該職位之網頁
		wd.get(url)
		html1 = wd.execute_script("return document.documentElement.outerHTML")
		the_page1 = BeautifulSoup(html1,"html.parser")
		time.sleep(1)
		#印出第幾個
		print(count_data)
		try:
			#工作內容
			workpage=the_page1.find('div',{'class':'grid-left'}).find('main',{'class':'main'}).find('section',{'class':'info'}).find('div',{'class':'content'}).find('p').get_text()
			workpage += "\n"
			print(workpage)
			count = 0
			for i in the_page1.find('div',{'class':'grid-left'}).find('main',{'class':'main'}).section.next_siblings:
				if count==1:
					work_part = i
					break
				else:	
					count += 1
			#需求技能
			time.sleep(1)
			for i in work_part.findAll('dd',{'class':'tool'}):
				for j in i.findAll('a'):
					if j.text.equals("不拘"):
						pass
					else:
						skill += j.text
						skill += " \n"
			for i in work_part.findAll('dd'):
				if count<7:
					count += 1
				else:
					skill += i.text+"\n"
		except AttributeError:
			pass

		#如果出現別的問題，pass掉
		time.sleep(1)
		try:
			with open("test.csv", "a") as textfile:
				input_no = str(count_data) + "\n"
				textfile.write(input_no)
				textfile.write(workpage)
				textfile.write(skill)
				textfile.write("----------------------------------\n")
			count_data += 1
		except:
			pass
	time.sleep(3)
