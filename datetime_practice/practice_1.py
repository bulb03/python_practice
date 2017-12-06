import datetime

now_time = datetime.datetime.now()
later_time = now_time+datetime.timedelta(seconds=30)
#later_time = now_time+30 錯誤，要用上面的方式

#以下這兩種if都可以用
#if(now_time - later_time != 0):
if(later_time - now_time != datetime.timedelta(seconds=0)):
	print("now_time:",now_time)
	print("later_time:",later_time)
  
	#如果寫if(now_time - later_time != datetime.timedelta(seconds=0))，結果變成now_time比later_time還晚
	"""now_time: 2017-11-27 21:02:38.522503
		later_time: 2017-11-27 21:03:08.522503
	"""
  
	#如果寫if(later_time - now_time != datetime.timedelta(seconds=0))，結果就是later_time比now_time還晚

	"""now_time: 2017-11-27 21:05:50.383122
		later_time: 2017-11-27 21:06:20.383122
	"""

else:
	print("now_time:",now_time)
	print("later_time:",later_time)
  
#存進去的時間，不能夠直接加減計算
#時間不支援>和<，只支援==和!=
