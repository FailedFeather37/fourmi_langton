from tkinter import *

HAUT = 0
GAUCHE= 1
BAS = 2
DROITE = 3

VIDE = 0
OCCUPE = 1

TAILLE_GRILLE = 100 # nombre de colonne et ligne

# definition des fonctions de dessin pour les fourmis
class CanvasFourmi(Canvas):
    def __init__(self, fenetre):
        super().__init__(fenetre, width=500, height=500, bg='white')
        self.pack()
        self.taille_case = int(self['width']) // TAILLE_GRILLE

    def dessine_case(self, x_grille, y_grille, couleur):
        taille = self.taille_case
        x, y = x_grille, y_grille
        x_prime=x+taille
        y_prime=y+taille
        self.create_rectangle(x,y,x_prime,y_prime,fill=couleur,outline=couleur)

# definition d'une fourmi de langton
class Fourmi:
    # constructeur avec le canvas pour le dessin, la position initiale x et y et la couleur de la fourmi si different de noir
    def __init__(self, grille, canvas, fx, fy, couleur_dessin='black'):
        self.canvas = canvas
        self.grille = grille
        self.pos_x = fx
        self.pos_y = fy
        self.orientation = HAUT
        self.couleur_dessin = couleur_dessin # la couleur que la fourmi laissera derriere elle

    # change la couleur sous la position actuelle de la fourmi
    def change_couleur(self):
        if self.grille[self.pos_x][self.pos_y]==VIDE:
           self.grille[self.pos_x][self.pos_y]=OCCUPE
           # inverser la couleur sous la fourmi
        canvas.dessine_case(self.pos_x,self.pos_y,self.couleur_dessin)

        # choisir la couleur a dessiner

        # dessiner la nouvelle case sur le canvas
        #self.grille[self.pos_x][self.pos_y].dessine_case()

    def step(self):
        if self.grille[self.pos_x][self.pos_y]==VIDE:
           self.change_couleur()
           #self.orientation=tourne_droite() corrige

        # si la grille est vide on inverse la couleur et tourne a droite
        else:
             #canvas.change_couleur() corrige
             self.orientation+=GAUCHE
             #self.orientation=tourne_gauche() corrige
        # si la grille est occupee on inverse la couleur et tourne a gauche
        #self.dessine_case()

    def tourne_gauche(self):
        a=self.orientation % GAUCHE
        self.orientation+=a
        return (self.orientation)
        # change l'orientation d'un cran vers la gauche

    def tourne_droite(self):
        a=self.orientation % GAUCHE
        self.orientation+=a
        return(self.orientation)
        # change l'orientation d'un cran vers la droite

    def avance(self):
        self.grille[self.pos_x][self.pos_y].dessine_case()
        # avance de une case en suivant la bonne orientation


if __name__ == "__main__":
    fenetre_principale = Tk()
    fenetre_principale.title("LANGTON")
    fenetre_principale.geometry("600x600")

    grille = [[VIDE for _ in range(100)] for _ in range(100)]

    canvas = CanvasFourmi(fenetre_principale)

    # initialisation des fourmis
    f1 = Fourmi(grille, canvas, 50, 50)
    #f2 = Fourmi(grille, canvas, 60, 60, 'red')
    #f3 = Fourmi(grille, canvas, 60, 50, 'green')

    # fonction appelee recursivement
    def fourmis():
        f1.step()
        #f2.step()
        #f3.step()

        fenetre_principale.after(10, fourmis)

    #fenetre_principale.after(10, fourmis)

    # a supprimer une fois que l'affichage marche
    #canvas.dessine_case(0, 0, "black")
    #canvas.dessine_case(50, 50, "red")
    fourmis()
    print(grille)
    fenetre_principale.mainloop()