from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""def gettitle(url,info):

	#連線，except抓連線錯誤(找不到頁面或連不上主機)
	try:
		a = urlopen(url)
	except HTTPError as e:
		print("belong HTTPError",e)
		print("Can't find the page")
		return None

	#把html抓下來爬我要的資訊(data.div)，except抓找不到該tag
	try:
		data = BeautifulSoup(a,"html.parser")
		a = data.findAll("div",info)
	except AttributeError as e:
		print("belong AttributeError",e)
		return None
	return a

url = "https://www.google.com.tw/"
data = gettitle(url,{"id":"main","class":"content"})
if data==None:
	print("I can't find anything")
else:
	print(data)"""
url = "file:///C:/Users/apple/Desktop/hi.html"
data = urlopen(url)
b = BeautifulSoup(data,"html.parser")
"""c = b.find("a")
print(c.attrs['href'])
"""
"""
print("下一堆:")
for i in b.tr.next_siblings:
    print(i)
print("下一個:",b.tr.next_sibling)
print("上一堆:")
for i in b.tr.previous_siblings:
	print(i)
print("上一個:",b.tr.previous_sibling)
"""
for i in b.findAll(lambda tag:len(tag.attrs)==1):
	print(i)
