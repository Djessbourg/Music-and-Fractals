import pygame as pg

def f (x,c):
    return (x**2 + c)

MAX_ITERATION = 100
XMIN, XMAX, YMIN, YMAX = -2, +0.5, -1.25, +1.25
L,H = 500,500
pg.init()
screen = pg.display.set_mode((L,H))

def Mandelbrot(x,y,nbIteration,ModuleMax):
    """Indique si un nombre complexe fait partie de l'ensemble de Mandelbrot ou non
    En entrée : x et y, deux coordonées, nbIteration, le nombre de répétitions de la formule et ModuleMax, le module à ne pas dépasser
    En sortie : un entier, indiquant si le complexe appartient à l'ensemble ou non """
    nombre = x+(y*1j)
    i = 1
    z = nombre
    c = nombre
    appartient = True
    while i <= nbIteration and appartient==True :

        if abs(z)>ModuleMax :
            appartient = False
        z = (z*z)+c
        i += 1

    return int(appartient)

for y in range (0,H):
    for x in range(0,L):
        cx = XMIN + (x/H) * (XMAX - XMIN)
        cy = -1*(YMIN +(y/L) * (YMAX - YMIN))
        C = cx +(cy*1j)
        X = x+(y*1j)
        Xn = 0 + 0*1j
        n = 0
        while abs(Xn)**2 < 4 and n < MAX_ITERATION :
            Xn = f(Xn ,C)
            n = n + 1
        if n == MAX_ITERATION:
            screen.set_at((x, y), (0, 0,0))
        else :
            screen.set_at((x, y), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256))
pg.display.flip()
print("okokok")
loop = True
while loop:
  for event in pg.event.get():
    if event.type == pg.QUIT: # Pour quitter l'application en fermant la fenêtre
      loop = False

pg.quit()
