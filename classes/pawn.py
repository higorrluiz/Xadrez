from piece import Piece
from typing import Type


class Pawn(Piece):

    __type = 'P'

    def __init__(self, is_white: bool, position: str) -> None:
        super().__init__(is_white, position)
        if is_white:
            self._sprite = ""
        else:
            self._sprite = ""

    def get_type(self) -> str:
        if self.get_is_white():
            return self.__type.lower()
        else:
            return self.__type.upper()
        
    def promote(self, piece: Type[Piece]) -> None:
        self.board.promotion(piece, self.get_position())
    
    def possible_moves(self) -> list[tuple[int, int]]:
        # falta implementação
        pass

    def move(self, pos: tuple[int, int]) -> None:
        column = self.get_column()
        piece = self.board.get_piece(pos)
        # verifica se é en passant
        if column != pos[1] and piece is None:
            self.board.move_piece(self.get_position(), pos, True)
            pos_column = self.get_inv_map()[pos[1]]
            pos_row = str(pos[0] + 1)
            self._position = pos_column + pos_row
        else:
            row = self.get_row()
            # verifica se moveu 2 casas
            if abs(row - pos[0]) == 2:
                if self.get_is_white():
                    self.board.match.get_passant_white = self
                else:
                    self.board.match.get_passant_black = self
            super().move(pos)
