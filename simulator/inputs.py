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
    if event.key == pg.K_t :
        motor.change_fract("Djessy")
    if event.key == pg.K_y :
        motor.change_fract("DjessyBis")
    if event.key == pg.K_UP:
        motor.move_fract('up')
    if event.key == pg.K_DOWN:
        motor.move_fract('down')
    if event.key == pg.K_LEFT:
        motor.move_fract('left')
    if event.key == pg.K_RIGHT:
        motor.move_fract('right')
    if event.key == pg.K_KP_PLUS:
        motor.move_fract('forward')
    if event.key == pg.K_KP_MINUS:
        motor.move_fract('backward')

    if event.key == "MOUSEBUTTONUP":
        pos = pg.mouse.get_pos()
        # faire la conversion des coordonées en un point du plan complexe
        loop = True
        eq = motor.f.get_eq()
        z = eq(0j , pos )
        #enter ici dans une boucle tant que la souris est pressée
        while loop :
            motor.delta(pos,z)
            z = eq(z,pos)
            if event.type != "MOUSEBUTTONUP":
                loop = False
