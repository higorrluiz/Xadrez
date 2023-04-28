from math import abs
from piece import Piece


class King(Piece):

    __type = 'K'

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

    def move(self, pos: tuple[int, int]) -> None:
        self.__moved = True
        column = self.get_column()
        # verifica se é roque
        if abs(column - pos[1]) > 1:
            rook = self.board.get_piece(pos)
            # roque grande
            if pos[1] == 0:
                king_column = 2
                rook_column = 3
            # roque pequeno
            elif pos[1] == 7:
                king_column = 6
                rook_column = 5
            else:
                raise Exception("Invalid movement!")
            super().move((self.get_row(), king_column))
            rook.move((rook.get_row(), rook_column))
        else:
            super().move(pos)
