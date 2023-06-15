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


class ChessPlayer():
    def __init__(self, color, match, board, depth):
        self.color = color
        self.match = match
        self.board = board
        self.depth = depth
        self.moves = None
        self.pieces = None
        self.next_move = None

    def player_moves(self):
        self.pieces = self.board.get_pieces(self.color)
        self.moves = []
        for p in self.pieces:
            for move in p.get_moves():
                self.moves.append([p, move])

    def set_next_move(self):
        self.__minimaxRoot()

    def __minimaxRoot(self):
        best_move = None
        if self.color:
            best_move = -9999
        else:
            best_move = 9999
        bestMoveFinal = None
        value = 0
        self.player_moves()
        for x in range(len(self.moves)):
            piece = self.moves[x][0]
            move = self.moves[x][1]
            this_move = [piece, move]
            matrix = [row[:] for row in self.board.matrix]
            white = self.board.white[:]
            black = self.board.black[:]
            column = piece.get_column()
            row = piece.get_row()
            peca_atacada = self.board.get_piece(move)
            if peca_atacada is not None:
                self.board._Board__delete_piece(move)
            piece.row = move[0]
            piece.column = move[1]
            if self.color:
                value = max(best_move, self.__minimax(self.depth - 1, self.board, -10000, 10000, not self.color))
            else:
                value = min(best_move, self.__minimax(self.depth - 1, self.board, -10000, 10000, not self.color))
            piece.column = column
            piece.row = row
            if peca_atacada is not None:
                peca_atacada.row = move[0]
                peca_atacada.column = move[1]
                self.board._Board__add_piece(peca_atacada, move)
            self.board.white = white
            self.board.black = black
            self.board.matrix = matrix
            if (value < best_move):
                best_move = value
                bestMoveFinal = this_move
        self.next_move = bestMoveFinal

    def __minimax(self, depth, board, alpha, beta, is_maximizing):
        if (depth == 0):
            return self.__evaluation()
        self.player_moves()
        best_move = None
        if is_maximizing:
            best_move = beta
        else:
            best_move = alpha
        for x in range(len(self.moves)):
            piece = self.moves[x][0]
            move = self.moves[x][1]
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
            if (is_maximizing):
                best_move = min(best_move, self.__minimax(depth - 1, board, alpha, beta, not is_maximizing))
            else:
                best_move = max(best_move, self.__minimax(depth - 1, board, alpha, beta, not is_maximizing))
            piece.column = column
            piece.row = row
            if peca_atacada is not None:
                peca_atacada.row = move[0]
                peca_atacada.column = move[1]
                board._Board__add_piece(peca_atacada, move)
            board.white = white
            board.black = black
            board.matrix = matrix
            if (is_maximizing):
                alpha = max(alpha, best_move)
                if beta <= alpha:
                    return alpha
            else:
                beta = min(beta, best_move)
                if (beta <= alpha):
                    return beta
        return best_move

    def __evaluation(self):
        white_eval = self.__get_white_player_eval()
        black_eval = self.__get_black_player_eval()
        return white_eval - black_eval

    def __get_white_player_eval(self):
        eval = 0
        pecas = self.board.get_pieces(True)
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

    def __get_black_player_eval(self):
        eval = 0
        pecas = self.board.get_pieces(False)
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
