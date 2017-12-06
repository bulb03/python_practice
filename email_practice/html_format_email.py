#MIME的使用
#MIME是甚麼：MIME消息能包含文本、圖像、音頻、視頻以及其他應用程序專用的數據。
#參考：https://www.how321.com/50849.html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPAuthenticationError,SMTPException

host = "smtp.gmail.com"
port = 587

username = "gaxen8753@gmail.com"
password = "Jn#__69t?31"

to_username = "gh2752@gmail.com"

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()

try:
	email_conn.login(username,password)
	
	#我還是不知道這三小，但根據網路上的講法：可放入alternavtie和mixed，各自有差異
	#the_msg = MIMEMultipart("mixed")
	the_msg = MIMEMultipart("alternavtive")

	#主旨
	the_msg['Subject'] = "Hello there"  
      
	#寄信者
	the_msg["From"] = username

	#收信者
	the_msg["To"] = to_username

	#信息
	the_plain = "This is a test about sending a email with a web page"

	the_html = """
		<h1>Hi</hi>
		<div>
			Hello, this is a test
			<a href='http://www.google.com'>click here</a>
		</div>
	"""

	#定義訊息內容的類型
	part_1 = MIMEText(the_plain,"plain")
	part_2 = MIMEText(the_html,"html")
	
	#將訊息內容放入變數
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	
	email_conn.sendmail(username,to_username,the_msg.as_string())  #the_msg換成part_1或part_2也可以寄
																   #訊息必須是string之類的

except SMTPAuthenticationError:
	print("can't login")
except SMTPException:
	print("an error occured")

email_conn.quit()

#MIME參考：https://docs.python.org/3.6/library/email.mime.html