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

    def __init__(self, board: Type[Board], arq: str = None) -> None:
        board.match = self
        self.board = board
        if arq is None:
            self.cont = 0
            # peca branca que pode ser capturada pelo en passant
            self.passant_white: Pawn = None
            # peca preta que pode ser capturada pelo en passant
            self.passant_black: Pawn = None
        else:
            handle = open(arq, 'r')
            linhas = handle.readlines()
            handle.close()

            passant = linhas[9:10]
            cont = linhas[10:11]

            if passant[:2] == '--': self.passant_white: Pawn = None
            else: self.passant_white: Pawn = self.board.get_piece((int(passant[0]), int(passant[1])))
            if passant[2:] == '--': self.passant_black: Pawn = None
            else: self.passant_black: Pawn = self.board.get_piece((int(passant[2]), int(passant[3])))
            self.cont = int(cont)
    
    def get_cont(self) -> int:
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

    # 
    # metodos de condicao de fim de partida
    # 
