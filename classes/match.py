from typing import Type
from classes.board import Board
from classes.pawn import Pawn


class Match:

    def __init__(self, board: Type[Board]) -> None:
        board.match = self
        self.cont = 0
        # peca branca que pode ser capturada pelo en passant
        self.passant_white: Pawn = None
        # peca preta que pode ser capturada pelo en passant
        self.passant_black: Pawn = None
    
    def get_cont(self) -> int:
        return self.cont
    
    def set_cont_zero(self) -> None:
        self.cont = 0

    def increment_cont(self) -> None:
        self.cont += 1

    def decrement_cont(self) -> None:
        self.cont -= 1
    
    # 
    # metodos de condicao de fim de partida
    # 
