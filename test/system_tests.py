import time
import os
import pygame
import sys
from datetime import datetime

# getting the name of the directory where the this file is present
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present
parent = os.path.dirname(current)
# adding the parent directory to the sys.path
sys.path.append(parent)

from classes.board import Board
from classes.match import Match
from ai import ChessPlayer


def main():
    print("TESTES DE SISTEMA")
    print("Teste de sistema 1: IA no cenário inicial com profundidade 1")
    tela = pygame.surface.Surface((800, 800))
    tam = 100
    board = Board(tela, tam)
    board.match = Match(board)
    ia = ChessPlayer(True, board.match, board, 1)
    start_time = datetime.now()
    pecas = board.get_pieces(True)
    for peca in pecas:
        peca.possible_moves(False)
    ia.set_next_move()
    end_time = datetime.now()
    print('Duração: {}'.format(end_time - start_time))
    print("Teste de sistema 2: IA no cenário inicial com profundidade 2")
    ia = ChessPlayer(True, board.match, board, 2)
    pecas = board.get_pieces(True)
    for peca in pecas:
        peca.possible_moves(False)
    start_time = datetime.now()
    ia.set_next_move()
    end_time = datetime.now()
    print('Duração: {}'.format(end_time - start_time))
    print("Teste de sistema 3: IA no cenário inicial com profundidade 3")
    ia = ChessPlayer(True, board.match, board, 3)
    start_time = datetime.now()
    ia.set_next_move()
    end_time = datetime.now()
    print('Duração: {}'.format(end_time - start_time))
    print("Teste de sistema 4: IA no cenário inicial com profundidade 4")
    ia = ChessPlayer(True, board.match, board, 4)
    start_time = datetime.now()
    ia.set_next_move()
    end_time = datetime.now()
    print('Duração: {}'.format(end_time - start_time))
    # Profundidade 5: 3min 55s
    # print("Teste de sistema 5: IA no cenário inicial com profundidade 5")
    # ia = ChessPlayer(True, board.match, board, 5)
    # start_time = datetime.now()
    # ia.set_next_move()
    # end_time = datetime.now()
    # print('Duração: {}'.format(end_time - start_time))


if __name__ == "__main__":
    main()