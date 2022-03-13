import pygame as pg

def handle_key_down_event(motor, event):
    if event.key == pg.K_a :
        motor.change_fract("Mandelbrot")
    if event.key == pg.K_z :
        motor.change_fract("Bouglé")
    if event.key == "MOUSEBUTTONUP":
        pos = pg.mouse.get_pos()
