from tkinter import *

HAUT = 0
GAUCHE = 1
BAS = 2
DROITE = 3
i = 0
VIDE = 0
OCCUPE = 1

TAILLE_GRILLE = 100


class FourmiPrecalcul:
    def step(self):
        global i
        i+=1
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
        
        
    def precalcule(self,n):
        pass
            

if __name__ == "__main__":
    fenetre_principale = Tk()
    fenetre_principale.title("LANGTON")
    fenetre_principale.geometry("600x600")

    grille = [[VIDE for _ in range(100)] for _ in range(100)]