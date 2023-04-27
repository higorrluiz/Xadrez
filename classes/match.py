from typing import Type
from board import Board
from pawn import Pawn


class Match:

    def __init__(self, board: Type[Board]) -> None:
        board.match = self
        self.__board = board
        self.__passant_white = None
        self.__passant_black = None

    def get_board(self) -> Type[Board]:
        return self.__board
    
    def get_passant_white(self) -> Type[Pawn]:
        return self.__passant_white

    def get_passant_black(self) -> Type[Pawn]:
        return self.__passant_black    
    
    # 
    # métodos de condição de fim de partida
    # 
