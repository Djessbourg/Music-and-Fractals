### flocon de Van Koch ###
import turtle as tr 
def flocon_1 (l):
    tr.forward(l/3)
    tr.left(60)
    tr.forward(l/3)
    tr.right(120)
    tr.forward(l/3)
    tr.left(60)
    tr.forward(l/3)

def flocon_2 (l):
    flocon_1(l/3)
    tr.left(60)
    flocon_1(l/3)
    tr.right(120)
    flocon_1(l/3)
    tr.left(60)
    flocon_1(l/3)

def flocon_n (l,n):
    if n == 1:
        flocon_1(l)
    else:
        flocon_n(l/3,n-1)
        tr.left(60)
        flocon_n(l/3,n-1)
        tr.right(120)
        flocon_n(l/3,n-1)
        tr.left(60)
        flocon_n(l/3,n-1)

def flocon_entier (l,n):
    flocon_n(l,n)
    tr.right(120)
    flocon_n(l,n)
    tr.right(120)
    flocon_n(l,n)
    tr.right(120)