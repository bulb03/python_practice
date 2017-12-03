#import circle：重複互相引用，例如：color.py import character , character.py import color
#就會發生import circle
from rpg_parameter.character import character
from rpg_parameter.skill import skill
from rpg_parameter.color import bcolor
import random

skill = skill("name", 0, 0, 0, 0, None,False)
bcolor = bcolor()

class action:

	#顯示可使用行動
	def show_action(self,computer):
		if not computer:
			print("1. Attack")
			print("2. Magic Attack")
			print("3. Run")
			try:
				data = input(">>>input:")
				return data
			except KeyboardInterrupt:
				print("Input Error")
		else:
			return random.randrange(1,3)

	#判斷其中一方血量歸零
	def judge(self,other1,other2,running):
		if other1.hp>0 and other2.hp>0:
			running = False
			return running
		else:
			running = True
			return running


	#選擇行動(物理攻擊、技能攻擊、逃跑)
	def select_action(self,data,computer,myself):
		#物理攻擊
		if int(data)==1:
			#玩家
			if not computer:
				#顯示此次攻擊傷害
				print(bcolor.Magenta,bcolor.Bold,"Player used physical attack",bcolor.Reset)
				#呼叫take_attack發動攻擊
				return myself.take_attack(1,None)
			#電腦
			else:
				#顯示此次攻擊傷害
				print(bcolor.Magenta,bcolor.Bold,"Computer used physical attack",bcolor.Reset)
				#呼叫take_attack發動攻擊
				return myself.take_attack(1,None)
		#技能攻擊
		elif int(data)==2:
			#檢查是否有足夠Mp以使用技能
			if skill.whether_use_skill(-1,myself):
				#玩家
				if not computer:
					#顯示可用技能
					skill.show_skill(myself)
					#選擇技能
					choice = 0
					choice = input("select your skill:")
					choice = int(choice)-1	#這樣寫就可以確實地讓int(choice)-1
					#判斷mp是否足以使用該技能
					if skill.whether_use_skill(choice,myself):
						#顯示該技能的傷害
						print(bcolor.Magenta,bcolor.Bold,"Player used skill:",myself.skill[choice].name,bcolor.Reset)
						#呼叫take_attack發動攻擊
						return myself.take_attack(int(data),choice)
					#mp不足，重新選擇技能
					else:
						return self.select_action(2,not computer,myself)
				#電腦
				else:
					#顯示可用技能					
					skill.show_skill(myself)
					#亂數選擇欲使用技能
					choice = random.randrange(1,3)
					#判斷mp是否足以使用該技能
					if skill.whether_use_skill(choice-1,myself):
						#顯示該技能的傷害
						print(bcolor.Magenta,bcolor.Bold,"Computer used skill:",myself.skill[choice-1].name,bcolor.Reset)
						#呼叫take_attack發動攻擊
						return myself.take_attack(int(data),choice-1)
					#mp不足，重新選擇技能						
					else:
						return self.select_action(2,computer,myself)
			#mp不足，重新選擇行動
			else:
				return self.show_action(computer)
		#逃跑
		if int(data)==3:
			print(1)