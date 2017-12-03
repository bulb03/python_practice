"""
練習讓自訂物件變數具別種變數的型態，以下是讓其擁有list的型態
"""
class Athlete(list):
	def __init__(self,name):
		list.__init__([])
		self.name = name

	def top3(self):
		for i in self:
			print(i)

John = Athlete("John")
John.append(['1','2','3'])
Alos = Athlete("AIos")
Alos.append(['4','5','6'])
John.top3()
Alos.top3()
#在此，John和Alos除了是實作Athlete的物件變數外，他們也是個list型態的變數
