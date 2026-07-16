import random
class Character:

    def __init__(self,name,hp,mp,power,defence):  
 
        self.name = name  
        self.show_status  
        self.hp = hp  
        self.mp = mp  
        self.max_hp = hp  
        self.max_mp = mp  
        self.power = power  
        self.defence = defence  
        self.charged = False  
        self.freeze = False
        self.dead = False
        self.revive_check = False
        
        
  ##ステータス表示  
    def show_status(self) :  
        print(f'{self.name}')  
        if self.hp < 0:  
            self.hp = 0  
        print(f'HP:{self.hp}/{self.max_hp} MP:{self.mp}/{self.max_mp}')  
        
   #rate keisann   
    @property
    def hp_rate(self):
        return self.hp / self.max_hp
      
    ##通常攻撃  
    def attack (self,target):  
      
        damage = random.randint(  
        self.power - 30,  
        self.power + 20  
        )  
      
        dis_damage = random.randint(  
        target.defence -50,  
        target.defence  
        )  
      
        if dis_damage > damage:  
            dis_damage = damage  
        
        damage -= dis_damage  
        target.hp -= damage  
        print (f'「{self.name}の攻撃！！」')  
        print(f'''  
    「{target.name}  
    に{damage}ダメージ！！」  
    ''')  
        if target.hp <= 0:  
            print(f'{target.name}は、倒れた！''')  
     
    ## 回復  
    def heal(self,target=None):  
        print(f'「{self.name} は、回復魔法を使った！」')  
     
        heal = random.randint(100,250)  
        mp = 30  
        if self.mp < mp:
            print('''
      「しかし、オーラが足りなかった・・・」
      ''')  
            return
            
        self.mp -= mp  
          
        self.hp += heal  
        if self.hp > self.max_hp:  
            self.hp = self.max_hp
        print(f'「{heal}回復した！」')  
     
# 行動不能      
    def nothing(self,target=None):  
        print(f'{self.name}は、身体が言うことをきかない！！')  
        self.freeze = False  
      
#復活  
    def revive(self,target = None):  
        print(f'''  
    「{self.name}を、まばゆい光がつつむ・・・」''')  
    #ステータスリセット  
        self.charged = False  
        self.freeze = False  
     
        input()  
        rev = random.choice([1,2,3,4,5])  
        if rev <= 2:  
            self.hp = self.max_hp //2  
            print (f'''  
        「{self.name}は、よみがえった！！」  
        ''')  
            
        else:  
            print('''
           「しかし、何も起こらなかった」''')  
            print(f'''
        「{self.name}は死んでしまった
        ''')  
            self.revive_check = True
            
    def action(self,target):  
        
        skill = random.choices(  
        self.skills,  
        self.weights  
        )[0] 
        
        if self.name == 'ゴン' and self.charged:
              skill = self.jajanken2
              
        if self.freeze:
              skill = self.nothing
              
      
        skill(target)