from importador import *
from classes.pawn import Pawn
from classes.rook import Rook
from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.queen import Queen
from tabuleiro import Tabuleiro
import math

pygame.init()
altura= 550
largura=550
tam_quadrado = 68.75 #tamanho quadrado linha
botao_exit=769
GREEN   = (  0,255,  0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()



peca = None
tabuleiro = Tabuleiro(tela)

#desenhando pawns pretos
black_pawns_group=pygame.sprite.Group()
for pos in posicoes_pawns_pretos:
    black_pawns.append(Pawn(pos,"black"))
    black_pawns_group.add(black_pawns[-1])


## desenhando pecas pretas
black_pieces = [Rook('8A',"black"), Knight('8B', "black"), Bishop('8C',"black"), King('8D',"black"), Queen('8E',"black"), Bishop('8F',"black"), Knight('8G',"black"), Rook('8H',"black")]

black_pieces_group=pygame.sprite.Group()
for peca in black_pieces:
    black_pieces_group.add(peca)

#### desenhando pawns brancos####
white_pawns_group=pygame.sprite.Group()
for pos in posicoes_pawns_brancos:
    white_pawns.append(Pawn(pos,"white"))
    white_pawns_group.add(white_pawns[-1])

#####desenhando pecas brancas##########
white_pieces = [Rook('1A',"white"), Knight('1B', "white"), Bishop('1C',"white"), King('1D',"white"), Queen('1E',"white"), Bishop('1F',"white"), Knight('1G',"white"), Rook('1H',"white")]

white_pieces_group=pygame.sprite.Group()
for peca in white_pieces:
    white_pieces_group.add(peca)


def selecionado(x,y):
    x=x/tam_quadrado
    y=y/tam_quadrado
    vermelho = math.floor(x)*tam_quadrado
    rosa = math.floor(y)*tam_quadrado
    amarelo = math.ceil(x) * tam_quadrado
    azul = math.ceil(y) * tam_quadrado

    pygame.draw.line(tela,(255,0,0),(vermelho,rosa),(amarelo,rosa),2)
    pygame.draw.line(tela,(255,0,0),(amarelo,rosa),(amarelo,azul),2)
    pygame.draw.line(tela,(255,0,0),(vermelho,azul),(amarelo,azul),2)
    pygame.draw.line(tela,(255,0,0),(vermelho,rosa),(vermelho,azul),2)

def posicao_do_quadrado():#pega a posicao do quadro clicado pelo mouse
    mouse = pygame.mouse.get_pos()
    x_novo=math.floor(mouse[0]/tam_quadrado)*tam_quadrado
    y_novo=math.floor(mouse[1]/tam_quadrado)*tam_quadrado
    return x_novo, y_novo