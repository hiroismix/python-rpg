from character import Character
import random

def battle (kilua,gon,hisoka):

    ##ターン数　表示
    turn = 1

    while (kilua.hp > 0 or gon.hp > 0) and                    hisoka.hp > 0:

        print (f'{turn}ターン目')  
        kilua.show_status()  
        gon.show_status()  
        hisoka.show_status()  
 
        input()  
 
        if kilua.hp > 0:
            print('～キルアのターン～')  
            input()  
            kilua.action(hisoka)  
     
        if hisoka.hp <= 0:  
            print(f'{hisoka.name}を倒した！！')
            break  
    
        if gon.hp > 0 :     
            print('~ゴンのターン～')  
            gon.action(hisoka)  
  
        if hisoka.hp <= 0:
            print(f'{hisoka.name}を倒した！！')  
            break  
        input()  
 
 
        print('～ヒソカのターン～')  
        input()  
        hunters = random.choice([kilua,gon])  
        if kilua.hp == 0:
            hunters = gon
        if gon.hp == 0:
            hunters = kilua
        hisoka.action(hunters)  
 
        if kilua.hp <= 0:
            if not kilua.revive_check:
                kilua.revive()  
   
        if gon.hp <= 0: 
            if not gon.revive_check:
                gon.revive()  
      
        if kilua.hp <= 0 and gon.hp <= 0:  
            print                         ('キルア達は、負けてしまった。。。')
            break  
        print('#################')  
 
        turn += 1