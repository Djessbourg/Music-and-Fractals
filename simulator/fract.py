import pygame as pg
import pylab as pl
import numpy as np
from dataclasses import dataclass
from typing import Callable # on en a besoin dans la dataclass pour insrire une fonction

@dataclass
class Fract:
        size: list[int]                          # un couple sous la forme [500,500]
        eq : Callable[[complex,complex],complex] # hollomorphisme à deux entrées
        color : str                              # couleurs de la carte d'affichage
        name : str                               # nom de la fractale

class Fract_manager:
    def __init__(self) :
        self.currentfract = "Mandelbrot"
        self.fracts = dict()
        self.frac_register([500,500],lambda z,c : z**2 +c ,"basic","Mandelbrot")

    def frac_register(self, size, eq, color, name):
        self.fracts[name] = Fract(size, eq, color, name)

    def switch_fract(self,name):
        'change la fractale en cours'
        self.currentfract = name

    def eval(self,c,n):
        'évalue un point du plan complexe de la fractale en cours'
        eq = get_eq()
        if n == 0 :
            return 0
        else :
            return eq(eval(c,n-1),c)

    def get_delta(self,point, partie):
        'retourne la différence de partie réelle (real) ou imaginaire (imag)'
        z1 = self.eval(point)
        z2 = self.eval(z1)
        if partie == 'real':
            return(pl.real(z2)-pl.real(z1))
        elif partie == 'imag':
            return(pl.imag(z2)-pl.imag(z1))

#les fonctions get sont de type récupération de données
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

    def get_size(self):
        'renvoie la taille de la fenètre de la fractale en cours'
        return self.get_fract().size
