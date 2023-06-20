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
        self.next_move = None

    def player_moves(self, color):
        self.pieces = self.board.get_pieces(color)
        moves = []
        for p in self.pieces:
            for move in p.get_moves():
                moves.append([p, move])
        return moves

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
        print(self.color)
        possible_moves = self.player_moves(self.color)
        for x in range(len(possible_moves)):
            piece = possible_moves[x][0]
            move = possible_moves[x][1]
            this_move = [piece, move]
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            piece.move(move, mock=True)
            

            if self.color:
                value = max(best_move, self.__minimax(self.depth - 1, self.board, -10000, 10000, not self.color))
            else:
                value = min(best_move, self.__minimax(self.depth - 1, self.board, -10000, 10000, not self.color))

            self._load_state(old_state)
            piece.column = old_state['column']
            piece.row = old_state['row']
            if (value < best_move):
                best_move = value
                bestMoveFinal = this_move
        print(value, bestMoveFinal)
        self.next_move = bestMoveFinal

    def __minimax(self, depth, board, alpha, beta, is_maximizing):
        if (depth == 0):
            return self.__evaluation()
        best_move = None
        possible_moves = self.player_moves(is_maximizing)
        if len(possible_moves) == 0:
            if self.match.king_is_checked(is_maximizing):
                best_move = -9999
                if not is_maximizing:
                    best_move = 9999
                return best_move
            else:
                return 0
        if is_maximizing:
            best_move = beta
        else:
            best_move = alpha
        for x in range(len(possible_moves)):
            piece = possible_moves[x][0]
            move = possible_moves[x][1]
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            self.board.printa()
            piece.move(move, mock=True)

            #  promoção 

            if (is_maximizing):
                best_move = min(best_move, self.__minimax(depth - 1, board, alpha, beta, not is_maximizing))
            else:
                best_move = max(best_move, self.__minimax(depth - 1, board, alpha, beta, not is_maximizing))
            piece.column = old_state['column']
            piece.row = old_state['row']
            self._load_state(old_state)
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
        print(white_eval - black_eval)
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


    def _load_state(self, state_dict):
        self.board.matrix = [row[:] for row in state_dict['matrix']]
        self.board.white = state_dict['white'][:]
        self.board.black = state_dict['black'][:]
        self.match.passant_white = state_dict['passant_w']
        self.match.passant_black = state_dict['passant_b']
