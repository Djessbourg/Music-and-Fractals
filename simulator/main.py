import pygame as pg
import motor as m

if __name__ == '__main__' :

    pg.init()
    # Démarrage du jeu
    motor = m.Motor()
    motor.run()
    # Redémarrage du jeu en cas de redimension de la fenêtre
    while motor.restart:
        pg.init()
        motor = m.Motor()
        motor.run()
