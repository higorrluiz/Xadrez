import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from classes.match import Match
from board_helper import *
from menu import Menu
from ai import ChessPlayer
import evaluation as eval


def desenha_tela(tabuleiro: Board) -> None:
    tabuleiro.desenhar_tabuleiro()
    tabuleiro.black_group.draw(tela)
    tabuleiro.black_group.update()
    tabuleiro.white_group.draw(tela)
    tabuleiro.white_group.update()


def end_turn(jogo: Match, tabuleiro: Board, white_turn: bool) -> tuple[bool, list[Piece]]:
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
        # tela de fim de jogo: xeque-mate
        pass
    tabuleiro.printa()

    return (white_turn, pecas)


def player(jogo: Match, tabuleiro: Board, white_turn: bool, peca: Piece, pecas: list[Piece], movimentos_validos: list[tuple[int, int]], 
           sel: tuple[int, int]) -> tuple[bool, Piece, list[Piece], list[tuple[int, int]], list[tuple[int, int]]]:
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()

        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()

        # permite selecao nas pecas
        if event.type == pygame.MOUSEBUTTONUP:

            for p in pecas:  
                # checa se o mouse cliclou em um peca
                if p.rect.collidepoint(mouse_pos):
                    sel = mouse_pos
                    peca = p
                    peca.selecionado = True
                    print(peca.name, peca.is_white)
                    movimentos_validos = peca.get_moves()
                    movimentos_validos = [POSICOES_TABULEIRO_LISTA[x][y] for (x, y) in movimentos_validos]
                    print(posicao_do_quadrado())

            # se a peca esta selecionada e o usuario clica em outro quadrado
            if peca.selecionado == True and not (peca.rect.collidepoint(mouse_pos)):
                x, y = posicao_do_quadrado()
                sel = mouse_pos
                if (x, y) in movimentos_validos:
                    peca.move((7-round(y/tamanho), round(x/tamanho)))
                    peca.selecionado = False
                    movimentos_validos = []
                    white_turn, pecas = end_turn(jogo, tabuleiro, white_turn)
                    desenha_tela(tabuleiro)

    if show_possible_moves:
        for (x, y) in movimentos_validos:
            pygame.draw.circle(tela, (207,14,14), (x+tamanho/2, y+tamanho/2), 10)
    selecionado(sel)

    return (white_turn, peca, pecas, movimentos_validos, sel)


jogo: Match = Match(tabuleiro)

sel = (20000, 30000)
peca: Piece = Piece()
white_turn = True
check = False
movimentos_validos = []

game_loop = True
game_state = "menu"
menu = Menu(tela, game_loop, game_state)
show_possible_moves = True
has_ia = True
player_is_white = True

if has_ia: ai_player = ChessPlayer(not player_is_white, jogo, tabuleiro, 4)

pecas = tabuleiro.get_pieces(white_turn)
for p in pecas:
    p.possible_moves(check)

while game_loop:
    tela.fill('black')
    if game_state == "menu":
        game_loop, game_state = menu.draw()
    elif game_state == "options":
        show_possible_moves, game_state = menu.options(show_possible_moves)
    elif game_state == "game":
        desenha_tela(tabuleiro)
        if not has_ia:
            white_turn, peca, pecas, movimentos_validos, sel = player(jogo, tabuleiro, white_turn, peca, pecas, movimentos_validos, sel)
        else:
            if player_is_white == white_turn:
                white_turn, peca, pecas, movimentos_validos, sel = player(jogo, tabuleiro, white_turn, peca, pecas, movimentos_validos, sel)
            else:
                ai_player.set_next_move()
                peca, move = ai_player.next_move
                # peca, move = ai.minimaxRoot(3, tabuleiro, False)
                peca.move(move)
                white_turn, pecas = end_turn(jogo, tabuleiro, white_turn)

    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
