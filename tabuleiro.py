import pygame 
from pygame.locals import *
from importador import *

class Tabuleiro:
    def __init__(self,tela):
        self.linhas = 8
        self.colunas = 8
        self.tamanho_quadrado = 68.75
        self.tela = tela
        self.tam_tabuleiro = self.tamanho_quadrado * 7


    def desenhar_tabuleiro(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if linha % 2 == 0: #se a linha for par(primeiro indice é zero) desenha branco e verde(nessa ordem)
                    self.__desenhar_linha(linha, coluna, 'white', 'dark green')
                else:
                    self.__desenhar_linha(linha, coluna, 'dark green', 'white')


    def desenhar_peças_pretas(self):
        x = 0
        for peça_preta in black_pieces:
            self.tela.blit(peça_preta,(x,0))
            x= x+ self.tamanho_quadrado
        x=0
        for pawn in black_pawns:
            self.tela.blit(pawn,(x,self.tamanho_quadrado))
            x= x+ self.tamanho_quadrado

    def desenhar_peças_brancas(self):
        x = 0
        y=self.tam_tabuleiro
        for peça_branca in white_pieces:
            self.tela.blit(peça_branca,(x,y))
            x= x+ self.tamanho_quadrado
        x=0
        y= y - self.tamanho_quadrado
        for pawn in white_pawns:
            self.tela.blit(pawn,(x,y))
            x= x+ self.tamanho_quadrado


    #metodos privados
    def __desenhar_linha(self, linha, coluna, primeira_cor, segunda_cor):
        tam = self.tamanho_quadrado
        if coluna % 2 == 0:
            pygame.draw.rect(self.tela, primeira_cor, (coluna*tam,linha*tam,tam,tam))
        else:
            pygame.draw.rect(self.tela, segunda_cor, (coluna*tam,linha*tam,tam,tam))

            