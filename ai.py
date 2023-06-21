
from classes.pawn import Pawn
from classes.rook import Rook
from classes.bishop import Bishop
from classes.queen import Queen
from classes.knight import Knight
from classes.king import King
import evaluation as EVAL


class ChessPlayer():
    def __init__(self, color, match, board, depth):
        self.color = color
        self.match = match
        self.board = board
        self.depth = depth
        self.next_move = None

    def player_moves(self, color: bool, recalculate: bool):
        self.pieces = self.board.get_pieces(color)
        moves = []
        for p in self.pieces:
            if recalculate:
                p.possible_moves(True)
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
        possible_moves = self.player_moves(self.color, False)
        for x in range(len(possible_moves)):
            promote_flag = False
            piece = possible_moves[x][0]
            move = possible_moves[x][1]
            this_move = [piece, move]
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            old_state['str_pos'] = piece.get_pos_str()
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            if isinstance(piece, Pawn) and (move[0] == 0 or move[0] == 7):
                old_state['pawn'] = piece
                piece.move(move, mock=True)
                promote_flag = True
                piece.promote(Queen(piece.get_pos_str(), self.color))
            else:
                piece.move(move, mock=True)
            if self.color:
                value = max(best_move, self.__minimax(self.depth - 1, self.board, not self.color))
            else:
                value = min(best_move, self.__minimax(self.depth - 1, self.board, not self.color))
            if promote_flag:
                self.board._Board__delete_piece(move)
                self._load_state(old_state)
                piece.row = old_state['row']
                piece.column = old_state['column']
                if self.color == True:
                    self.board.white_group.add(old_state['pawn'])
                else:
                    self.board.black_group.add(old_state['pawn'])
            else:
                self._load_state(old_state)
                piece.row = old_state['row']
                piece.column = old_state['column']
            if (value < best_move):
                best_move = value
                bestMoveFinal = this_move
        self.next_move = bestMoveFinal

    def __minimax(self, depth, board, is_maximizing):
        if (depth == 0):
            return self.__evaluation()
        best_move = None
        possible_moves = self.player_moves(is_maximizing, True)
        if len(possible_moves) == 0:
            if self.match.king_is_checked(is_maximizing):
                best_move = -9999
                if not is_maximizing:
                    best_move = 9999
                return best_move
            else:
                return 0
        if is_maximizing:
            best_move = 9999
        else:
            best_move = -9999
        for x in range(len(possible_moves)):
            promote_flag = False
            piece = possible_moves[x][0]
            move = possible_moves[x][1]
            old_state = {}
            old_state['matrix'] = [row[:] for row in self.board.matrix]
            old_state['white'] = self.board.white[:]
            old_state['black'] = self.board.black[:]
            old_state['column'] = piece.get_column()
            old_state['row'] = piece.get_row()
            old_state['str_pos'] = piece.get_pos_str()
            old_state['passant_w'] = self.match.passant_white
            old_state['passant_b'] = self.match.passant_black
            if isinstance(piece, Pawn) and (move[0] == 0 or move[0] == 7):
                old_state['pawn'] = piece
                piece.move(move, mock=True)
                promote_flag = True
                piece.promote(Queen(piece.get_pos_str(), self.color))
            else:
                piece.move(move, mock=True)
            if (is_maximizing):
                best_move = min(best_move, self.__minimax(depth - 1, board, not is_maximizing))
            else:
                best_move = max(best_move, self.__minimax(depth - 1, board, not is_maximizing))
            if promote_flag:
                self.board._Board__delete_piece(move)
                self._load_state(old_state)
                piece.row = old_state['row']
                piece.column = old_state['column']
                if is_maximizing:
                    self.board.white_group.add(old_state['pawn'])
                else:
                    self.board.black_group.add(old_state['pawn'])
            else:
                self._load_state(old_state)
                piece.row = old_state['row']
                piece.column = old_state['column']
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

    def _load_state(self, state_dict):
        self.board.matrix = [row[:] for row in state_dict['matrix']]
        self.board.white = state_dict['white'][:]
        self.board.black = state_dict['black'][:]
        self.match.passant_white = state_dict['passant_w']
        self.match.passant_black = state_dict['passant_b']
