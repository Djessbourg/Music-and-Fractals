import pygame as pg
import numpy as np
Rate = 44100
pg.init()
pg.mixer.init()

class Sound:
    def __init__(self,frequency,amplitude,duration):
        self.f = frequency # [Hz]
        self.a = amplitude # [V]
        self.d = duration # [s]
        self.frames = int(self.d * Rate)

    def make_sine_sound(self):
        arr = np.sin(2*np.pi*self.f*np.linespace(0,self.d,self.frames))
        sound = np.asarray([32767*arr,32767*arr]).astype(np.float16)
        sound = pg.sndarray.make_sound(sound.copy())
        sound.play()

from pyo import *
'''
s = Server().boot()
s.amp = 0.1

# Creates two objects with cool parameters, one per channel.
a = FM().out()
b = FM().out(1)

# Opens the controller windows.
a.ctrl(title="Frequency modulation left channel")
b.ctrl(title="Frequency modulation right channel")

# If a list of values is given at a particular argument, the ctrl
# window will show a multislider to set each value separately.

oscs = Sine([100, 200, 300, 400, 500, 600, 700, 800], mul=0.1).out()
oscs.ctrl(title="Simple additive synthesis")
s.gui(locals())
'''
