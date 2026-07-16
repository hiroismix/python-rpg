from character import Character
import random

#ゴン start
class Gon(Character) :
    def __init__(
        self,
        name,
        hp,
        mp,
        power,
        defence,
        ):
        
        super().__init__(
        name,
        hp,
        mp,
        power,
        defence,
        )
        
        self.skills = [  
    self.attack,  
    self.heal,  
    self.jajanken1,  
    self.burst  
    ]  
        self.weights=[  
         50,  
         10,  
         30,  
         10,  
         ]  

    def jajanken1 (self,target=None):  
        self.charged = True  
        print('''  
さい…しょは……グー……  
     ''')  
        print(f'''  
 {self.name}の身体からオーラがあふれている！  
     ''')  
        return  
       
    def jajanken2 (self,target):  
        damage = random.randint(self.power *2,self.power*3)  
        target.hp -= damage  
        self.charged = False  
        print('じゃんけん…グーー！！！')
        print(f'{target.name}に、{damage}ダメージ！！')
       
    def burst(self,target =None) :  
        print(f'''  
      {self.name}は、制約と誓約を発動した！  
          ''')  
        self.power += 100  
        self.defence += 100  
        self.hp = self.max_hp
        self.mp = 0  
        print (f'''  
      {self.name}は、  
      全てのオーラを戦闘力に変えた！  
      ''')  
       