from math import inf
from classes.match import Match
from classes.board import Board
from classes.piece import Piece
from classes.pawn import Pawn
from classes.rook import Rook
from classes.bishop import Bishop
from classes.queen import Queen
from classes.knight import Knight
from classes.king import King
import evaluation as EVAL


class ChessPlayer():
    def __init__(self, color: bool, match: Match, board: Board, depth: int) -> None:
        self.color = color
        self.match = match
        self.board = board
        self.depth = depth
        self.next_move = None

    def get_next_move(self) -> tuple[Piece, tuple[int, int]]:
        return self.next_move

    def player_moves(self, color: bool, recalculate: bool) -> list[tuple[Piece, tuple[int, int]]]:
        self.pieces = self.board.get_pieces(color)
        moves = []
        for p in self.pieces:
            if recalculate: p.possible_moves(True)
            for move in p.get_moves():
                moves.append((p, move))
        return moves

    def set_next_move(self) -> None:
        self.__minimaxRoot()

    def __minimaxRoot(self) -> None:
        best_move = -inf if self.color else inf
        bestMoveFinal = None
        value = 0
        possible_moves = self.player_moves(self.color, False)
        for piece, move in possible_moves:
            this_move = (piece, move)
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            castle_flag = False
            if (isinstance(piece, King) or isinstance(piece, Rook)):
                old_state['piece_moved'] = piece.get_moved()
                if isinstance(piece, King) and abs(piece.get_column() - move[1]) > 1:
                    castle_flag = True
                    rook_column = 0 if (piece.get_column() == 2) else 7
                    rook = self.board.get_piece((move[0], rook_column))
                    old_state['rook_pos'] = rook.get_pos()

            piece.move(move, mock=True)
            if self.board.get_king(not piece.get_is_white()) is None: return inf if self.color else -inf
            if isinstance(piece, Pawn) and (move[0] in [0, 7]):
                piece.promote(Queen(piece.get_pos_str(), piece.get_is_white()), mock=True)

            if self.color:
                value = max(best_move, self.__minimax(self.depth - 1, not self.color))
            else:
                value = min(best_move, self.__minimax(self.depth - 1, not self.color))
            
            self._load_state(old_state)
            piece.row = old_state['row']
            piece.column = old_state['column']
            if (isinstance(piece, King) or isinstance(piece, Rook)):
                piece.moved = old_state['piece_moved']
                if castle_flag:
                    pos = old_state['rook_pos']
                    rook.row = pos[0]
                    rook.column = pos[1]
            
            if (not self.color and (value < best_move)) or (self.color and (value > best_move)):
                best_move = value
                bestMoveFinal = this_move
        self.next_move = bestMoveFinal

    def __minimax(self, depth: int, is_maximizing: bool) -> float:
        if (depth == 0):
            return self.__evaluation()
        possible_moves = self.player_moves(is_maximizing, True)
        if len(possible_moves) == 0:
            if self.match.king_is_checked(is_maximizing): return -inf if is_maximizing else inf
            else: return 0
        best_move = -inf if is_maximizing else inf
        for piece, move in possible_moves:
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            castle_flag = False
            if (isinstance(piece, King) or isinstance(piece, Rook)):
                old_state['piece_moved'] = piece.get_moved()
                if isinstance(piece, King) and abs(piece.get_column() - move[1]) > 1:
                    castle_flag = True
                    rook_column = 0 if (piece.get_column() == 2) else 7
                    rook = self.board.get_piece((move[0], rook_column))
                    old_state['rook_pos'] = rook.get_pos()
            
            piece.move(move, mock=True)
            if self.board.get_king(not piece.is_white) is None: return inf if is_maximizing else -inf
            if isinstance(piece, Pawn) and (move[0] == 0 or move[0] == 7):
                piece.promote(Queen(piece.get_pos_str(), self.color), mock=True)

            if (is_maximizing):
                best_move = max(best_move, self.__minimax(depth - 1, not is_maximizing))
            else:
                best_move = min(best_move, self.__minimax(depth - 1, not is_maximizing))
            
            self._load_state(old_state)
            piece.row = old_state['row']
            piece.column = old_state['column']
            if (isinstance(piece, King) or isinstance(piece, Rook)):
                piece.moved = old_state['piece_moved']
                if castle_flag:
                    pos = old_state['rook_pos']
                    rook.row = pos[0]
                    rook.column = pos[1]
        return best_move

    def __evaluation(self) -> float:
        white_eval = self.__get_white_player_eval()
        black_eval = self.__get_black_player_eval()
        return white_eval - black_eval

    def __get_white_player_eval(self) -> float:
        eval = 0
        pecas = self.board.get_pieces(True)
        for piece in pecas:
            piece_row, piece_col = piece.get_pos()
            if isinstance(piece, Pawn):
                eval = eval + 10 + EVAL.white_pawn[piece_row][piece_col]
            if isinstance(piece, Bishop):
                eval = eval + 30 + EVAL.white_bishop[piece_row][piece_col]
            if isinstance(piece, Knight):
                eval = eval + 30 + EVAL.white_knight[piece_row][piece_col]
            if isinstance(piece, Rook):
                eval = eval + 50 + EVAL.white_rook[piece_row][piece_col]
            if isinstance(piece, Queen):
                eval = eval + 90 + EVAL.queen[piece_row][piece_col]
            if isinstance(piece, King):
                eval = eval + 900 + EVAL.white_king[piece_row][piece_col]
        return eval

    def __get_black_player_eval(self) -> float:
        eval = 0
        pecas = self.board.get_pieces(False)
        for piece in pecas:
            piece_row, piece_col = piece.get_pos()
            if isinstance(piece, Pawn):
                eval = eval + 10 + EVAL.black_pawn[piece_row][piece_col]
            if isinstance(piece, Bishop):
                eval = eval + 30 + EVAL.black_bishop[piece_row][piece_col]
            if isinstance(piece, Knight):
                eval = eval + 30 + EVAL.black_knight[piece_row][piece_col]
            if isinstance(piece, Rook):
                eval = eval + 50 + EVAL.black_rook[piece_row][piece_col]
            if isinstance(piece, Queen):
                eval = eval + 90 + EVAL.queen[piece_row][piece_col]
            if isinstance(piece, King):
                eval = eval + 900 + EVAL.black_king[piece_row][piece_col]
        return eval

    def _load_state(self, state_dict: dict) -> None:
        self.board.matrix = state_dict['matrix']
        self.board.white = state_dict['white']
        self.board.black = state_dict['black']
        self.match.passant_white = state_dict['passant_w']
        self.match.passant_black = state_dict['passant_b']
