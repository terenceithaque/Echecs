# Script principal du jeu
import pygame
from tkinter import messagebox
from terrain import *

pygame.init() # Démarrer le module pygame

largeur = 800 # Largeur de l'écran
hauteur = 600 # Hauteur de l'écran

window = pygame.display.set_mode((largeur, hauteur)) # Créer une fenêtre de jeu en suivant les dimensions indiquées
pygame.display.set_caption("Echecs !")

running = True # On crée une variable pour obtenir l'état actuel de l'exécution du jeu.


def quitter_jeu():
    "Demander au joueur s'il souhaite quitter le jeu"
    quitter = messagebox.askquestion("Désirez-vous quitter le jeu ?", "Voulez-vous quitter le jeu maintenant ?") # Afficher une boîte de dialogue pour demander au joueur s'il souhaite arrêter de jouer
    if quitter == "yes": # Si le joueur clique sur "Oui"
        global running
        running = False # Alors on arrête le jeu


terrain = Terrain(window, 800, 600, [(212, 29, 57), (127, 127, 127)])        


while running: # Tant que le jeu est en cours d'exécution
    for evenement in pygame.event.get(): # Pour chaque évènement intercepté pendant l'exécution de la boucle de jeu
        if evenement.type == pygame.QUIT: # Si le joueur désire quitter le jeu
            quitter_jeu()


    pygame.display.flip()





