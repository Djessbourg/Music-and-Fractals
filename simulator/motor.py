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
        'affiche sur l écran pygame la fractale en mémoire'                    # trouver une manière de conserver les données de la fractale de manière à optimiser le temps de calcul
        size = self.size
        "color = self.color"
        for y in range (size[0]):
            for x in range (size[1]):
                p = self.f.is_in(x,y)
                if p == 1 :
                    screen.set_at((x, y), (0, 0,0))
                if p == 0 :
                    screen.set_at((x, y), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256)) #TO DO: créer différents modes de colorisation
                pg.display.flip()

    def run(self):
        """Boucle principale"""
        "clock = pg.time.Clock()"
        self.draw_fract()
        self.is_running = True

        while self.is_running:
            "pg.display.flip() " # Mise à jour de l'écran

            # Gestion des évènements
            for event in pg.event.get():
                if event.type == pg.QUIT: # Ferme le jeu
                    self.restart = False
                    self.is_running = False
            "clock.tick(60)"  # Attente jusqu'à la prochaine image

        self.quit_motor() # Fermeture du jeu
