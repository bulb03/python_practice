"""受到的傷害或治療直接算完(每秒回復量*總時間)，秒數繼續算，直到時間停止，把狀態消除"""
from rpg_parameter.character import character
import datetime
from datetime import timedelta
import random
import time

class status:

	def __init__(self):
		pass

	def __doc__(self):
		'''Set the character's status

		show_status: whether skil has status and show them
		'''

	def show_status(self,something):
		whole = ""
		
		if something.status == None:
			return whole
		else:
			for i in something.status:
				whole += i+" "
			return whole

	def checktime(self,other1,other2):
		now_time = datetime.datetime.now()
		#問題很簡單，就是存進去的就不能計算
		if other1.status_time - now_time == datetime.timedelta(0) or other1.status_time - now_time > datetime.timedelta(0):
			del_status(other1)
		else:
			pass
		if other2.status_time - now_time == datetime.timedelta(0) or other2.status_time - now_time > datetime.timedelta(0):
			del_status(other2)
		else:
			pass

	def del_status(self,something):
		j = 0
		for i in something.status:
			i = ""
			something.status[j] = i
			j += 1

	def set_status(self,status_list,something):
		print(something)
		for i in status_list:
			if i==1:
				self.burn(something)
			if i==2:
				self.poison(something)
			if i==3:
				self.freeze(something)
			if i==4:
				self.bloody(something)
			if i==5:
				self.stunned(something)
			if i==6:
				self.Invincible(something)
			if i==7:
				self.steelwall(something)
			if i==8:
				self.healer(something)
			if i==9:
				self.violent(something)
			if i==10:
				self.weakness(something)
			if i==11:
				self.unlimited_mp(something)

	def burn(self,something):
		#1
		keep_time = 30
		keep_dmg = 1

		something.hp -= keep_time*keep_dmg

		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def poison(self,something):
		#2
		keep_time = 20
		keep_dmg = 1

		something.hp -= keep_time*keep_dmg
		something.low_defense -= keep_time*keep_dmg

		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def freeze(self,something):
		#3
		keep_time = 40
		keep_dmg = 0.5

		something.hp -= keep_time*keep_dmg

		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def bloody(self,something):
		#4
		keep_time = 10
		keep_dmg = 3

		something.hp -= keep_time*keep_dmg

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time	

	def stunned(self,something): 
		#5
		keep_time = 20
		keep_dmg = 0

		something.hp -= keep_time*keep_dmg
		something.mp = 0

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def Invincible(self,something):
		#6
		keep_time = 10
		keep_def = 1000

		something.low_defense = keep_def

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def steelwall(self,i,something):
		#7
		keep_time = 10
		i = 0.5

		something.low_defense += something.low_defense * i
		something.high_defense += something.high_defense * i

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def healer(self,i,something):
		#8
		keep_time = 10
		heal = 5	

		something.hp += keep_time*heal
		if(something.maxhp<something.hp):
			something.hp = something.maxhp

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def violent(self,i,something):
		#9
		keep_time = 10
		i = 5

		something.low_attack = something.low_attack * i
		something.high_attack = something.high_attack * i

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def weakness(self,i,something):
		#10
		keep_time = 10
		i = 5

		something.low_defense -= i
		something.high_defense -= i

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

	def unlimited_mp(self,something):
		#11
		keep_time = 10
		i = 9999

		something.mp = i

		
		now_time = datetime.datetime.now()
		finish_time = now_time+datetime.timedelta(seconds=keep_time)
		return finish_time

#1:burn 2:poison 3:freeze 4:bloody 5:stunned 6:Invincible 7:steelwall 8:healer 9:violent 10:weakness 11:unlimited_mp