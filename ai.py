# import chess
# import sunfish
# import math
import random
import sys

from classes.piece import Piece
from classes.pawn import Pawn
from classes.rook import Rook
from classes.bishop import Bishop
from classes.queen import Queen
from classes.knight import Knight
from classes.king import King
from classes.match import Match
from board_helper import *
import evaluation as EVAL



def player_moves(board, is_white):
    pecas = board.get_pieces(is_white)
    possible_moves = []
    for p in pecas:
        for move in p.get_moves():
            possible_moves.append([p, move])
    return possible_moves


def ai_move(board, is_white):
    possible_moves = player_moves(board, is_white)
    random_move = possible_moves[random.randint(0, len(possible_moves)-1)]
    return random_move


def minimaxRoot(depth, board, is_maximizing):
    bestMove = 9999
    bestMoveFinal = None
    possible_moves = player_moves(board, is_maximizing)
    for x in range(len(possible_moves)):
        piece = possible_moves[x][0]
        move = possible_moves[x][1]
        this_move = [piece, move]
        matrix = [row[:] for row in board.matrix]
        white = board.white[:]
        black = board.black[:]
        column = piece.get_column()
        row = piece.get_row()
        peca_atacada = board.get_piece(move)
        if peca_atacada is not None:
            board._Board__delete_piece(move)
        piece.row = move[0]
        piece.column = move[1]
        value = min(bestMove, minimax(depth - 1, board, -10000, 10000, not is_maximizing))
        piece.column = column
        if peca_atacada is not None:
            peca_atacada.row = move[0]
            peca_atacada.column = move[1]
            board._Board__add_piece(peca_atacada, move)
        piece.row = row
        board.white = white
        board.black = black
        board.matrix = matrix
        if (value < bestMove):
            bestMove = value
            bestMoveFinal = this_move
    return bestMoveFinal


def minimax(depth, board, alpha, beta, is_maximizing):
    if (depth == 0):
        return evaluation(board)
    possible_moves = player_moves(board, is_maximizing)
    # zerado porque?

    if (is_maximizing):
        bestMove = beta
        for x in range(len(possible_moves)):
            piece = possible_moves[x][0]
            move = possible_moves[x][1]
            matrix = [row[:] for row in board.matrix]
            white = board.white[:]
            black = board.black[:]
            column = piece.get_column()
            row = piece.get_row()
            peca_atacada = board.get_piece(move)
            piece.row = move[0]
            piece.column = move[1]
            bestMove = min(bestMove, minimax(depth - 1, board, alpha, beta, not is_maximizing))
            piece.column = column
            if peca_atacada is not None:
                peca_atacada.row = move[0]
                peca_atacada.column = move[1]
                board._Board__add_piece(peca_atacada, move)
            piece.row = row
            board.white = white
            board.black = black
            board.matrix = matrix
            alpha = max(alpha, bestMove)
            if beta <= alpha:
                break
        return bestMove
    else:
        bestMove = alpha
        for x in range(len(possible_moves)):
            piece = possible_moves[x][0]
            move = possible_moves[x][1]

            matrix = [row[:] for row in board.matrix]
            white = board.white[:]
            black = board.black[:]

            column = piece.get_column()
            row = piece.get_row()
            peca_atacada = board.get_piece(move)
            piece.row = move[0]
            piece.column = move[1]

            bestMove = max(bestMove, minimax(depth - 1, board, alpha, beta, not is_maximizing))
            piece.column = column
            if peca_atacada is not None:
                peca_atacada.row = move[0]
                peca_atacada.column = move[1]
                board._Board__add_piece(peca_atacada, move)
            piece.row = row
            board.white = white
            board.black = black
            board.matrix = matrix
            beta = min(beta, bestMove)
            if (beta <= alpha):
                break
        return bestMove


def evaluation(board):
    white_eval = get_white_player_eval(board)
    black_eval = get_black_player_eval(board)
    return white_eval - black_eval


def get_white_player_eval(board):
    eval = 0
    pecas = board.get_pieces(True)
    for piece in pecas:
        piece_col = piece.get_column()
        piece_row = piece.get_row()
        if isinstance(piece, Pawn):
            eval = eval + 10 + EVAL.white_pawn[piece_row][piece_col]
        if isinstance(piece, Bishop):
            eval = eval + 30 + EVAL.white_bishop[piece_row][piece_col]
        if isinstance(piece, Knight):
            eval = eval + 30 + EVAL.knight[piece_row][piece_col]
        if isinstance(piece, Rook):
            eval = eval + 50 + EVAL.white_rook[piece_row][piece_col]
        if isinstance(piece, Queen):
            eval = eval + 90 + EVAL.queen[piece_row][piece_col]
        if isinstance(piece, King):
            eval = eval + 900 + EVAL.white_king[piece_row][piece_col]
    return eval


def get_black_player_eval(board):
    eval = 0
    pecas = board.get_pieces(False)
    for piece in pecas:
        piece_col = piece.get_column()
        piece_row = piece.get_row()
        if isinstance(piece, Pawn):
            eval = eval + 10 + EVAL.white_pawn[piece_row][piece_col]
        if isinstance(piece, Bishop):
            eval = eval + 30 + EVAL.black_bishop[piece_row][piece_col]
        if isinstance(piece, Knight):
            eval = eval + 30 + EVAL.knight[piece_row][piece_col]
        if isinstance(piece, Rook):
            eval = eval + 50 + EVAL.black_rook[piece_row][piece_col]
        if isinstance(piece, Queen):
            eval = eval + 90 + EVAL.queen[piece_row][piece_col]
        if isinstance(piece, King):
            eval = eval + 900 + EVAL.black_king[piece_row][piece_col]
    return eval
