import pygame as pg
import numpy as np
from dataclasses import dataclass
from typing import Callable # on en a besoin dans la dataclass pour insrire une fonction

@dataclass
class Fract:
        size: list[int]                          # un couple sous la forme [H,L]
        eq : Callable[[complex,complex],complex] # hollomorphisme à deux entrées
        color : str                              # couleurs de la carte d'affichage
        name : str                               # nom de la fractale
        coord : list[int]                        # positions des extremums du plan sous la form [XMIN,XMAX,YMIN,YMAX]
        julia : int                              # indique le type de fractale ( 0 = type Mandelbrot et  1 = type julia)
        c : complex                              # donne le départ d'un ensemble de julia
        file : bool                              # indique par un booléen si la fratale possède un fichier npy dans le fichier rsc

class Fract_manager:
    def __init__(self) :
        self.currentfract = "zigouigoui"
        self.fracts = dict()
        self.colors = dict()
        #implémentation de fractales
        self.frac_register([500,500],lambda z,c : z**2 +c ,"ew","Mandelbrot",[-2, +0.5, -1.25, +1.25],0,True)
        self.frac_register([500,500],lambda z,c :18*z**4 -36*z**3 -(7/3)* z**2 + c ,"hard red","Bouglé",[-0.25, 0.25, -0.25, +0.25],0,True)
        self.frac_register([500,500], lambda z,c : 19*z**3 + 20*z**5 + c ,"purple", "Nolan", [-0.5, +0.5, -0.5, +0.5],0,True )
        self.frac_register([500,500], lambda z,c : np.cos(z)+np.cos(2*z)*1j- np.cos(3*z)- np.cos(4*z)*1j+c ,"hard blue", "Horgues", [-0.25, +0.25, -0.25, +0.25],0,True )
        #implémentation de couleur
        self.color_register("basic",70,70,70)
        self.color_register("purple",3,1,10)
        self.color_register("ew",16,32,64)
        self.color_register("black",2,3,5)
        self.color_register("light black",3,5,8)
        self.color_register("blue",1,2,21)
        self.color_register("hard blue",1,2,42)
        self.color_register("hard red",42,1,5)

    def frac_register(self, size, eq, color, name, coord,julia, c = complex (0,0) , file = False):
        self.fracts[name] = Fract(size, eq, color, name, coord,julia,c,file)

    def color_register(self,color,r,g,b):
        self.colors[color] = [r,g,b]

    def switch_fract(self,name):
        'change la fractale en cours'
        if self.currentfract != name :
            self.currentfract = name

    def eval(self,c,n):
        'évalue un point du plan complexe de la fractale en cours'
        eq = self.get_eq()
        if n == 0 :
            return 0
        else :
            return eq(eval(c,n-1),c)

    def is_in(self,x,y,MAX_ITERATION = 20, NORME = 4):
        'détermine si un point de coordonées pygame x y est dans la partie convergente de la fractale'
        Julia = self.get_julia()
        eq = self.get_eq()
        C = self.get_coord()
        S = self.get_size()
        c = self.get_c()
        cx = C[0] + (x/S[0]) * (C[1] - C[0])
        cy = -1*(C[2] +(y/S[1]) * (C[3] - C[2]))
        if Julia == 0 :                                            # si la fractale est de type Mandelbrot
            c = complex (cx,cy)
            Xn = complex(0,0)
            n = 0
            while abs(Xn)**2 < NORME and n < MAX_ITERATION :
                Xn = eq(Xn ,c)
                n = n + 1
            if n == MAX_ITERATION:
                return ([True,n])
            else :
                return ([False,n])
        if Julia == 1 :                                            # si la fractale est de type julia
            Xn = complex (cx,cy)                                   # pas la même initialisation que pour une fractale de type Mandelbrot
            n = 0
            while abs(Xn)**2 < NORME and n < MAX_ITERATION :
                Xn = eq(Xn ,c)
                n = n + 1
            if n == MAX_ITERATION:
                return ([True,n])
            else :
                return ([False,n])

#les fonctions get sont de type récupératrice de données

    def get_fract(self):
        'récupère la fractale courante'
        return self.fracts[self.currentfract]

    def get_eq(self):
        'renvoie l équation de la fractale en cours'
        return self.get_fract().eq

    def get_name(self):
        'renvoie le nom de la fractale en cours'
        return self.currentfract

    def get_color(self):
        'renvoie le mode de couleur de la fractale en cours'
        return self.get_fract().color

    def get_rgblist(self):
        return self.colors[self.get_color()]

    def get_size(self):
        'renvoie la taille de la fenètre de la fractale en cours'
        return self.get_fract().size

    def get_coord(self):
        'renvoie les coordonées des extrèmes de la fenètre'
        return self.get_fract().coord

    def get_julia(self):
        'renvoie l entier id de julia'
        return self.get_fract().julia

    def get_c(self):
        'renvoie la valeur de c'
        return self.get_fract().c

# les foncions there renvoient un booléen ( comme une question : "there is/are smtg ?")

    def there_file(self):
        'revoie True (resp false) si un fichier npy de la fracalte existe (resp pas) dans rsc'
        return self.get_fract().file
