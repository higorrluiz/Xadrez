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
    black_pawns.append(Pawn(pos,False))
    black_pawns_group.add(black_pawns[-1])


## desenhando pecas pretas
black_pieces = [Rook('A8',False), Knight('B8', False), Bishop('C8',False), King('D8',False), Queen('E8',False), Bishop('F8',False), Knight('G8',False), Rook('H8',False)]

black_pieces_group=pygame.sprite.Group()
for peca in black_pieces:
    black_pieces_group.add(peca)

#### desenhando pawns brancos####
white_pawns_group=pygame.sprite.Group()
for pos in posicoes_pawns_brancos:
    white_pawns.append(Pawn(pos,True))
    white_pawns_group.add(white_pawns[-1])

#####desenhando pecas brancas##########
white_pieces = [Rook('A1',True), Knight('B1', True), Bishop('C1',True), King('D1',True), Queen('E1',True), Bishop('F1',True), Knight('G1',True), Rook('H1',True)]

white_pieces_group=pygame.sprite.Group()
for peca in white_pieces:
    white_pieces_group.add(peca)


def selecionado(x,y):
    x=x/tam_quadrado
    y=y/tam_quadrado
    esquerda = math.floor(x)*tam_quadrado
    cima = math.floor(y)*tam_quadrado
    direita = math.ceil(x) * tam_quadrado
    baixo = math.ceil(y) * tam_quadrado

    pygame.draw.line(tela,(255,0,0),(esquerda,cima),(direita,cima),2)
    pygame.draw.line(tela,(255,0,0),(direita,cima),(direita,baixo),2)
    pygame.draw.line(tela,(255,0,0),(esquerda,baixo),(direita,baixo),2)
    pygame.draw.line(tela,(255,0,0),(esquerda,cima),(esquerda,baixo),2)

def posicao_do_quadrado():#pega a posicao do quadro clicado pelo mouse
    mouse = pygame.mouse.get_pos()
    x_novo=math.floor(mouse[0]/tam_quadrado)*tam_quadrado
    y_novo=math.floor(mouse[1]/tam_quadrado)*tam_quadrado
    return x_novo, y_novo
