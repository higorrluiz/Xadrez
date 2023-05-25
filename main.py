import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Dummy
from helper import *
import math

sel_x,sel_y=20000,30000
x,y=0,0
peca = Dummy()


while True:
    tela.fill('black')
       
    tabuleiro.desenhar_tabuleiro()
    # tabuleiro.desenhar_pecas_pretas()
    # tabuleiro.desenhar_pecas_brancas()

    black_pawns_group.draw(tela)
    black_pawns_group.update()
    black_pieces_group.draw(tela)
    black_pieces_group.update()
    white_pawns_group.draw(tela)
    white_pawns_group.update()
    white_pieces_group.draw(tela)
    white_pieces_group.update()


    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()
        #permite selecao nas pecas pretas
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(black_pawns)):
                if black_pawns[i].rect.collidepoint(mouse_pos):#checa se o mouse cliclou em um peão preto
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1] 
                    peca = black_pawns[i]
                    peca.selecionado = True
                    print(posicao_do_quadrado())
                    
                
            for j in black_pieces:#checa se o mouse cliclou em um peca preta
                if j.rect.collidepoint(mouse_pos):
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                    peca = j
                    peca.selecionado = True
                    

            if peca.selecionado == True and not (peca.rect.collidepoint(mouse_pos)):#se a peca esta selecionada e o usuario
                x=posicao_do_quadrado()[0]
                y=posicao_do_quadrado()[1]
                sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                
                if peca.nome == 'pawn':
                    if movimentos_validos[0] == (x,y) or movimentos_validos[1] == (x,y):
                        peca.rect.x= x
                        peca.rect.y= y
                        peca.selecionado = False
                
    if peca.selecionado == True and peca.nome == 'pawn':
        x_bolinha=math.ceil(peca.rect.left/tam_quadrado)*tam_quadrado
        y_bolinha=math.floor(peca.rect.top/tam_quadrado)*tam_quadrado
        movimentos_validos  = peca.mostrar_movimentos_validos(x_bolinha,y_bolinha,tela)
    selecionado(sel_x,sel_y)
    












    pygame.display.flip()

    #Setting FPS
    clock.tick(60)
    pygame.display.update


