# Terrain du jeu
import pygame

class Terrain():
    "Terrain de jeu"
    def __init__(self, screen, largeur, hauteur, couleurs):
        self.largeur = largeur # Largeur maximale du terrain
        self.hauteur = hauteur # Hauteur maximale du terrain
        self.couleurs = couleurs # Couleurs pour chaque carré du terrain
        self.liste_carres = [] # Liste pour représenter tous les carrés dessinés
        for i in range(10):
            carre = Carre(self.liste_carres, couleur=self.couleurs[1])
            carre.draw(screen)
            self.liste_carres.append(carre)
    



class Carre:
    def __init__(self, liste_carres, couleur):
        self.x = 0 # Position x où dessiner le carré
        self.y = 50 # Position y où dessiner le carré
        self.liste_carres = liste_carres # Liste des carrés dessinés 
        self.couleur = couleur # Couleur du carré
        self.width = 50 # Largeur du carré
        self.height = 50 # Hauteur du carré

    def draw(self, screen):
        "Dessiner le carré à l'écran"
        for carre in self.liste_carres: # Pour chaque carré dessiné
            self.x = carre.x + 5 # On dessine le nouveau carré plus loin sur l'axe des abscisses
            self.y = carre.y + 5 # On dessine le nouveau carré plus loin sur l'axe des ordonnées

        rect = pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.width, self.height))     




        


