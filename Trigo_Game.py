import pygame as py
import random
import os


class Trigo:
    def __init__(self,image,val,index):
        self.image = image
        self.val = val
        self.index = index
    def __len__(self):
        return self.val
    def get_index(self):
        return self.index

WIDE = 150
HIGH = 100
iden1 = py.image.load(os.path.join("Assets/Trigo","1.png"))
iden1 = py.transform.scale(iden1,(WIDE,HIGH))
card1 = Trigo(iden1,1,0)
iden2 = py.image.load(os.path.join("Assets/Trigo","sin^2 + cos^2 = 1.png"))
iden2 = py.transform.scale(iden2,(WIDE,HIGH))
card2 = Trigo(iden2,1,1)
iden3 = py.image.load(os.path.join("Assets/Trigo","sec^2 = tan^2 +1.png"))
iden3 = py.transform.scale(iden3,(WIDE,HIGH))
card3 = Trigo(iden3,2,2)
iden4 = py.image.load(os.path.join("Assets/Trigo","tan^2 +1 = sec^2.png"))
iden4 = py.transform.scale(iden4,(WIDE,HIGH))
card4 = Trigo(iden4,2,3)
iden5 = py.image.load(os.path.join("Assets/Trigo","2sincos = sin(2x).png"))
iden5 = py.transform.scale(iden5,(WIDE,HIGH))
card5 = Trigo(iden5,3,4)
iden6 = py.image.load(os.path.join("Assets/Trigo","sin(2x) = 2sincos.png"))
iden6 = py.transform.scale(iden6,(WIDE,HIGH))
card6 = Trigo(iden6,3,5)
iden7 = py.image.load(os.path.join("Assets/Trigo","cos(pi_x).png"))
iden7 = py.transform.scale(iden7,(WIDE,HIGH))
card7 = Trigo(iden7,4,6)
iden8 = py.image.load(os.path.join("Assets/Trigo","sin(x).png"))
iden8 = py.transform.scale(iden8,(WIDE,HIGH))
card8 = Trigo(iden8,4,7)
iden9 = py.image.load(os.path.join("Assets/Trigo","cos(x) = cos(-x).png"))
iden9 = py.transform.scale(iden9,(WIDE,HIGH))
card9 = Trigo(iden9,5,8)
iden10 = py.image.load(os.path.join("Assets/Trigo","cos(-x) = cos(x).png"))
iden10 = py.transform.scale(iden10,(WIDE,HIGH))
card10 = Trigo(iden10,5,9)
iden11 = py.image.load(os.path.join("Assets/Trigo","trigo iden 5.png"))
iden11 = py.transform.scale(iden11,(WIDE,HIGH))
card11 = Trigo(iden11,6,10)
iden12 = py.image.load(os.path.join("Assets/Trigo","cos(x).cos(y).png"))
iden12 = py.transform.scale(iden12,(WIDE,HIGH))
card12 = Trigo(iden12,6,11)
iden13 = py.image.load(os.path.join("Assets/Trigo","cos(x).sin(y).png"))
iden13 = py.transform.scale(iden13,(WIDE,HIGH))
card13 = Trigo(iden13,7,12)
iden14 = py.image.load(os.path.join("Assets/Trigo","trigo iden 7.png"))
iden14 = py.transform.scale(iden14,(WIDE,HIGH))
card14 = Trigo(iden14,7,13)
iden15 = py.image.load(os.path.join("Assets/Trigo","cos(x)+cos(y).png"))
iden15 = py.transform.scale(iden15,(WIDE,HIGH))
card15 = Trigo(iden15,8,14)
iden16 = py.image.load(os.path.join("Assets/Trigo","trigo iden 2.png"))
iden16 = py.transform.scale(iden16,(WIDE,HIGH))
card16 = Trigo(iden16,8,15)
iden17 = py.image.load(os.path.join("Assets/Trigo","trigo iden 1.png"))
iden17 = py.transform.scale(iden17,(WIDE,HIGH))
card17 = Trigo(iden17,9,16)
iden18 = py.image.load(os.path.join("Assets/Trigo","cos(x)-cos(y).png"))
iden18 = py.transform.scale(iden18,(WIDE,HIGH))
card18 = Trigo(iden18,9,17)
iden19 = py.image.load(os.path.join("Assets/Trigo","sin(-x) = sin(x).png"))
iden19 = py.transform.scale(iden19,(WIDE,HIGH))
card19 = Trigo(iden19,10,18)
iden20 = py.image.load(os.path.join("Assets/Trigo","-sin(x) = sin(-x).png"))
iden20 = py.transform.scale(iden20,(WIDE,HIGH))
card20 = Trigo(iden20,10,19)
iden21 = py.image.load(os.path.join("Assets/Trigo","trigo iden 6.png"))
iden21 = py.transform.scale(iden21,(WIDE,HIGH))
card21 = Trigo(iden21,11,20)
iden22 = py.image.load(os.path.join("Assets/Trigo","sin(x).cos(y).png"))
iden22 = py.transform.scale(iden22,(WIDE,HIGH))
card22 = Trigo(iden22,11,21)
iden23 = py.image.load(os.path.join("Assets/Trigo","sin(x)+sin(y).png"))
iden23 = py.transform.scale(iden23,(WIDE,HIGH))
card23 = Trigo(iden23,12,22)
iden24 = py.image.load(os.path.join("Assets/Trigo","trigo iden 3.png"))
iden24 = py.transform.scale(iden24,(WIDE,HIGH))
card24 = Trigo(iden24,12,23)
iden25 = py.image.load(os.path.join("Assets/Trigo","sinx.siny.png"))
iden25 = py.transform.scale(iden25,(WIDE,HIGH))
card25 = Trigo(iden25,13,24)
iden26 = py.image.load(os.path.join("Assets/Trigo","trigo iden 4.png"))
iden26 = py.transform.scale(iden26,(WIDE,HIGH))
card26 = Trigo(iden26,13,25)

#card_list = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,card21,card22,card23,card24]






