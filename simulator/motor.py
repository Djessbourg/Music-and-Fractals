import pygame as pg
import fract
import sound

class Motor :
    def __init__ (self):
        self.f = fract.Fract_manager()
        self.size = self.f.get_size()
        self.screen = pg.display.set_mode(self.size) # taille de la fenêtre
        pg.display.set_caption("Sound of Fractals")
    
    def quit_game(self):
        """Ferme le jeu"""
        pg.quit()

    def run(self):
        """Boucle principale"""
        clock = pg.time.Clock()
        self.is_running = True

        while self.is_running:
            pg.display.flip()  # Mise à jour de l'écran

            # Gestion des évènements
            for event in pg.event.get():
                if event.type == pg.QUIT: # Ferme le jeu
                    self.restart = False
                    self.is_running = False
            clock.tick(60)  # Attente jusqu'à la prochaine image

        self.quit_game() # Fermeture du jeu
