import pygame


map = dict({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7})

class Piece(pygame.sprite.Sprite):
    
    def __init__(self, pos: str = 'A1', is_white: bool = False) -> None:
        super().__init__()

        if not isinstance(is_white, bool) or not isinstance(pos, str):
            raise Exception("Invalid type!")
        if len(pos) != 2:
            raise Exception("Invalid postion size!")
        if (pos[0].upper() not in map or not pos[1].isnumeric or 
           int(pos[1]) < 1 or int(pos[1]) > 8):
            raise Exception("Invalid pos!")

        self.board = None
        self.selecionado = False
        self.is_white = is_white
        self.row = int(pos[1]) - 1  # linha (1-8) -> (0-7)
        self.column = map[pos[0].upper()]  # coluna (A-G) -> (0-7)
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
        
    # calcula os movimentos possiveis e os coloca em self._moves
    def possible_moves(self,x_atual, y_atual,tela):
        pass

    def move(self, pos: tuple[int, int]) -> None:
        self.board.move_piece(self.get_pos(), pos)
        self.column = pos[1]
        self.row = pos[0]
