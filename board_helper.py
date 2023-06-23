from importador import *
from classes.board import Board
import math
import pygame

pygame.init()
altura = 550
largura = 550  # tamanho quadrado linha
botao_exit = 769
GREEN = (0, 255, 0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

def selecionado(pos):
    x = pos[0]/tamanho
    y = pos[1]/tamanho
    esquerda = math.floor(x) * tamanho
    cima = math.floor(y) * tamanho
    direita = math.ceil(x) * tamanho - 2
    baixo = math.ceil(y) * tamanho - 2 

    pygame.draw.line(tela, (255,0,0), (esquerda,cima),  (direita,cima),   2)
    pygame.draw.line(tela, (255,0,0), (direita,cima),   (direita,baixo),  2)
    pygame.draw.line(tela, (255,0,0), (esquerda,baixo), (direita,baixo),  2)
    pygame.draw.line(tela, (255,0,0), (esquerda,cima),  (esquerda,baixo), 2)

# pega a posicao do quadro clicado pelo mouse
def posicao_do_quadrado():
    mouse = pygame.mouse.get_pos()
    x_novo = math.floor(mouse[0]/tamanho)*tamanho
    y_novo = math.floor(mouse[1]/tamanho)*tamanho
    return (x_novo, y_novo)
