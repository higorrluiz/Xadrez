from typing import Type
from classes.board import Board
from classes.pawn import Pawn
from classes.piece import Piece
from classes.queen import Queen
from classes.rook import Rook
from classes.knight import Knight


class Match:

    def __init__(self, board: Type[Board]) -> None:
        board.match = self
        self.board = board
        self.cont = 0
        # peca branca que pode ser capturada pelo en passant
        self.passant_white: Pawn = None
        # peca preta que pode ser capturada pelo en passant
        self.passant_black: Pawn = None
    
    def set_cont_zero(self) -> None:
        self.cont = 0

    def increment_cont(self) -> None:
        self.cont += 1

    def decrement_cont(self) -> None:
        self.cont -= 1
    
    # 
    # metodos de condicao de fim de partida
    # 

    def is_draw(self, is_white: bool, check: bool) -> bool:
        if self.cont == 50: return True  # checa regra dos 50 movimentos
        if self._is_stalemate(is_white, check): return True
        if self._insufficient_material(): return True
        return False

    def _is_stalemate(self, is_white: bool, check: bool) -> bool:
        if check: return False
        pieces: list[Piece] = self.board.get_pieces(is_white)
        for piece in pieces:
            if piece.get_moves(): return False
        return True
    
    def _insufficient_material(self) -> bool:  # K - KN - KB - KNN
        for is_white in [False, True]:
            knights = 0
            pieces: list[Piece] = self.board.get_pieces(is_white)
            if len(pieces) >= 4: return False 
            for piece in pieces:
                if isinstance(piece, Queen): return False
                if isinstance(piece, Rook): return False
                if isinstance(piece, Pawn): return False
                if isinstance(piece, Knight): knights += 1
            if len(pieces) == 3 and knights != 2: return False
        return True
