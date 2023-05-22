import pygame 
from pygame.locals import *
from classes.pawn import Pawn
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
        black_pieces_group=pygame.sprite.Group()
        for peça_preta in black_pieces:
            black_pieces_group.add(peça_preta)

        black_pieces_group.draw(self.tela)
        black_pieces_group.update()

        #desenhando peão


    def desenhar_peças_brancas(self):
        white_pieces_group=pygame.sprite.Group()
        for peça_branca in white_pieces:
            white_pieces_group.add(peça_branca)

        white_pieces_group.draw(self.tela)
        white_pieces_group.update()
        

        #desenhando peão
        x=0
        y=self.tam_tabuleiro
        y= y - self.tamanho_quadrado
        white_pawns_group=pygame.sprite.Group()
        for i in range(8):
            white_pawns.append(Pawn((x,y),"white"))
            white_pawns_group.add(white_pawns[-1])
            x= x+ self.tamanho_quadrado

        white_pawns_group.draw(self.tela)
        white_pawns_group.update()


    #metodos privados
    def __desenhar_linha(self, linha, coluna, primeira_cor, segunda_cor):
        tam = self.tamanho_quadrado
        if coluna % 2 == 0:
            pygame.draw.rect(self.tela, primeira_cor, (coluna*tam,linha*tam,tam,tam))
        else:
            pygame.draw.rect(self.tela, segunda_cor, (coluna*tam,linha*tam,tam,tam))


