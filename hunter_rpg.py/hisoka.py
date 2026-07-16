from character import Character
import random

#'ヒソカ'    start
class Hisoka(Character):
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
        self.dokkiri,  
        self.drain,  
        ]  
  
        self.weights =[  
        40,  
        10,  
        25,  
        25,  
        ]  

    def dokkiri(self,target):  
        damage = random.randint(200,300)  
        target.hp -= damage  
        print(f'{self.name}のバンジーガム！！')  
        print(f'{target.name}に{damage}ダメージ！')  
          
    # オーラ吸収  
    def drain(self,target):  
        print(f'''  
    「{self.name}は  
    {target.name}の念を吸い込み始めた！」  
    ''')  
        damage = random.randint(100,150)  
        drain_mp = random.randint(5,25)  
     
        target.hp -= damage  
        target.mp -= drain_mp   
        if target.mp < drain_mp:  
            drain_mp = target.mp  
        
        input()  
     
        print(f'''  
    「{target.name}に  
    {damage}ダメージ！」  
    ''')  
        print(f'''  
    「{self.name}は、  
    {target.name}のオーラを  
    {drain_mp}吸い取った！！」  
    ''')  
        self.mp += drain_mp  
        if self.mp > self.max_mp:  
            self.mp = self.max_mp  
        if target.hp <= 0:  
            print(f'{target.name}は、倒れた！')  

        
            


############################