### Arbre de pythagore ###
import turtle as tr

def arbre_1 (L,a=30):
    tr.forward(L/3)
    tr.left(a)
    tr.forward(2*L /3)
    tr.back(2*L/3)
    tr.right(2*a)
    tr.forward(2*L /3)
    tr.back(2*L /3)
    tr.left(a)
    tr.back(L/3)

def arbre_2 (L,a=30):
    tr.forward(L)
    tr.left(a)
    arbre_1(L,a)
    tr.right(2*a)
    arbre_1(L,a)
    tr.left(a)
    tr.back(L)


def arbre_n(L,n,a=30):
    'il fauf faire un tr.left(90);arbre_n(L,n) pour qu il soit droit'
    if n == 1 :
        arbre_1(L)
    else : 
        tr.forward(L)
        tr.left(a)
        arbre_n(3*L/4,n-1)
        tr.right(2*a)
        arbre_n(3*L/4,n-1)
        tr.left(a)
        tr.back(L)
