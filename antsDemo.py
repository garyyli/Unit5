#Gary Li
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import *

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,lineStyle(1,red),red)
    
    Sprite(ant,
