import pygame 
from pygame.locals import *
from importador import *

class Tabuleiro:
    def __init__(self):
        self.linhas = 8
        self.colunas = 8
        self.tamanho_quadrado = 68.75


    def desenhar_tabuleiro(self,tela):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if linha % 2 == 0: #se a linha for par(primeiro indice é zero) desenha branco e verde(nessa ordem)
                    self.__desenhar_linha(tela, linha, coluna, 'white', 'dark green')
                else:
                    self.__desenhar_linha(tela, linha, coluna, 'dark green', 'white')

    def desenhar_peças_pretas(self,tela):
        x = 0
        for peça_preta in black_pieces:
            tela.blit(peça_preta,(x,0))
            x= x+ 68.75
        x=0
        for pawn in black_pawns:
            tela.blit(pawn,(x,68.75))
            x= x+ 68.75

    def desenhar_peças_brancas(self,tela):
        x = 0
        y=550 - 68.78
        for peça_branca in white_pieces:
            tela.blit(peça_branca,(x,y))
            x= x+ 68.75
        x=0
        y= y - 68.78
        for pawn in white_pawns:
            tela.blit(pawn,(x,y))
            x= x+ 68.75


    #metodos privados
    def __desenhar_linha(self,tela, linha, coluna, primeira_cor, segunda_cor):
        tam = self.tamanho_quadrado
        if coluna % 2 == 0:
            pygame.draw.rect(tela, primeira_cor, (coluna*tam,linha*tam,tam,tam))
        else:
            pygame.draw.rect(tela, segunda_cor, (coluna*tam,linha*tam,tam,tam))

            