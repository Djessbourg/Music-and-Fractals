import turtle as tr
def triangle (l):
    tr.forward(l)
    tr.left(120)
    tr.forward(l)
    tr.left(120)
    tr.forward(l)
    tr.left(120)

def triangle_1(l):
    triangle(l)
    tr.forward(l)
    triangle(l)
    tr.forward(l)
    tr.left(120)
    tr.forward(l)
    triangle(l)
    tr.forward(l)
    tr.left(120)
    tr.forward(2*l)
    tr.left(120)

def triangle_2(l):
    triangle_1(l)
    tr.forward(2*l)
    triangle_1(l)
    tr.forward(2*l)
    tr.left(120)
    tr.forward(2*l)
    triangle_1(l)
    tr.forward(2*l)
    tr.left(120)
    tr.forward(4*l)
    tr.left(120)

def triangle_n (l,n):
    if n == 1 :
        triangle_1(l)
    else:
        triangle_n(l,n-1)
        tr.forward(2**(n-1)*l)
        triangle_n(l,n-1)
        tr.forward(2**(n-1)*l)
        tr.left(120)
        tr.forward(2**(n-1)*l)
        triangle_n(l,n-1)
        tr.forward(2**(n-1)*l)
        tr.left(120)
        tr.forward(2**n*l)
        tr.left(120)
print ('coucou')
