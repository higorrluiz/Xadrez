import pygame
from typing import Type

from importador import POSICOES_TABULEIRO


class Queen(pygame.sprite.Sprite):

    def __init__(self,pos,cor):
        super().__init__()
        self.image = pygame.image.load('assets/images/white queen.png') if cor == 'white' else pygame.image.load('assets/images/black queen.png')
        self.image = pygame.transform.scale(self.image, (68, 68))
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.selecionado = False