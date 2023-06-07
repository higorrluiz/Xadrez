import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from classes.king import King
from classes.rook import Rook
from classes.match import Match
from board_helper import *

jogo: Match = Match(tabuleiro)

sel_x, sel_y = 20000, 30000
x, y = 0, 0
peca: Piece = Piece()
white_turn = True
change = True
movimentos_validos = []
# tabuleiro.printa()

pecas = tabuleiro.get_pieces(white_turn)
for p in pecas:
    p.possible_moves(False)

while True:
    tela.fill('black')

    tabuleiro.desenhar_tabuleiro()

    tabuleiro.black_group.draw(tela)
    tabuleiro.black_group.update()
    tabuleiro.white_group.draw(tela)
    tabuleiro.white_group.update()

    pygame.event.set_blocked(pygame.MOUSEMOTION)
    for event in pygame.event.get():
        
        mouse_pos = pygame.mouse.get_pos()

        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()

        # permite selecao nas pecas pretas
        if event.type == pygame.MOUSEBUTTONUP:

            for p in pecas:  # checa se o mouse cliclou em um peca
                if p.rect.collidepoint(mouse_pos):
                    sel_x, sel_y = mouse_pos[0], mouse_pos[1]
                    if not (isinstance(peca, King) and isinstance(p, Rook)):
                        peca = p
                        peca.selecionado = True
                        movimentos_validos = peca.get_moves()
                        movimentos_validos = [POSICOES_TABULEIRO_LISTA[x][y] for (x, y) in movimentos_validos]
                    print(posicao_do_quadrado())

            # se a peca esta selecionada e o usuario
            if peca.selecionado == True and not (peca.rect.collidepoint(mouse_pos)):
                x, y = posicao_do_quadrado()
                sel_x, sel_y = mouse_pos[0], mouse_pos[1]
                
                if (x, y) in movimentos_validos:
                    peca.rect.x = x
                    peca.rect.y = y
                    peca.move((7-round(y/tamanho), round(x/tamanho)))

                    peca.selecionado = False
                    movimentos_validos = []
                    white_turn = not white_turn
                    
                    check = jogo.king_is_checked(white_turn)
                    pecas = tabuleiro.get_pieces(white_turn)
                    for p in pecas:
                        p.possible_moves(check)
                        
                    print(check, jogo.is_checkmate(white_turn, check))
                    print(jogo.cont)
                    # tabuleiro.printa()
    
    for (x, y) in movimentos_validos:
        pygame.draw.circle(tela, (207,14,14), (x+tamanho/2, y+tamanho/2), 10)
    selecionado(sel_x, sel_y)

    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
