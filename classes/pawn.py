import pygame
from importador import POSICOES_TABULEIRO

class Pawn(pygame.sprite.Sprite):

    def __init__(self,pos,cor):
        super().__init__()
        self.image = pygame.image.load('assets/images/white pawn.png') if cor == 'white' else pygame.image.load('assets/images/black pawn.png')
        self.image = pygame.transform.scale(self.image, (68, 68))
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.selecionado = False

    def mostrar_movimentos_validos(self,x_atual, y_atual,tela):
        x1_valido = x_atual+(68.75/2)
        y1_valido=y_atual+68.75*2+(68.75/2)
        x2_valido = x1_valido
        y2_valido= y1_valido +68.75
        pygame.draw.circle(tela, (207,14,14), (x1_valido,y1_valido), 10) 
        pygame.draw.circle(tela, (207,14,14), (x2_valido,y2_valido), 10)
        return (x_atual,y_atual+(68.75*2)), (x_atual,y_atual+68.75*3)
    

   
        