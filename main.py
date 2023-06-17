import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from classes.match import Match
from board_helper import *
from menu import Menu

game_loop = True
game_state = "menu"
menu = Menu(tela, game_loop, game_state)
show_possible_moves = True

while game_loop:
    tela.fill('black')
    if game_state == "menu":
        game_loop, game_state = menu.draw()
    elif game_state == "options":
        show_possible_moves, game_state = menu.options(show_possible_moves)
    elif game_state == "checkmate":
        game_loop, game_state = menu.checkmate(winner)
    elif game_state == "new_game":
        tabuleiro: Board = Board(tela, tamanho)
        jogo: Match = Match(tabuleiro)
        sel_x, sel_y = 20000, 30000
        x, y = 0, 0
        peca: Piece = Piece()
        white_turn = True
        check = False
        movimentos_validos = []
        pecas = tabuleiro.get_pieces(white_turn)
        for p in pecas:
            p.possible_moves(check)
        game_state = "game"

    elif game_state == "game":
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
                p: Piece
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
                        peca.move((7-round(y/tamanho), round(x/tamanho)))
                        
                        peca.selecionado = False
                        movimentos_validos = []
                        if white_turn:
                            jogo.passant_black = None
                        else:
                            jogo.passant_white = None
                        white_turn = not white_turn
                        
                        check = jogo.king_is_checked(white_turn)
                        pecas = tabuleiro.get_pieces(white_turn)
                        for p in pecas:
                            p.possible_moves(check)
                            
                        if jogo.is_checkmate(white_turn, check):
                            game_state = "checkmate"
                            menu.game_state = game_state
                            winner = "black" if white_turn else "white"

                        if jogo.is_draw(white_turn, check):
                            pass
                        # tabuleiro.printa()
                        
        if show_possible_moves:
            for (x, y) in movimentos_validos:
                pygame.draw.circle(tela, (207,14,14), (x+tamanho/2, y+tamanho/2), 10)
        selecionado(sel_x, sel_y)

    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
