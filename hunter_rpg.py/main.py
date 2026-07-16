from kilua import Kilua
from gon import Gon
from hisoka import Hisoka
from battle import battle
import random
#hp,mp,atk,def
kilua = Kilua('キルア',500,200,150,80)
gon = Gon('ゴン',500,250,150,80)
hisoka = Hisoka('ヒソカ',2500,200,200,80)

battle (kilua,gon,hisoka)