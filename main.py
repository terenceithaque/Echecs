# Script principal du jeu
import pygame
pygame.init() # Démarrer le module pygame

largeur = 800 # Largeur de l'écran
hauteur = 600 # Hauteur de l'écran

window = pygame.display.set_mode((largeur, hauteur)) # Créer une fenêtre de jeu en suivant les dimensions indiquées
pygame.display.set_caption("Echecs !")

running = True # On crée une variable pour obtenir l'état actuel de l'exécution du jeu.

while running: # Tant que le jeu est en cours d'exécution
    for evenement in pygame.event.get(): # Pour chaque évènement intercepté pendant l'exécution de la boucle de jeu
        if evenement.type == pygame.QUIT: # Si le joueur désire quitter le jeu
            running = False # Alors on arrête le jeu

