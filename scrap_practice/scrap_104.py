#Documents：網頁在server端生成
#XHR：網頁用JS生成
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

"""要攻克的難點：如何抓到轉了好幾頁的網頁原始碼並從中得到我想要的
	要嘛就要wd.get(url)的url是各個職業的單一頁面(但這很智障)
	要嘛就想辦法透過現在的程式碼爬"""

url2 = "https://www.104.com.tw/job/?jobno=33jbd&jobsource=n104bank1"
# 啟動想起動的瀏覽器 #注意：根據你想啟動的瀏覽器，除了webdrive.瀏覽器名()不一樣外，你也要到selenium去下載和欲開啟的瀏覽器相關的檔案
#wd = webdriver.Edge()
wd = webdriver.Firefox()
# 連上想連的網站，跟requests.get的功能一樣
wd.get(url)


#輸入欲查詢職業
time.sleep(1)
#search = input("請輸入欲查詢職稱:")

search = "網頁設計師"
data = wd.find_element_by_xpath("//*[@id='ikeyword']")
url1 = "https://www.104.com.tw/jobs/search/?ro=0&keyword="+data+"&order=7&asc=0&kwop=7&page=1&mode=s&jobsource=n104bank1"


#data.clear()
#data.send_keys(search)

"""
#輸入地區
list = []
wd.find_element_by_xpath("/html/body/div[3]/div[2]/form[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]").click()
i = 1
while i<20:
	list.append(wd.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li["+str(i)+"]").text)
	i += 1

count = 1
for j in list:
	print(str(count)+j)
	count += 1

multi_ = 2
j = 1
while multi_-1:
	count = 1
	list2 = []
	multi_2 = 2
	i =	input(">>>請輸入項目編號(一律複選，不想複選就選一個就好):")
	wd.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li["+str(i)+"]").click()
	time.sleep(3)

	while wd.find_element_by_xpath("//*[@id='e104menu2011_m_i_0_0_"+str(j)+"']") is not None:
		#//*[@id='e104menu2011_m_i_0_0_"+str(j)+"']抓不到
		#這堆是要讓游標停在選擇區域的，因為那區域是mouse moveover的區域，我猜是因為這樣，所以裡面的都抓不到	
		actions =ActionChains(wd)
		val1 = wd.find_element_by_xpath("//*[@id='e104menu2011_m_i_0_0_"+str(j)+"']")
		actions.move_to_element(val1).perform()
		time.sleep(1)
		list2.append(wd.find_element_by_xpath("//*[@id='e104menu2011_m_i_0_0_"+str(j)+"']").text)
		j+=1

	for i in list2:
		print(str(count)+i)
		count += 1

	while multi_2-1:
		i =	input(">>>請輸入項目編號(一律複選，不想複選就選一個就好):")
		wd.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li["+str(i)+"]").click()
		#/html/body/div[5]/div[3]/div/ul/li[1]/a
		multi_2 = input("繼續輸入?1.否 2.是")
	mult_ = input("繼續輸入?1.否 2.是")
"""
"""
#點擊搜尋
time.sleep(1)
search = wd.find_element_by_xpath("/html/body/div[3]/div[2]/form[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/input")
search.click()
"""
"""

#選擇相關性排序、日期、...
time.sleep(1)
select1 = Select(wd.find_element_by_xpath("//*[@id='js-sort']"))

list = []
for i in select1.options:
	list.append(i.text)

print("選擇排序方式")
for i in list:
	print(i)

selection = input(">>>選擇項目(輸入1~8):")
select1.select_by_visible_text(list[int(selection)-1])



#選擇各種福利
time.sleep(1)

list2=[]
i = 1
#將所有標籤抓下來
while i<10:
	arg = "/html/body/main/div[3]/div/div[1]/div[1]/dl[1]/dd/label["+str(i)+"]/span"
	sel = wd.find_element_by_xpath(arg).text
	sel = str(i)+sel
	list2.append((sel))
	i += 1
#印出選擇
print("選擇福利")
for j in list2:
	print(j)

mulit_ = input(">>>1.單選 2.複選):")
#複選
if int(mulit_)-1:
	while int(mulit_)-1:
		selection2 = input(">>>請選擇篩選條件(輸入1~10):")
		wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[1]/dd/label["+str(selection2)+"]").click()
		mulit_ = input("繼續輸入? 1.否 2.是:")
#單選
else:
	selection2 = input(">>>請選擇篩選條件(輸入1~10):")
	wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[1]/dd/label["+str(selection2)+"]").click()

dd的爬蟲，要抓的是label的xpath，例如：
<label>
	<input value="1" type="checkbox">
		<span>年終獎金</span>
		<svg class="icon-clear b-icon--gray b-icon--w12">
			<use xlink:href="#icon-clear"></use>
		</svg>
</label>，而不是抓span或是svg，因為span不能點，svg抓不到，所以只能抓label



list = []
i = 1
while i<5:
	selection = wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[2]/dd/label["+str(i)+"]/span").text
	selection = str(i)+selection
	list.append(selection)
	i += 1	#忘記這個就變無限迴圈

print("選擇日期")
for i in list:
	print(i)

mulit_ = input(">>>1.單選 2.複選:")
if int(mulit_)-1:
	while int(mulit_)-1:
		sel = input(">>>選擇項目(1~5):")
		wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[2]/dd/label["+str(sel)+"]").click()
		mulit_ = input(">>>繼續輸入? 1.否 2.是:")
else:
	sel = input(">>>選擇項目(1~5):")
	wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[2]/dd/label["+str(sel)+"]").click()



choose = input("選擇查詢薪資方式:1.點擊 2.輸入:")
if int(choose) == 1:
	list = []
	i = 1
	while i<4:
		selection = wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[3]/dd/span[1]/label["+str(i)+"]/span").text
		selection = str(i)+selection
		list.append(selection)
		i += 1

	print("選擇薪資")
	for i in list:
		print(i)

	mulit_ = input(">>>1.單選 2.複選:")
	if int(mulit_)-1:
		while int(mulit_)-1:
			sel = input(">>>選擇項目(1~4):")
			wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[3]/dd/span[1]/label["+str(sel)+"]").click()
			mulit_ = input(">>>繼續輸入? 1.否 2.是:")
	else:
		sel = input(">>>選擇項目(1~5):")
		wd.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]/dl[3]/dd/span[1]/label["+str(sel)+"]").click()

	else:
	list3 = []
	select1 = Select(wd.find_element_by_xpath("//*[@id='js-salary-type']"))
	for i in select1.options:
		#原本有加上項目編號，但是根據select_by_visible_text不行，因為原本的項目沒有編號
		print(i.text)
		list3.append(i.text)

	for i in list3:
		print(i)

	choose = input(">>>選擇薪水計算方式:")
	select1.select_by_visible_text(list3[int(choose)-1])

	sal1 = input(">>>輸入底薪")
	low_salary = wd.find_element_by_xpath("//*[@id='js-salary-min']")
	low_salary.clear()
	low_salary.send_keys(int(sal1))

	sal2 = input(">>>輸入高薪(也可不輸入)")
	high_salary = wd.find_element_by_xpath("//*[@id='js-salary-max']")
	high_salary.clear()
	high_salary.send_keys(int(sal2))

	#點擊確認
	wd.find_element_by_xpath("//*[@id='js-salary-send']").click()"""
n = 1
wd.find_element_by_xpath("/html/body/main/div[3]/div/div[4]/div[4]/article["+str(n)+"]/div[1]/h2/a").click()



"""
#這種方法只能爬wd.get(url)裡的url的原始碼
#查到的項目點擊是抓a(超連結)
n = 1
while n<10:
	wd.find_element_by_xpath("/html/body/main/div[3]/div/div[4]/div[4]/article["+str(n)+"]/div[1]/h2/a").click()
	no_renew = BeautifulSoup(wd2.page_source,"html.parser")
	for i in no_renew.select('.grid-left .main .info .content p'):
		time.sleep(1)
		print(i.text)
		break
	time.sleep(1)
	if no_renew.select('.grid-left .main .info .content dl .tool a'):
		for i in no_renew.select('.grid-left .main .info .content dl .tool a'):
			print(i.text)
	else:
		for i in no_renew.select('.grid-left .main .info .content dl .tool'):
			print(i.text)
	print("=========================================================")
	n+=1
	time.sleep(2)
"""

"""no = wd.execute_script("return document.documentElement.outerHTML")
no_renew = BeautifulSoup(no,"html.parser")
print(no_renew.prettify())#根據這印出來的東西，發現我們抓的根本不是個別的頁面，而是首頁
之前可以抓到的原因是：requests.get(url2)的url2是個別的頁面，也就是說，必須要換個方式，不然只能抓到首頁
"""
#/html/body/main/div[3]/div/div[4]/div[4]/article[n]/div[1]/h2/a -> n是第n個找到的項目
