import pygame as pg
import numpy as np

import fract
import sound
import inputs

class Motor :
    def __init__ (self):
        self.f = fract.Fract_manager()
        self.size = self.f.get_size()
        self.color = self.f.get_color()
        self.screen = pg.display.set_mode(self.size) # taille de la fenêtre
        pg.display.set_caption("Sound of Fractals")

    def quit_motor(self):
        """Ferme le simulateur"""
        pg.quit()

    def draw_fract(self,Coords=[],zoom = 0):
        'affiche sur l écran pygame la fractale en mémoire'             
        f = self.f
        size = self.size
        screen = self.screen
        window = pg.display.set_mode(size)
        screen.blit(window,(0,0))
        nmax = 100
        rgb = f.get_rgblist()
        if not(f.there_file()) :                                              # si la fractale n'est pas prénregistrée, on fait tous les calculs
            for y in range (size[0]):
                for x in range (size[1]):
                    L = f.is_in(x,y,Coords,zoom)
                    if L[0] == True :
                        window.set_at((x, y), (0, 0,0))
                    if not(L[0]) == True :
                        window.set_at((x, y), ((rgb[0] * L[1]) % 256, (rgb[1] * L[1]) % 256, (rgb[2]* L[1]) % 256)) #TO DO: créer différents modes de colorisation
        elif f.there_file() :
            name = f.get_name()                               # si elle possède un préenregistrment alors on lit la matrice ( pas de calculs)
            M = np.load() #TODO: retrouver la documentation pour acceder aux fichier
            for y in range (size[0]):
                for x in range (size[1]):
                    n = M[x][y]
                    if n == nmax :
                        window.set_at((x, y), (0, 0,0))
                    else:
                        window.set_at((x, y), ((rgb[0] * n) % 256, (rgb[1] * n) % 256, (rgb[2]* n) % 256)) #TO DO: créer différents modes de colorisation

    def change_fract(self,name):
        self.f.switch_fract(name)
        self.draw_fract()
        pg.display.flip()

    def move_fract(self,dir,k=0.1,kz=0.4):
        Coords = self.f.get_coord()
        zoom = 0
        dx = Coords[1]-Coords[0]
        dy = Coords[3]-Coords[2]
        if dir == 'up':
            Coords[2],Coords[3] = Coords[2]+k*dy,Coords[3]+k*dy
            self.draw_fract(Coords,zoom)
            pg.display.flip()
        elif dir == 'down':
            Coords[2],Coords[3] = Coords[2]-k*dy,Coords[3]-k*dy
            self.draw_fract(Coords,zoom)
            pg.display.flip()
        elif dir == 'left':
            Coords[0],Coords[1] = Coords[0]-k*dx,Coords[1]-k*dx
            self.draw_fract(Coords,zoom)
            pg.display.flip()
        elif dir == 'right':
            Coords[0],Coords[1] = Coords[0]+k*dx,Coords[1]+k*dx
            self.draw_fract(Coords,zoom)
            pg.display.flip()
        elif dir == 'forward':
            Coords[0],Coords[1] = Coords[0]+kz*dx,Coords[1]-kz*dx
            Coords[2],Coords[3] = Coords[2]+kz*dy,Coords[3]-kz*dy
            if zoom == 0 :
                zoom = 2
            elif zoom == -2:
                zoom = 0
            else :
                zoom = 2*zoom
            self.draw_fract(Coords,zoom)
            pg.display.flip()
        elif dir == 'backward':
            Coords[0],Coords[1] = Coords[0]-kz*dx,Coords[1]+kz*dx
            Coords[2],Coords[3] = Coords[2]-kz*dy,Coords[3]+kz*dy
            if zoom == 0:
                zoom = -2
            elif zoom == 2:
                zoom = 0
            else :
                zoom = zoom/2
            self.draw_fract(Coords,zoom)
            pg.display.flip()

    def delta(self,begining,point ):
        'prend en entrée un point du plan complexe et un point d origine correspondant à la consante c pour renvoyer une différence de partie réelle et imaginaire sour forme de liste'
        eq = self.f.get_eq()
        y = eq(point,begining)
        return [point.real - y.real , point.imag - y.imag]

    def run(self):
        """Boucle principale"""
        self.draw_fract()
        pg.display.flip()
        print("c'est affiché")
        self.is_running = True

        while self.is_running:
            # Gestion des évènements
            for event in pg.event.get():
                if event.type == pg.QUIT: # Ferme le jeu
                    self.is_running = False
                elif event.type == pg.KEYDOWN :
                    inputs.handle_key_down_event(self, event)
                    ## TODO: envoyer les coordonées dans une fonction sonore

        self.quit_motor() # Fermeture du jeu
