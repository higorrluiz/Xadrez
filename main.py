import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from board_helper import *


sel_x,sel_y=20000,30000
x,y=0,0
peca: Piece = Piece()
white_turn = True

while True:
    tela.fill('black')

    tabuleiro.desenhar_tabuleiro()

    black_pieces_group.draw(tela)
    black_pieces_group.update()
    white_pieces_group.draw(tela)
    white_pieces_group.update()


    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()

        # permite selecao nas pecas pretas
        if event.type == pygame.MOUSEBUTTONUP:

            p: Piece
            pecas = tabuleiro.white if white_turn else tabuleiro.black
            for p in pecas:  # checa se o mouse cliclou em um peca preta
                if p.rect.collidepoint(mouse_pos):
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                    peca = p
                    peca.selecionado = True
                    print(posicao_do_quadrado())

            # se a peca esta selecionada e o usuario
            if peca.selecionado == True and not (peca.rect.collidepoint(mouse_pos)):
                x = posicao_do_quadrado()[0]
                y = posicao_do_quadrado()[1]
                sel_x,sel_y = mouse_pos[0], mouse_pos[1]
                
                if peca.name != None and (x, y) in movimentos_validos:
                    peca.rect.x = x
                    peca.rect.y = y
                    peca.selecionado = False
                    white_turn = not white_turn
                
    if peca.selecionado == True and peca.name != None:
        x_bolinha = round(peca.rect.left/tam_quadrado)*tam_quadrado
        y_bolinha = round(peca.rect.top/tam_quadrado)*tam_quadrado
        movimentos_validos = peca.possible_moves(x_bolinha, y_bolinha, tela)
    selecionado(sel_x, sel_y)

    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
