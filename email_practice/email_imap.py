import email
import imaplib

username = "寄信帳號"
password = "寄信密碼"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)

all_stuff = mail.list()

mail.select("INBOX")

result,data = mail.uid("search",None,"all")

get_list = data[0].split()

oldest = get_list[0]

result,data2 = mail.uid("fetch",oldest,"(RFC822)")

get_data = data2[0][1].decode("utf-8")

a = email.message_from_string(get_data)

print(a['To'])
