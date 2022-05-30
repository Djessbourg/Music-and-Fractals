import pygame as pg

def handle_key_down_event(motor, event):
    if event.key == pg.K_a :
        motor.change_fract("Mandelbrot")
    if event.key == pg.K_z :
        motor.change_fract("Bouglé")
    if event.key == pg.K_e :
        motor.change_fract("Nolan")
    if event.key == pg.K_r :
        motor.change_fract("Horgues")

    if event.key == "MOUSEBUTTONUP":
        pos = pg.mouse.get_pos()
        # faire la conversion des coordonées en un point du plan complexe
        loop = true
        eq = motor.f.get_eq()
        z = eq(0j , pos )
        #enter ici dans une boucle tant que la souris est pressée
        while loop :
            motor.delta(pos,z)
            z = eq(z,pos)
            if even.type != "MOUSEBUTTONUP":
                loop = False
