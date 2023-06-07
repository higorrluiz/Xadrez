import pygame
from importador import *


class Piece(pygame.sprite.Sprite):
    
    def __init__(self, pos: str = '', is_white: bool = None) -> None:
        super().__init__()

        if pos == '' and is_white is None:
            self.is_white = None
            self.row = None
            self.column = None
        else:
            if not isinstance(is_white, bool) or not isinstance(pos, str):
                raise Exception("Invalid type!")
            if len(pos) != 2:
                raise Exception("Invalid postion size!")
            if (pos[0].upper() not in COLUNAS or not pos[1].isnumeric or 
                int(pos[1]) < 1 or int(pos[1]) > 8):
                raise Exception("Invalid pos!")
            
            self.is_white = is_white
            self.row = int(pos[1]) - 1  # linha (1-8) -> (0-7)
            self.column = COLUNAS[pos[0].upper()]  # coluna (A-G) -> (0-7)

        self.board = None
        self.selecionado = False
        self.image: pygame.image = None
        self.rect: pygame.Rect = None
        self.name = None
        self.moves = []
    
    def get_is_white(self) -> bool:
        return self.is_white

    # linha (1-8) -> (0-7)
    def get_row(self) -> int:
        return self.row

    # coluna (A-G) -> (0-7)
    def get_column(self) -> int:
        return self.column
    
    def get_pos(self) -> tuple[int, int]:
        row = self.get_row()
        column = self.get_column()
        return (row, column)
    
    def get_moves(self) -> list[tuple[int, int]]:
        return self.moves
    
    def verify_moves(self, check: bool = True) -> None:
        column = self.column
        row = self.row
        white = self.board.white
        black = self.board.black
        white_group = self.board.white_group
        black_group = self.board.black_group
        matrix = self.board.matrix
        cont = self.board.match.cont

        for i in range(len(self.moves)-1, -1, -1):
            self.move(self.moves[i])
            if check:
                if self.board.match.king_is_checked(self.is_white): del self.moves[i]
            else:
                if self.board.match.discovered_check(self.is_white): del self.moves[i]
            self.column = column
            self.row = row
            self.board.white = white
            self.board.black = black
            self.board.white_group = white_group
            self.board.black_group = black_group
            self.board.matrix = matrix
        self.board.match.cont = cont
        
    # calcula os movimentos possiveis e os coloca em self.moves
    def possible_moves(self, check: bool) -> None:
        pass

    def move(self, pos: tuple[int, int]) -> None:
        self.board.match.increment_cont()
        self.board.move_piece(self.get_pos(), pos)
        self.column = pos[1]
        self.row = pos[0]
