from tkinter import *

HAUT = 0
GAUCHE = 1
BAS = 2
DROITE = 3
VIDE = 0
OCCUPE = 1

TAILLE_GRILLE = 100


class CanvasFourmi(Canvas):
    def __init__(self, fenetre):
        super().__init__(fenetre, width=500, height=500, bg='white')
        self.pack()
        self.taille_case = int(self['width']) // TAILLE_GRILLE
        self.label_pas = Label(fenetre, text="Nombre de pas : 0")
        self.label_pas.pack()

    def dessine_case(self, x_grille, y_grille, couleur):
        taille = self.taille_case
        x, y = x_grille * taille, y_grille * taille
        x_prime = x + taille
        y_prime = y + taille
        self.create_rectangle(x, y, x_prime, y_prime, fill=couleur, outline=couleur)

    def actu(self, pas):
        self.label_pas.config(text="Nombre de pas : {}".format(pas))


class FourmiPrecalcul:
    def __init__(self, grille, canvas, positions, couleur_dessin='black'):
        self.canvas = canvas
        self.grille = grille
        self.positions = positions
        self.pos_index = 0
        self.couleur_dessin = couleur_dessin

    def change_couleur(self):
        x, y = self.positions[self.pos_index]
        if self.grille[x][y] == OCCUPE:
            self.grille[x][y] = VIDE
            self.canvas.dessine_case(x, y, self.couleur_dessin)
        elif self.grille[x][y] == VIDE:
            self.grille[x][y] = OCCUPE
            self.canvas.dessine_case(x, y, 'white')

    def precalcule(self, n):
        for _ in range(n):
            self.change_couleur()
            self.pos_index += 1

    def affiche(self):
        if self.pos_index < len(self.positions):
            x, y = self.positions[self.pos_index]
            self.canvas.dessine_case(x, y, self.couleur_dessin)

    def est_fini(self):
        return self.pos_index >= len(self.positions)


if __name__ == "__main__":
    fenetre_principale = Tk()
    fenetre_principale.title("LANGTON")
    fenetre_principale.geometry("600x650")

    grille = [[VIDE for _ in range(100)] for _ in range(100)]

    canvas = CanvasFourmi(fenetre_principale)

    positions_prealculees = [(50, 50)]  # Ajoutez ici les positions précalculées

    f1 = FourmiPrecalcul(grille, canvas, positions_prealculees, 'black')

    def fourmis():
        f1.affiche()
        canvas.actu(len(f1.positions))
        if not f1.est_fini():
            fenetre_principale.after(10, fourmis)

    f1.precalcule(1000)  # Précalcule les 1000 premières itérations
    fourmis()

    fenetre_principale.mainloop()
