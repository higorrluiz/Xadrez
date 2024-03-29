import pygame
from importador import *


class Piece(pygame.sprite.Sprite):
    
    def __init__(self, pos: str = None, is_white: bool = None) -> None:
        super().__init__()

        if pos is None:
            self.row = None
            self.column = None
        else:
            self.row = int(pos[1]) - 1  # linha (1-8) -> (0-7)
            self.column = COLUNAS[pos[0].upper()]  # coluna (A-G) -> (0-7)
        self.is_white = is_white
        self.board = None
        self.selecionado: bool = False
        self.image: pygame.image = None
        self.rect: pygame.Rect = None
        self.name: str = None
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
        row = self.row
        column = self.column
        return (row, column)
    
    def get_pos_str(self) -> str:
        if self.row is None or self.column is None: return None
        row = str(self.row + 1)
        column = COLUNAS_STR[self.column]
        pos_str = column + row
        return pos_str
    
    def get_moves(self) -> list[tuple[int, int]]:
        return self.moves
    
    def verify_moves(self, check: bool = True) -> None:
        column = self.column
        row = self.row
        white = self.board.white[:]
        black = self.board.black[:]
        matrix = [row[:] for row in self.board.matrix]
        passant_white = self.board.match.passant_white
        passant_black = self.board.match.passant_black
        if self.name.lower() in 'kr':
            moved = self.moved

        # percorre lista ao contrario para permitir remocao
        for i in range(len(self.moves)-1, -1, -1):
            # quando mock=True, o movimento eh feito somente na matriz do tabuleiro e
            # na posicao da peca, sem alterar as listas de pecas nem a interface
            self.move(self.moves[i], mock=True)
            if check:
                if self.board.match.king_is_checked(self.is_white): del self.moves[i]
            else:
                if self.board.match.discovered_check(self.is_white): del self.moves[i]
            self.column = column
            self.row = row
            self.board.matrix = [row[:] for row in matrix]
        self.board.white = white[:]
        self.board.black = black[:]
        self.board.match.passant_white = passant_white
        self.board.match.passant_black = passant_black
        if self.name.lower() in 'kr':
            self.moved = moved
        
    # calcula os movimentos possiveis e os coloca em self.moves
    def possible_moves(self, check: bool) -> None:
        pass

    def move(self, pos: tuple[int, int], mock: bool = False) -> None:
        if not mock: self.board.match.increment_cont()
        self.board.move_piece(self.get_pos(), pos, mock=mock)
        self.column = pos[1]
        self.row = pos[0]
