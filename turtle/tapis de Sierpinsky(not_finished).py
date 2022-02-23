### tapis de Sierpinsky ###
import turtle as tr
class carre ():
    def __init__(self,x,y,c) :
        self.x = x
        self.y = y
        self.c = c
    
    def create (self):
        tr.up()
        tr.goto(self.x,self.y)
        tr.down()
        for i in range (4):
            tr.forward(self.c)
            tr.left(90)

C1 = carre(0,0,50)
carre.create(C1)


def tapis_1(l):
    C0 = carre(0,0,l)
    carre.create(C0)
    for i in range (0,3):
        for j in range (0,3):
          carre.create(carre(i*l/3,j*l/3,l/3))
