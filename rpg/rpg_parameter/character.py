#如果前一個函數沒放內容也會出現expected an indented block
"""
EX：
def a():

def b():
	...
    
File "C:\Program Files\Sublime Text 3\rpg\rpg_parameter\character.py", 	
	def b()::
      ^
IndentationError: expected an indented block
"""
#函數裡沒加上self會有問題
#參考網址：https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given

import random

class character:

	def __init__(self,attack,defense,mp,hp,skill,status,status_time):
		self.low_attack = attack
		self.high_attack = attack
		self.low_defense = defense
		self.high_defense = defense
		self.mp = mp
		self.maxmp = mp
		self.hp = hp
		self.maxhp = hp
		self.skill = skill		#list
		self.status = status	#list
		self.status_time = status_time

	def take_attack(self,choice,select):
		if choice == 1:
			return self.low_attack
		else:
			self.mp = self.mp-self.skill[select].cost
			return self.skill[select].dmg1

	def toked_attack(self,dmg):
		if dmg<self.low_defense:
			self.hp = self.hp
		else:
			if (self.hp-(dmg-self.low_defense))<0:
				self.hp = 0
			else:
				self.hp = self.hp-(dmg-self.low_defense)  #每次戰鬥後生命值都會減去，所以要重設生命值

