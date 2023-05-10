import pygame
from typing import Type


class Pawn(pygame.sprite.Sprite):

    def __init__(self,pos,cor):
        super().__init__()
        self.image = pygame.image.load('assets/images/white pawn.png') if cor == 'white' else pygame.image.load('assets/images/black pawn.png')
        self.image = pygame.transform.scale(self.image, (68, 68))
        self.rect = self.image.get_rect(topleft=pos)
        self.selecionado = False

   
        