from piece import Piece


class Knight(Piece):

    __type = 'N'

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
    
    def possible_moves(self) -> list[tuple[int, int]]:
        # falta implementação
        pass
