THIS READ ME IS IN FRENCH (AND WILL BE SOON TRANSLATED TO ENGLISH)

Ce document vous permet dans un premier temps de générér des fractales à partir de holomorphismes. Je vous présente la prise en main : 
-Lorsque vous lancer le fichier main.py pour la première fois, vous tombez sur l'ensemble de Mandelbrot avec des nuances rouges.
-Pour naviguer dans cet espace vous pouver utiliser les flèches directionnelles de votre clavier et vous pouvez effectuer des zooms avec les touches "+" et "-".
-Vous pouvez changer de fractales avec les touches a z e r t y u (toutes ont des fractales préenregistrées)

Pour ceux qui veulent bidouiller:

Ajouter une fractale:
Rendez-vous dans le fichier fract.py 
Vous pouvez inmplémenter vos fractales à partir de la ligne 24 en jouant sur différents arguments:
  * Size : la taille de la fenetre en pixel qui s'écrit comme une liste
  * eq : la fonction complexe associée à votre fractale (s'écrit sous la nomenclature lambda z,c: ...)
  * color : une chaîne de caractères associer à un dictionaire de couleur ("basic","purple,"ew","black","light black","blue","hard blue","hard red"). Ce dictionaire peut être enrichie
    avec la fonction color_register à partir de la ligne 34
  * name : une chaine de caractère nomant votre fractale
  * coord : positions des extremums du plan sous la forme [XMIN,XMAX,YMIN,YMAX]
  * julia : entier indiquant le type de fractale ( 0 = type Mandelbrot et  1 = type julia)
  * c : nombre complex de départ pour un enxemble de Julia
  * file : indique par un booléen si la fratale possède un fichier npy dans le fichier rsc (fonctionalité par encore au point)
  * zoom : 0 par défault, indique le zoom initial appliqué
Vous pouvez modifier la fractale affichée au lancement du programe en modifiant à la ligne 20 le nom de la fractale pour self.currentfract
