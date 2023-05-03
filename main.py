import pygame 
from pygame.locals import *
from sys import exit
from importador import *
from tabuleiro import Tabuleiro

pygame.init()
altura= 630
largura=660
botao_exit=769
GREEN   = (  0,255,  0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()


tabuleiro = Tabuleiro()
while True:
    tela.fill('black')
    for event in pygame.event.get():
        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()
        
    tabuleiro.desenhar_tabuleiro(tela)
    tabuleiro.desenhar_peças_pretas(tela)
    tabuleiro.desenhar_peças_brancas(tela)



   
    













    pygame.display.flip()

    #Setting FPS
    clock.tick(60)
    pygame.display.update


