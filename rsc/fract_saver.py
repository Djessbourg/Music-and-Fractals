import numpy as np
H,L =500,500
name = 'Mandelbrot.npy'
def f (x,c):
    return ( x**2 + c  )
MAX_ITERATION = 100
XMIN,XMAX,YMIN,YMAX=-2, +0.5, -1.25, +1.25

M = [[ None for x in range(H)] for y in range(L)]
np.asarray(M)
for y in range (0,H):
    for x in range(0,L):
        cx = XMIN + (x/H) * (XMAX - XMIN)
        cy = -1*(YMIN +(y/L) * (YMAX - YMIN))
        c = complex (cx,cy)
        Xn = complex(0,0)
        n = 0
        while abs(Xn)**2 < 4 and n < MAX_ITERATION :
            Xn = f(Xn , c)
            n = n + 1
        if n == MAX_ITERATION:
            M[x][y] = n
        else :
            M[x][y] = n
np.save(name,M)
