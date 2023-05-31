from typing import Type
from piece import Piece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King


class Board():

    def __init__(self, state: str = None) -> None:
        self.__sprite = ""
        self.match = None
        self.__pieces = []
        self.__white = []
        self.__black = []
        self.__matrix = []
        if state is None:
            # primeira linha da matriz corresponde a linha 1 do tabuleiro (a linha de baixo)
            self.__matrix = [[Rook(True, 'a1'), Knight(True, 'b1'), Bishop(True, 'c1'), Queen(True, 'd1'),
                              King(True, 'e1'), Bishop(True, 'f1'), Knight(True, 'g1'), Rook(True, 'h1')],
                             [Pawn(True, 'a2'), Pawn(True, 'b2'), Pawn(True, 'c2'), Pawn(True, 'd2'),
                              Pawn(True, 'e2'), Pawn(True, 'f2'), Pawn(True, 'g2'), Pawn(True, 'h2')],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             [Pawn(False, 'a7'), Pawn(False, 'b7'), Pawn(False, 'c7'), Pawn(False, 'd7'),
                              Pawn(False, 'e7'), Pawn(False, 'f7'), Pawn(False, 'g7'), Pawn(False, 'h7')],
                             [Rook(False, 'a8'), Knight(False, 'b8'), Bishop(False, 'c8'), Queen(False, 'd8'),
                              King(False, 'e8'), Bishop(False, 'f8'), Knight(False, 'g8'), Rook(False, 'h8')]
                              ]
        else:
            # falta implementação
            pass
        self.__insert_pieces()

    def get_sprite(self) -> str:
        return self.__sprite

    def get_piece(self, pos: tuple[int, int]) -> Type[Piece]:
        return self.__matrix[pos[0]][pos[1]]

    def __insert_pieces(self) -> None:
        for i in range(8):
            for j in range(8):
                piece: Piece = self.get_piece((i, j))
                if piece is not None:
                    piece.board = self
                    self.__pieces.append(piece)
                    if piece.get_is_white():
                        self.__white.append(piece)
                    else:
                        self.__black.append(piece)

    def __add_piece(self, piece: Type[Piece], pos: tuple[int, int]) -> None:
        self.__matrix[pos[0]][pos[1]] = piece
        piece.board = self
        self.__pieces.append(piece)
        if piece.get_is_white():
            self.__white.append(piece)
        else:
            self.__black.append(piece)
    
    def __delete_piece(self, pos: tuple[int, int]) -> None:
        piece = self.get_piece(pos)
        self.__matrix[pos[0]][pos[1]] = None
        self.__pieces.remove(piece)
        if piece.get_is_white():
            self.__white.remove(piece)
        else:
            self.__black.remove(piece)

    def move_piece(self, pos_old: tuple[int, int], pos_new: tuple[int, int], passant: bool = False) -> None:
        piece = self.get_piece(pos_old)
        self.__matrix[pos_old[0]][pos_old[1]] = None
        if self.get_piece(pos_new) is not None:
            self.__delete_piece(pos_new)
        self.__matrix[pos_new[0]][pos_new[1]] = piece
        if passant:
            self.__delete_piece((pos_new[0]-1, pos_new[1]))
    
    def promotion(self, piece: Type[Pawn], pos: tuple[int, int]) -> None:
        self.__delete_piece(pos)
        self.__add_piece(piece, pos)
