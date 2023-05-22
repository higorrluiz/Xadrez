import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Dummy
from ajudar import *
import math

sel_x,sel_y=20000,30000
x,y=0,0
peça = Dummy()


while True:
    tela.fill('black')
       
    tabuleiro.desenhar_tabuleiro()
    # tabuleiro.desenhar_peças_pretas()
    # tabuleiro.desenhar_peças_brancas()

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
        #permite selecao nas peças pretas
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(black_pawns)):
                if black_pawns[i].rect.collidepoint(mouse_pos):#checa se o mouse cliclou em um peão preto
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1] 
                    peça = black_pawns[i]
                    peça.selecionado = True
                    print(posicao_do_quadrado())
                    
                
            for j in black_pieces:#checa se o mouse cliclou em um peça preta
                if j.rect.collidepoint(mouse_pos):
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                    peça = j
                    peça.selecionado = True
                    

            if peça.selecionado == True and not (peça.rect.collidepoint(mouse_pos)):#se a peça esta selecionada e o usuario
                x=posicao_do_quadrado()[0]
                y=posicao_do_quadrado()[1]
                sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                
                if peça.nome == 'pawn':
                    if movimentos_validos[0] == (x,y) or movimentos_validos[1] == (x,y):
                        peça.rect.x= x
                        peça.rect.y= y
                        peça.selecionado = False
                
    if peça.selecionado == True and peça.nome == 'pawn':
        x_bolinha=math.ceil(peça.rect.left/tam_quadrado)*tam_quadrado
        y_bolinha=math.floor(peça.rect.top/tam_quadrado)*tam_quadrado
        movimentos_validos  = peça.mostrar_movimentos_validos(x_bolinha,y_bolinha,tela)
    selecionado(sel_x,sel_y)
    












    pygame.display.flip()

    #Setting FPS
    clock.tick(60)
    pygame.display.update


