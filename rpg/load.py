#從rpg_parameter這資料夾裡呼叫character.py裡面的class character
from rpg_parameter.character import character  
from rpg_parameter.color import bcolor
from rpg_parameter.skill import skill
from rpg_parameter.action import action
from rpg_parameter.status import status
import datetime
import random
import time

status = status()
#1:burn 2:poison 3:freeze 4:bloody 5:stunned 6:Invincible 7:steelwall 8:healer 9:violent 10:weakness 11:unlimited_mp

fire = skill("Fire",40,0,0,10,[1,10],True)
frozen = skill("Frozen",10,0,0,10,[3,5],True)
thunder = skill("Thunder",100,0,0,20,[4,10],True)
bite = skill("Bite",10,0,0,5,[4,10],True)
punch = skill("Punch",20,0,0,7,[10],True)
quake = skill("Quake",100,0,0,20,[5],True)


now_time = datetime.datetime.now()
scarecrow = character(1,10,0,200,None,[],now_time)
fighter = character(20,5,30,100,[bite,punch,quake],[],now_time)
player = character(30,10,20,150,[fire,frozen,thunder],[],now_time)

color = bcolor()

action = action()
#如果類別沒有先建好變數，會出現：missing 1 required positional argument: 'computer'
#參考網址：https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self

#python的函數可以一次回傳多個值，太方便了吧

def cal_hp_mp(something):
    hp_bar = ""
    mp_bar = ""
    now_hp_bar = (something.hp/something.maxhp) * 100 / 4
    now_mp_bar = (something.mp/something.maxmp) * 100 / 10

    while now_hp_bar > 0:
        hp_bar += "█"
        now_hp_bar -= 1
    while len(hp_bar) < 25:
        hp_bar += " "

    while now_mp_bar > 0:
        mp_bar += "█"
        now_mp_bar -= 1
    while len(mp_bar) < 10:
        mp_bar += " "

    return hp_bar,mp_bar

def cal_hp_mp2(something):
    max_hp = str(something.hp)+"/"+str(something.maxhp)
    current_hp = ""
    count = len(max_hp)
    while count<7:
        current_hp += " "
        count += 1
    current_hp += max_hp

    max_mp = str(something.mp)+"/"+str(something.maxmp)
    current_mp = ""
    count = len(max_mp)
    while count<5:
        current_hp += " "
        count += 1
    current_mp += max_mp
    return current_hp,current_mp

def show_test(player,monster):
    a,b = cal_hp_mp(player)
    c,d = cal_hp_mp(monster)
    e,f = cal_hp_mp2(player)
    g,h = cal_hp_mp2(fighter)
    print("===================================================================================================")
    print(color.Yellow,"Player    HP:",e+color.Green,"|"+a+"|","   MP:",f,color.Blue,"|"+b+"|","Defense:",player.low_defense,color.Reset,color.Red,"\nStatus:"+status.show_status(player),color.Reset)
    print(color.Cyan,"Fighter   HP:",g+color.Cyan,"|"+c+"|","   MP:",h,color.Blue,"|"+d+"|","Defense:",monster.low_defense,color.Reset,color.Red,"\nStatus:"+status.show_status(monster),color.Reset)
    print("===================================================================================================")

running = False
try:
    show_test(player, fighter)
    
    while not running:
        choose = action.show_action(False)
        dmg = action.select_action(choose,False,player)
        now_hp = fighter.toked_attack(int(dmg))
        
        print(color.Red,color.Bold,"Player attack:",dmg,color.Reset)
        
        show_test(player, fighter)

        #時間有確實輸入各自的status_time
        #這function要接收player和fighter物件，我卻傳時間
        status.checktime(player,fighter)

        #我猜是Python是直譯式語言的關係，所以不會跳掉
        running = action.judge(player,fighter,running)

        time.sleep(1)
        
        choose = action.show_action(True)
        dmg1 = action.select_action(choose,True,fighter)
        player.toked_attack(int(dmg1))

        print(color.Red,color.Bold,"Fighter attack:",dmg1,color.Reset)
        
        show_test(player, fighter)

        status.checktime(player,fighter)

        running = action.judge(player,fighter,running)

except KeyboardInterrupt:
    pass


#{}:set []: list
