import pygame as pg
import fract
import sound

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

    def draw_fract(self):
        'affiche sur l écran pygame la fractale en mémoire'                   # trouver une manière de conserver les données de la fractale de manière à optimiser le temps de calcul
        f = self.f
        size = self.size
        screen = self.screen
        window = pg.display.set_mode(size)
        screen.blit(window,(0,0))
        "color = self.color"
        for y in range (size[0]):
            for x in range (size[1]):
                L = f.is_in(x,y)
                if L[0] == True :
                    window.set_at((x, y), (0, 0,0))
                if not(L[0]) == True :
                    window.set_at((x, y), ((3 * L[1]) % 256, (1 * L[1]) % 256, (10* L[1]) % 256)) #TO DO: créer différents modes de colorisation
                pg.display.flip()

    def run(self):
        """Boucle principale"""
        self.draw_fract()
        self.is_running = True

        while self.is_running:
            # Gestion des évènements
            for event in pg.event.get():
                if event.type == pg.QUIT: # Ferme le jeu
                    self.restart = False
                    self.is_running = False
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    ## TODO: envoyer les coordonées dans une fonction sonore

        self.quit_motor() # Fermeture du jeu
