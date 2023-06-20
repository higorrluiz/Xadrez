from typing import Type
from classes.board import Board
from classes.piece import Piece
from classes.pawn import Pawn
from classes.rook import Rook
from classes.bishop import Bishop
from classes.queen import Queen
from classes.knight import Knight
from classes.king import King


class Match:

    def __init__(self, board: Type[Board]) -> None:
        board.match = self
        self.board = board
        self.cont = 0
        # peca branca que pode ser capturada pelo en passant
        self.passant_white: Pawn = None
        # peca preta que pode ser capturada pelo en passant
        self.passant_black: Pawn = None

    def get_cont(self) -> None:
        return self.cont 
    
    def set_cont_zero(self) -> None:
        self.cont = 0

    def increment_cont(self) -> None:
        self.cont += 1

    def decrement_cont(self) -> None:
        self.cont -= 1
    
    def king_is_checked(self, is_white: bool) -> bool:
        king: King = self.board.get_king(is_white)
        if self._checked_from_diagonal(king): return True
        if self._checked_from_line(king): return True
        if self._checked_by_knight(king): return True
        if self._checked_by_pawn(king): return True
        if self._king_is_blocking(king): return True
        return False
    
    def discovered_check(self, is_white: bool) -> bool:
        king: King = self.board.get_king(is_white)
        if self._checked_from_diagonal(king): return True
        if self._checked_from_line(king): return True
        return False
    
    def is_checkmate(self, is_white: bool, check: bool) -> bool:
        if not check: return False
        pieces: list[Piece] = self.board.get_pieces(is_white)
        for piece in pieces:
            if piece.get_moves(): return False
        return True

    def _checked_by_knight(self, king: King) -> bool:
        linha, coluna = king.get_pos()

        # movimento em L (para cima e direita)
        aux_linha = linha + 2
        aux_coluna = coluna + 1
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha <= 7 and aux_coluna <= 7 and isinstance(piece, Knight)):
            return True

        # movimento em L (para cima e esquerda)
        aux_linha = linha + 2
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha <= 7 and aux_coluna >= 0 and isinstance(piece, Knight)):
            return True

        # movimento em L (para baixo e direita)
        aux_linha = linha - 2
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha >= 0 and aux_coluna <= 7 and isinstance(piece, Knight)):
            return True

        # movimento em L (para baixo e esquerda)
        aux_linha = linha - 2
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0 and isinstance(piece, Knight)):
            return True

        # movimento em L (para direita e cima)
        aux_linha = linha + 1
        aux_coluna = coluna + 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha <= 7 and aux_coluna <= 7 and isinstance(piece, Knight)):
            return True

        # movimento em L (para direita e baixo)
        aux_linha = linha - 1
        aux_coluna = coluna + 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha >= 0 and aux_coluna <= 7 and isinstance(piece, Knight)):
            return True

        # movimento em L (para esquerda e cima)
        aux_linha = linha + 1
        aux_coluna = coluna - 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha <= 7 and aux_coluna >= 0 and isinstance(piece, Knight)):
            return True

        # movimento em L (para esquerda e baixo)
        aux_linha = linha - 1
        aux_coluna = coluna - 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != king.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0 and isinstance(piece, Knight)):
            return True
        
        return False


    def _checked_from_diagonal(self, king: King) -> bool:
        linha, coluna = king.get_pos()

        # movimentos para diagonal 1 (cima e esquerda)
        aux_linha = linha + 1
        aux_coluna = coluna - 1
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7 and aux_coluna >= 0:
            aux_linha += 1
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Bishop) or isinstance(piece, Queen):
                    return True
        
        # movimentos para diagonal 2 (cima e direita)
        aux_linha = linha + 1
        aux_coluna = coluna + 1 
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7 and aux_coluna <= 7:
            aux_linha += 1
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Bishop) or isinstance(piece, Queen):
                    return True

        # movimentos para diagonal 3 (baixo e esquerda)
        aux_linha = linha - 1
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0 and aux_coluna >= 0:
            aux_linha -= 1
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Bishop) or isinstance(piece, Queen):
                    return True

        # movimentos para diagonal 4 (baixo e direita)
        aux_linha = linha - 1
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0 and aux_coluna <= 7:
            aux_linha -= 1
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Bishop) or isinstance(piece, Queen):
                    return True
        
        return False
        
        

    def _checked_from_line(self, king: King) -> bool:
        linha, coluna = king.get_pos()

        # movimentos para cima
        aux_linha = linha + 1
        aux_coluna = coluna
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7:
            aux_linha += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Rook) or isinstance(piece, Queen):
                    return True
        
        
        # movimentos para baixo
        aux_linha = linha - 1
        aux_coluna = coluna
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0:
            aux_linha -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Rook) or isinstance(piece, Queen):
                    return True

        # movimentos para direita
        aux_linha = linha
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_coluna <= 7:
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Rook) or isinstance(piece, Queen):
                    return True

        # movimentos para esquerda
        aux_linha = linha
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_coluna >= 0:
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None:
            if piece.is_white != king.is_white:
                if isinstance(piece, Rook) or isinstance(piece, Queen):
                    return True        
        return False

    def _checked_by_pawn(self, king: King) -> bool:
        linha, coluna = king.get_pos()
        if king.is_white:
            aux_linha = linha + 1
            aux_coluna = coluna + 1
            piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
            if piece is not None and not piece.is_white and isinstance(piece, Pawn):
                return True
            
            aux_coluna = coluna - 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            if piece is not None and not piece.is_white and isinstance(piece, Pawn):
                return True
            
            return False
        else:
            aux_linha = linha - 1
            aux_coluna = coluna + 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            if piece is not None and piece.is_white and isinstance(piece, Pawn):
                return True
            
            aux_coluna = coluna - 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            if piece is not None and piece.is_white and isinstance(piece, Pawn):
                return True
            
            return False
        
    def _king_is_blocking(self, king: King) -> bool:
        linha, coluna = king.get_pos()
        for aux_linha in range(-1,2):
            for aux_coluna in range(-1,2):
                piece: Piece = self.board.get_piece((linha + aux_linha, coluna + aux_coluna))
                if piece is not None and piece.is_white != king.is_white and isinstance(piece, King):
                    return True
        return False

    def is_tie(self, is_white: bool, check: bool) -> bool:
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
    
    def _insufficient_material(self) -> bool:  # K - KN - KB
        for is_white in [False, True]:
            pieces: list[Piece] = self.board.get_pieces(is_white)
            if len(pieces) >= 3: return False 
            for piece in pieces:
                if isinstance(piece, Queen): return False
                if isinstance(piece, Rook): return False
                if isinstance(piece, Pawn): return False
        return True
