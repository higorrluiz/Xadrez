from piece import Piece
from typing import Self


class Rook(Piece):

    __type = 'R'

    def __init__(self, is_white: bool, position: str, moved: bool = False) -> None:
        super().__init__(is_white, position)
        if is_white:
            self._sprite = ""
        else:
            self._sprite = ""
        self.__moved = moved

    def get_type(self) -> str:
        if self.get_is_white():
            return self.__type.lower()
        else:
            return self.__type.upper()
        
    def get_moved(self) -> bool:
        return self.__moved
    
    def possible_moves(self) -> list[tuple[int, int]]:
        # falta implementação
        pass

    def move(self, pos: tuple[int, int]) -> Self:
        self.__moved = True
        super().move(pos)
        pass
