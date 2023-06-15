import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from classes.king import King
from classes.rook import Rook
from classes.match import Match
from board_helper import *
from menu import Menu
from ai import ChessPlayer
import evaluation as eval

jogo: Match = Match(tabuleiro)

sel_x, sel_y = 20000, 30000
x, y = 0, 0
peca: Piece = Piece()
white_turn = True
change = True
movimentos_validos = []


game_loop = True
game_state = "menu"
menu = Menu(tela, game_loop, game_state)
show_possible_moves = True

ai_player = ChessPlayer(False,jogo,tabuleiro,1)

while game_loop:
    tela.fill('black')
    if game_state == "menu":
        game_loop, game_state = menu.draw()
    elif game_state == "options":
        show_possible_moves, game_state = menu.options(show_possible_moves)
    elif game_state == "game":
        tabuleiro.desenhar_tabuleiro()

        tabuleiro.black_group.draw(tela)
        tabuleiro.black_group.update()
        tabuleiro.white_group.draw(tela)
        tabuleiro.white_group.update()

        if change:
            p: Piece
            pecas = tabuleiro.white if white_turn else tabuleiro.black
            for p in pecas:
                p.possible_moves()
            change = False
        
        if white_turn:
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
                            if white_turn:
                                jogo.passant_black = None
                            else:
                                jogo.passant_white = None
                            white_turn = not white_turn
                            change = True
                            tabuleiro.desenhar_tabuleiro()
                            tabuleiro.black_group.draw(tela)
                            tabuleiro.black_group.update()
                            tabuleiro.white_group.draw(tela)
                            tabuleiro.white_group.update()

            if show_possible_moves:
                for (x, y) in movimentos_validos:
                    pygame.draw.circle(tela, (207,14,14), (x+tamanho/2, y+tamanho/2), 10)
            selecionado(sel_x, sel_y)
        else:
            if ai_player.color == white_turn:
                ai_player.set_next_move()
                peca, move = ai_player.next_move
                
                # peca, move = ai.minimaxRoot(3, tabuleiro, False)
                peca.move(move)
                print("tabuleiro após")
                tabuleiro.printa()


                white_turn = not white_turn
                pecas = tabuleiro.get_pieces(white_turn)
                change = True
    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
