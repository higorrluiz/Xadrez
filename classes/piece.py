from abc import ABC, abstractmethod


class Piece(ABC):

    __map = dict({'a': 0, 'b': 1, 'c': 2, 'd': 3, 
                  'e': 4, 'f': 5, 'g': 6, 'h': 7})
    
    __inv_map = "abcdefgh"
    
    def __init__(self, is_white: bool, position: str) -> None:
        if not isinstance(is_white, bool) or not isinstance(position, str):
            raise Exception("Invalid type!")
        if len(position) != 2:
            raise Exception("Invalid postion size!")
        if (position[0].lower() not in self.__map.keys() or not position[1].isnumeric or 
           int(position[1]) < 1 or int(position[1]) > 8):
            raise Exception("Invalid position!")

        self._sprite = ""
        self.board = None
        self.__is_white = is_white
        self._position = position.lower()
        self._moves = []

    def get_inv_map(self) -> str:
        return self.__inv_map

    def get_sprite(self) -> str:
        return self._sprite
    
    def get_is_white(self) -> bool:
        return self.__is_white

    # linha (1-8) -> (0-7)
    def get_row(self) -> int:
        pos_x = int(self._position[1]) - 1
        return pos_x

    # coluna (A-G) -> (0-7)
    def get_column(self) -> int:
        pos_y = self.__map[self._position[0].lower()]
        return pos_y
    
    def get_position(self) -> tuple[int, int]:
        row = self.get_row()
        column = self.get_column()
        return row, column
    
    def get_moves(self) -> list[tuple[int, int]]:
        return self._moves
        
    # calcula os movimentos possíveis e os coloca em self._moves
    @abstractmethod
    def possible_moves(self) -> None:
        raise NotImplementedError

    def move(self, pos: tuple[int, int]) -> None:
        self.board.move_piece(self.get_position(), pos)
        pos_column = self.__inv_map[pos[1]]
        pos_row = str(pos[0] + 1)
        self._position = pos_column + pos_row
