from importador import *
from classes.board import Board
import math

pygame.init()
altura = 550
largura = 550
tam_quadrado = tamanho  # tamanho quadrado linha
botao_exit = 769
GREEN = (0, 255, 0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

tabuleiro: Board = Board(tela, tam_quadrado)

# desenhando pecas pretas
black_pieces_group = pygame.sprite.Group()
for peca in tabuleiro.black:
    black_pieces_group.add(peca)

# desenhando pecas brancas
white_pieces_group=pygame.sprite.Group()
for peca in tabuleiro.white:
    white_pieces_group.add(peca)

def selecionado(x,y):
    x = x/tam_quadrado
    y = y/tam_quadrado
    esquerda = math.floor(x) * tam_quadrado
    cima = math.floor(y) * tam_quadrado
    direita = math.ceil(x) * tam_quadrado - 2
    baixo = math.ceil(y) * tam_quadrado - 2 

    pygame.draw.line(tela, (255,0,0), (esquerda,cima),  (direita,cima),   2)
    pygame.draw.line(tela, (255,0,0), (direita,cima),   (direita,baixo),  2)
    pygame.draw.line(tela, (255,0,0), (esquerda,baixo), (direita,baixo),  2)
    pygame.draw.line(tela, (255,0,0), (esquerda,cima),  (esquerda,baixo), 2)

# pega a posicao do quadro clicado pelo mouse
def posicao_do_quadrado():
    mouse = pygame.mouse.get_pos()
    x_novo = round(mouse[0]/tam_quadrado)*tam_quadrado
    y_novo = round(mouse[1]/tam_quadrado)*tam_quadrado
    return (x_novo, y_novo)
