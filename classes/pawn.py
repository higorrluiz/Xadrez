from piece import Piece
from typing import Self, Type


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

    def move(self, pos: tuple[int, int]) -> Self:
        # polimorfismo: falta implementação para considerar en passant
        pass
