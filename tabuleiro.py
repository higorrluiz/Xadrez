import pygame 
from pygame.locals import *
class Tabuleiro:
    def __init__(self):
        self.linhas = 8
        self.colunas = 8
        self.tamanho_quadrado = 550 // 8


    def desenhar_peças(self,tela):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if linha % 2 == 0: #se a linha for par(primeiro indice é zero) desenha branco e verde(nessa ordem)
                    self.__desenhar_linha(tela, linha, coluna, 'white', 'dark green')
                else:
                    self.__desenhar_linha(tela, linha, coluna, 'dark green', 'white')


    #metodos privados
    def __desenhar_linha(self,tela, linha, coluna, primeira_cor, segunda_cor):
        tam = self.tamanho_quadrado
        if coluna % 2 == 0:
            pygame.draw.rect(tela, primeira_cor, (coluna*tam,linha*tam,tam,tam))
        else:
            pygame.draw.rect(tela, segunda_cor, (coluna*tam,linha*tam,tam,tam))

            