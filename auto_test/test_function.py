from selenium import webdriver
from urllib.request import urlopen
import time

class test_function:
	#登入測試
	def login_test(self,data):
		data_ = data.split(';')
		i = 0
		while i<len(data_):
			data__ = data_[i].split(',')
			try:
				wd = webdriver.Chrome()
				wd.get("http://localhost/membersystem/member.html")

				time.sleep(1)

				account = wd.find_element_by_xpath("/html/body/form/div/input[1]")
				time.sleep(1)
				account.clear
				account.send_keys(data__[0])

				pwd = wd.find_element_by_xpath("/html/body/form/div/input[2]")
				time.sleep(1)
				pwd.clear
				pwd.send_keys(data__[1])

				wd.find_element_by_xpath("/html/body/form/div/input[3]").click()
				time.sleep(1)
				return 1

			except Exception as e:
				print(e)
				return 0
			i += 1

		wd.quit()

	#登出測試
	def logout_test(self):
		try:
			wd = webdriver.Chrome()
			wd.get("http://localhost/membersystem/member.html")

			time.sleep(1)

			account = wd.find_element_by_xpath("/html/body/form/div/input[1]")
			time.sleep(1)
			account.clear
			account.send_keys("admin")

			pwd = wd.find_element_by_xpath("/html/body/form/div/input[2]")
			time.sleep(1)
			pwd.clear
			pwd.send_keys("admin")

			wd.find_element_by_xpath("/html/body/form/div/input[3]").click()
			time.sleep(1)

			wd.find_element_by_xpath("/html/body/a[3]").click()
			time.sleep(1)
			return 1

		except Exception as e:
			print(e)
			return 0

		wd.quit()

	#註冊測試
	def register_test(self,data):
		data_ = data.split(';')
		i = 0
		j = 0
		data__ = data_[i].split(',')
		while i<len(data_):
			try:
				wd = webdriver.Chrome()
				wd.get("http://localhost/membersystem/register.html")
				
				time.sleep(1)

				account = wd.find_element_by_xpath("/html/body/form/input[1]")
				time.sleep(1)
				account.clear
				account.send_keys(data__[0])

				pwd = wd.find_element_by_xpath("/html/body/form/input[2]")
				time.sleep(1)
				pwd.clear
				pwd.send_keys(data__[1])

				wd.find_element_by_id(data__[2]).click()
				time.sleep(1)

				wd.find_element_by_xpath("/html/body/form/input[5]").send_keys(data__[3])
				time.sleep(1)

				checkbox_data = (data__[4].lstrip("(")).split(",")
				while j<len(checkbox_data):			
					wd.find_element_by_id(checkbox_data[j]).click()
					time.sleep(1)
					j += 1

				wd.find_element_by_xpath("/html/body/form/input[9]").click()
				time.sleep(1)
				return 1

			except Exception as e:
				print(e)
				return 0

		wd.quit()