#introduction à la visualisation d'une fonction complexe#
import pylab as pl
x = pl.linspace(0,10,200)

Z = 2j - x*pl.exp(3j*x)
def im_re (X,Z):
    pl.plot(X,pl.real(Z),label ='partie réelle')
    pl.plot(X,pl.imag(Z),label='partie imaginaire')
    pl.legend()

    pl.show()

def arg_module(X,Z):
    pl.plot(X,abs(Z),label = 'module')
    pl.plot(X,pl.angle(Z),label = 'agrument')
    pl.legend()
    pl.show()

#regardons les choses un peu plus en couleur ...
def couleur ():
    x1 = pl.linspace(-3,3,51)
    y1 = pl.linspace(-3,3,51)
    X1, Y1 = pl.meshgrid(x1, y1)
    Z1 = pl.angle(X1 + 2j*Y1)
    pl.pcolormesh(X1, Y1, Z1, shading='gouraud',cmap= pl.cm.hsv)
    pl.colorbar()
    pl.xlabel('reel')
    pl.ylabel('im')
    pl.show()

