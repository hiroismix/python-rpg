from character import Character
import random

"キルア"   ##################start

class Kilua(Character):
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
        self.narukami,  
        self.kanmuru,  
        ]  
        if self.hp_rate >= 0.7:
            
            self.weights =[  
            50,
            0,   
            0,  
            50,  
             ]
        elif self.hp_rate >= 0.5:
            print('50%')
            self.weights =[
        5,
        35,
        50,
        10,
        ]
        
        elif self.hp_rate>= 0.3:
            print('30%')
            self.weights =[
            0,
            45,
            35,
            20,
            ]
            
        else:
            print('else%')
            self.weights =[
            0,
            50,
            50,
            0,
            ]
    

    def narukami(self,target):  
        damage = 250  
        target.hp -= damage  
        target.freeze = True  
        print('鳴神(ナルカミ)！！')  
        print(f'{target.name} {damage}ダメージ！！')  
          
    def kanmuru(self,target):  
        print(f'{self.name}の、カンムル！！')  
        damage1 = random.randint(50,120)  
        damage2 = random.randint(80,150)  
          
        target.hp -= damage1  
        print(f'''  
{target.name}に  
{damage1}ダメージ！！  
        ''')  
        target.hp -= damage2  
        print (f'''  
{target.name}に  
{damage2}ダメージ！！  
        ''')  

#########################