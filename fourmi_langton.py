from tkinter import *

HAUT = 0
GAUCHE= 1
BAS = 2
DROITE = 3

VIDE = 0
OCCUPE = 1

TAILLE_GRILLE = 100


#x_grille y_grille 100*100 grille pour la fourmi
#x y 500*500 valeur de la fourmi
# definition des fonctions de dessin pour les fourmis
class CanvasFourmi(Canvas):
    def __init__(self, fenetre):
        super().__init__(fenetre, width=500, height=500, bg='white')
        self.pack()
        self.taille_case = int(self['width']) // TAILLE_GRILLE

    def dessine_case(self, x_grille, y_grille, couleur):
        taille = self.taille_case
        x, y = x_grille*taille, y_grille*taille
        x_prime=x+taille
        y_prime=y+taille
        self.create_rectangle(x,y,x_prime,y_prime,fill=couleur,outline=couleur)


class Fourmi:
    def __init__(self, grille, canvas, fx, fy, couleur_dessin='black'):
        self.canvas = canvas
        self.grille = grille
        self.pos_x = fx
        self.pos_y = fy
        self.orientation = HAUT
        self.couleur_dessin = couleur_dessin

    def change_couleur(self):
        print(self.pos_x,self.pos_y)
        if grille[self.pos_x][self.pos_y]==OCCUPE:
            grille[self.pos_x][self.pos_y]=VIDE
            self.canvas.dessine_case(self.pos_x,self.pos_y,self.couleur_dessin)

        elif grille[self.pos_x][self.pos_y]==VIDE:
            grille[self.pos_x][self.pos_y]=OCCUPE
            self.canvas.dessine_case(self.pos_x,self.pos_y,'white')

        if self.pos_x<0: # corrige
            self.pos_x=TAILLE_GRILLE-1
            self.pos_y=TAILLE_GRILLE-self.pos_y
        """ corrige
        elif self.pos_x>TAILLE_GRILLE:
            self.pos_x=0
            self.pos_y=TAILLE_GRILLE-self.pos_y

        elif self.pos_x<0:
            self.pos_x=TAILLE_GRILLE
            self.pos_y=TAILLE_GRILLE-self.pos_y

        elif self.pos_x<0:
            self.pos_x=TAILLE_GRILLE
            self.pos_y=TAILLE_GRILLE-self.pos_y
        
        """
    def step(self):

        if grille[self.pos_x][self.pos_y]==VIDE:
           self.change_couleur()
           self.orientation=self.tourne_droite()

        elif grille[self.pos_x][self.pos_y]==OCCUPE:
            self.change_couleur()
            self.orientation=self.tourne_gauche()

        self.grille=self.avance()


    def tourne_gauche(self):
        self.orientation+=1
        self.orientation%= 4
        return(self.orientation)


    def tourne_droite(self):
        self.orientation-=1
        self.orientation%= 4
        return(self.orientation)



    def avance(self):
        if self.orientation == HAUT:
            self.pos_y += 1
        elif self.orientation == GAUCHE:
            self.pos_x -= 1
        elif self.orientation == DROITE:
            self.pos_x += 1
        elif self.orientation == BAS:
            self.pos_y -= 1


if __name__ == "__main__":
    fenetre_principale = Tk()
    fenetre_principale.title("LANGTON")
    fenetre_principale.geometry("600x600")

    grille = [[VIDE for _ in range(100)] for _ in range(100)]

    canvas = CanvasFourmi(fenetre_principale)

    f1 = Fourmi(grille, canvas, 50, 50,'black')
    #f2 = Fourmi(grille, canvas, 60, 60, 'red')
    #f3 = Fourmi(grille, canvas, 60, 50, 'green')

    def fourmis():
        f1.step()
        #f2.step()
        #f3.step()
        fenetre_principale.after(10, fourmis)

    fourmis()
    fenetre_principale.mainloop()