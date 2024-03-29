from time import sleep
import pygame 
from pygame.locals import *
from sys import exit
from classes.piece import Piece
from classes.pawn import Pawn
from classes.queen import Queen
from classes.king import King
from classes.board import Board
from classes.match import Match
from helper import *
from importador import *
from menu import Menu
from ai import ChessPlayer


def get_config(arq: str) -> tuple[list[bool], int]:
    handle = open(arq, 'r')
    linhas = handle.readlines()
    handle.close()

    config = linhas[11:12][0].strip()
    config = [(char == 'T') for char in config]

    ia_difficulty = int(linhas[12:13][0].strip())

    # deleta estado retomado
    open(arq, 'w').close()
    return (config, ia_difficulty)


def desenha_tela(tabuleiro: Board) -> None:
    tabuleiro.desenhar_tabuleiro()
    tabuleiro.black_group.draw(tela)
    tabuleiro.black_group.update()
    tabuleiro.white_group.draw(tela)
    tabuleiro.white_group.update()


def end_turn() -> tuple[bool, list[Piece], str, str]:
    global game_state, jogo, tabuleiro, white_turn, pecas, white_check, black_check, winner, end
    if white_turn:
        jogo.passant_black = None
    else:
        jogo.passant_white = None

    white_turn = not white_turn

    check = jogo.king_is_checked(white_turn)
    if check:
        if white_turn: white_check = True
        else: black_check = True
    pecas = tabuleiro.get_pieces(white_turn)
    for p in pecas:
        p.possible_moves(check)

    if jogo.is_checkmate(white_turn, check):
        game_state = "checkmate"
        menu.game_state = game_state
        winner = "black" if white_turn else "white"
        end = True
    if jogo.is_tie(white_turn, check):
        game_state = "tie"
        menu.game_state = game_state
        end = True
    desenha_tela(tabuleiro)


def player() -> None:
    global game_state, menu, jogo, tabuleiro, white_turn, check, has_ia, player_is_white, ia_difficulty, peca, pecas, \
        movimentos_validos, sel, old_pos, new_pos, w_king_pos, b_king_pos, white_check, black_check, winner, end
    
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()

        if (event.type == botao_exit) or (event.type == QUIT):
            tabuleiro.save_state(STATE_PATH, [white_turn, check, has_ia, player_is_white], ia_difficulty)
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
                    movimentos_validos = peca.get_moves()
                    movimentos_validos = [POSICOES_TABULEIRO_LISTA[x][y] for (x, y) in movimentos_validos]

            # se a peca esta selecionada e o usuario clica em outro quadrado
            if peca.selecionado == True and not (peca.rect.collidepoint(mouse_pos)):
                x, y = posicao_do_quadrado()
                sel = mouse_pos
                if (x, y) in movimentos_validos:
                    old_pos = peca.get_pos()
                    peca.move((7-round(y/TAMANHO), round(x/TAMANHO)))
                    new_pos = peca.get_pos()
                    
                    white_check = black_check = False
                    if isinstance(peca, King):
                        if white_turn: w_king_pos = new_pos
                        else: b_king_pos = new_pos

                    peca.selecionado = False
                    movimentos_validos = []
                    if isinstance(peca, Pawn) and peca.get_row() in [0, 7]: 
                        menu.promotion(peca, white_turn)
                    end_turn()

    if show_possible_moves:
        for (x, y) in movimentos_validos:
            pygame.draw.circle(tela, (207,14,14), (x+TAMANHO/2, y+TAMANHO/2), 10)
    selecionado(sel)
    if old_pos is not None:
        selecionado_cor(old_pos, (0, 255, 255))
        selecionado_cor(new_pos, (0, 255, 255))
    if white_check: selecionado_cor(w_king_pos, (255, 0, 0))
    if black_check: selecionado_cor(b_king_pos, (255, 0, 0))


game_loop = True
game_state = "menu"
menu = Menu(tela, game_loop, game_state)
show_possible_moves = True
player_is_white = True
ia_toggled = False
ia_difficulty = 0
end = False

while game_loop:
    if end: 
        sleep(2)
        end = False
    tela.fill('black')
    if game_state == "menu":
        game_loop, game_state = menu.draw()
    elif game_state == "options":
        show_possible_moves, game_state = menu.options(show_possible_moves)
    elif game_state == "checkmate":
        game_loop, game_state = menu.checkmate(winner)
    elif game_state == "tie":
        game_loop, game_state = menu.tie()
    elif game_state == "continue_game":
        sel = (20000, 30000)
        old_pos = new_pos = None
        w_king_pos = (0, 4)
        b_king_pos = (7, 4)
        white_check = black_check = False

        tabuleiro: Board = Board(tela, TAMANHO, STATE_PATH)
        jogo: Match = Match(tabuleiro, STATE_PATH)
        peca: Piece = Piece()
        (white_turn, check, has_ia, player_is_white), ia_difficulty = get_config(STATE_PATH)
        movimentos_validos = []

        if has_ia: ai_player = ChessPlayer(not player_is_white, jogo, tabuleiro, ia_difficulty)
        pecas = tabuleiro.get_pieces(white_turn)
        for p in pecas:
            p.possible_moves(check)
        game_state = "game"
    elif game_state == "mode_selection":
        game_state, ia_toggled, ia_difficulty = menu.mode_selection(ia_toggled)
    elif game_state == "side_selection":
        game_state, player_is_white = menu.side_selection()
    elif game_state == "new_game":
        # deleta estado salvo
        open(STATE_PATH, 'w').close()

        sel = (20000, 30000)
        old_pos = new_pos = None
        w_king_pos = (0, 4)
        b_king_pos = (7, 4)
        white_check = black_check = False

        tabuleiro: Board = Board(tela, TAMANHO)
        jogo: Match = Match(tabuleiro)
        peca: Piece = Piece()
        white_turn = True
        check = False
        has_ia = ia_toggled
        movimentos_validos = []

        if has_ia: ai_player = ChessPlayer(not player_is_white, jogo, tabuleiro, ia_difficulty)
        pecas = tabuleiro.get_pieces(white_turn)
        for p in pecas:
            p.possible_moves(check)
        game_state = "game"
        ia_toggled = False

    elif game_state == "game":
        desenha_tela(tabuleiro)
        if not has_ia: player()
        else:
            if player_is_white == white_turn:
                player()
            else:
                ai_player.set_next_move()
                peca, move = ai_player.get_next_move()
                old_pos = peca.get_pos()
                peca.move(move)
                new_pos = peca.get_pos()

                white_check = black_check = False
                if isinstance(peca, King):
                    if white_turn: w_king_pos = new_pos
                    else: b_king_pos = new_pos

                if isinstance(peca, Pawn) and (peca.get_row() in [0, 7]):
                    peca.promote(Queen(peca.get_pos_str(), peca.get_is_white()))
                end_turn()

    pygame.display.flip()

    # Setting FPS
    clock.tick(60)
    pygame.display.update()
