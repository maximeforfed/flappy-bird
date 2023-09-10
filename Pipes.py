import random

import pygame


class PipesAleatoire:
    display = True
    pipe = pygame.image.load("sprites/pipe-green.png")

    vitesse = 2
    position = 600
    taille = 0

    def __init__(self, position):

        self.taille = random.randint(0,200)
        self.position = position


    def calcul(self):


        self.position = self.position - self.vitesse

    def display(self, screen):

        screen.blit(self.pipe, (self.position,550-150 - self.taille ))
