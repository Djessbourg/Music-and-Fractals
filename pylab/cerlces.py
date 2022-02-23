import pylab
F = pylab.gca()
def cercle (x,y,r):
    cercle = pylab.Circle([x,y],radius = r ,fill = False, color = 'red' )
    F.add_patch(cercle)
def cerclesRec(x,y,r,sens):
    cercle(x,y,r) 
    if r > 1:
        if sens == 'nul' :
            cerclesRec(x+3 * r/2 , y , r/2,'droite')
            cerclesRec(x ,y+3 * r/2 , r/2 ,'haut')
            cerclesRec(x-3 * r/2 ,y , r/2 ,'gauche')
            cerclesRec(x ,y-3 * r/2 , r/2 ,'bas')
        if sens == 'gauche' :
            cerclesRec(x ,y+3 * r/2 , r/2 ,'haut')
            cerclesRec(x-3 * r/2 ,y , r/2 ,'gauche')
            cerclesRec(x ,y-3 * r/2 , r/2 ,'bas')
        if sens == 'droite':
            cerclesRec(x+3 * r/2 , y , r/2,'droite')
            cerclesRec(x ,y+3 * r/2 , r/2 ,'haut')
            cerclesRec(x ,y-3 * r/2 , r/2 ,'bas')
        if sens == 'haut':
            cerclesRec(x+3 * r/2 , y , r/2,'droite')
            cerclesRec(x ,y+3 * r/2 , r/2 ,'haut')
            cerclesRec(x-3 * r/2 ,y , r/2 ,'gauche')
        if sens == 'bas' :
            cerclesRec(x+3 * r/2 , y , r/2,'droite')
            cerclesRec(x-3 * r/2 ,y , r/2 ,'gauche')
            cerclesRec(x ,y-3 * r/2 , r/2 ,'bas')
cerclesRec(0,0,64,'nul')
pylab.axis('scaled')
pylab.show()