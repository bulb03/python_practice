from rpg_parameter.status import status
from rpg_parameter.character import character

class skill:

	status = status()

	def __init__(self,name,dmg1,dmg2,dmg3,cost,status,has_status):
		self.name = name
		self.dmg1 = dmg1
		self.dmg2 = dmg2
		self.dmg3 = dmg3
		self.cost = cost
		self.status = status
		self.has_status = has_status

	def show_skill(self,something):
		count = 1
		for i in something.skill:
			print("Skill"+str(count)+":",i.name,"damage:",i.dmg1,"cost:",i.cost)
			count+=1

	def whether_use_skill(self,no,something):
		if no==-1:
			if something.mp==0:
				print("You can't use skill")
				return False
			else:
				return True
		else:
			if something.mp<something.skill[no].cost:
				print("Not enough mp")
				return False
			else:
				if something.skill[no].has_status:
					"""現在想法是乾脆status做一個儲存物件的函數，要輸入的時候再呼叫那個函數就好，但是，問題就在於我要在哪裡把物件傳入函數裡
					用建構元也不知道是哪個status的物件變數儲存player和fighter(也不只有load.py要用到status變數，skill.py也要)"""
					something.status_time = status.set_status(something.skill[no].status,something)
					#status.test(a)#這也不行，不過something是從action傳來的，action的又是從load傳來的，不曉得是不是因為不能傳太遠?
					#跟java的問題一樣
					"""可是，我剛才自己做測試，透過建立了另外的三個class(桌面的a資料夾)，由
					執行 test1.py開始，最後有成功把物件傳入status.py(資料夾a裡的)
					"""
					return True
				else:
					return True

"""原先whether_use_skill最一開始判斷有沒有mp是寫if no==-1 and something.mp==0
	但是我發現這樣寫會造成它再判斷一次，因為是no==-1 和 something.mp==0，只要其中一個不合
	就會以n==-1跳到下面的else: if something.mp<something.skill[no].cost
	它會以something.mp < something.skill[-1].cost來運算，就會出現錯誤"""