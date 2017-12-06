import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

#使用哪家的伺服器寄信，哪個port
host = "smtp.gmail.com"
port = 587

#要寄信的帳號
username = "gaxen8753@gmail.com"
password = "Jn#__69t?31"

#要收信的帳號
to_username = "gh2752@gmail.com"


# 建立和gmail連線
email_conn = smtplib.SMTP(host,port)  

# 跟server打招呼認證
email_conn.ehlo()				      
	
# 啟動安全傳輸協議	
email_conn.starttls()				  

#強烈建議，try except用打的，不要用複製貼上的，會有不具名錯誤
try:		
	# 登入(失敗，原因就是要認證才能登入的帳號不能用，換一支帳號)
	email_conn.login(username,password)	  

	# 寄信(寄信者、收信者、訊息)
	#email_conn.sendmail(username,to_username,"外面吵死了!")  # 寄信內容不能用中文
	email_conn.sendmail(username,to_username,"Fuck!")

except SMTPAuthenticationError:	# 如果要寄信的帳戶的帳號或密碼錯誤，用此例外接收
	print("can't login")
except:							# 其他錯誤 
	print("an error occured")

#結束該服務
email_conn.quit()

#例外參考區:https://docs.python.org/3.4/library/smtplib.html?highlight=smtplib