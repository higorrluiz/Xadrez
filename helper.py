from importador import *
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

def selecionado(pos: tuple[int, int]) -> None:
    x = pos[0]/TAMANHO
    y = pos[1]/TAMANHO
    esquerda = math.floor(x) * TAMANHO
    cima = math.floor(y) * TAMANHO
    direita = math.ceil(x) * TAMANHO - 2
    baixo = math.ceil(y) * TAMANHO - 2 

    pygame.draw.line(tela, (0,0,255), (esquerda,cima),  (direita,cima),   2)
    pygame.draw.line(tela, (0,0,255), (direita,cima),   (direita,baixo),  2)
    pygame.draw.line(tela, (0,0,255), (esquerda,baixo), (direita,baixo),  2)
    pygame.draw.line(tela, (0,0,255), (esquerda,cima),  (esquerda,baixo), 2)

def selecionado_cor(pos: tuple[int, int], cor: tuple[int, int, int]) -> None:
    esquerda = pos[1] * TAMANHO
    cima = (7-pos[0]) * TAMANHO
    direita = (pos[1]+1) * TAMANHO - 2
    baixo = (7-pos[0]+1) * TAMANHO - 2 

    pygame.draw.line(tela, cor, (esquerda,cima),  (direita,cima),   2)
    pygame.draw.line(tela, cor, (direita,cima),   (direita,baixo),  2)
    pygame.draw.line(tela, cor, (esquerda,baixo), (direita,baixo),  2)
    pygame.draw.line(tela, cor, (esquerda,cima),  (esquerda,baixo), 2)

# pega a posicao do quadro clicado pelo mouse
def posicao_do_quadrado() -> tuple[float, float]:
    mouse = pygame.mouse.get_pos()
    x_novo = math.floor(mouse[0]/TAMANHO)*TAMANHO
    y_novo = math.floor(mouse[1]/TAMANHO)*TAMANHO
    return (x_novo, y_novo)
