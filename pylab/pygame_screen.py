import pygame as pg
import random as rd

h,l = 500 , 500
pg.init()
screen = pg.display.set_mode((h,l))

for i in range (h):
    for j in range (l):
        r= i % 256
        g= j % 256
        b= (i**j) % 256
        screen.set_at((i,j),(r,g,b))
pg.display.flip()

loop = True
while loop:
  for event in pg.event.get():
    if event.type == pg.QUIT: # Pour quitter l'application en fermant la fenêtre
      loop = False

pg.quit()
