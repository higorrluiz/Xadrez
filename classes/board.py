import pygame
from typing import Type
from classes.piece import Piece
from classes.pawn import Pawn
from classes.rook import Rook
from classes.knight import Knight
from classes.bishop import Bishop
from classes.queen import Queen
from classes.king import King


class Board():

    def __init__(self, tela: pygame.Surface, tam: float, state: str = None) -> None:
        self.match = None

        self.linhas = 8
        self.colunas = 8
        self.tam = tam
        self.tela = tela

        self.white = []
        self.black = []
        self.matrix = []
        if state is None:
            # primeira linha da matriz corresponde a linha 1 do tabuleiro (a linha de baixo)
            self.matrix = [[Rook('A1', True), Knight('B1', True), Bishop('C1', True), Queen('D1', True),
                            King('E1', True), Bishop('F1', True), Knight('G1', True), Rook('H1', True)],
                           [Pawn('A2', True), Pawn('B2', True), Pawn('C2', True), Pawn('D2', True),
                            Pawn('E2', True), Pawn('F2', True), Pawn('G2', True), Pawn('H2', True)],
                           [None, None, None, None, None, None, None, None],
                           [None, None, None, None, None, None, None, None],
                           [None, None, None, None, None, None, None, None],
                           [None, None, None, None, None, None, None, None],
                           [Pawn('A7', False), Pawn('B7', False), Pawn('C7', False), Pawn('D7', False),
                            Pawn('E7', False), Pawn('F7', False), Pawn('G7', False), Pawn('H7', False)],
                           [Rook('A8', False), Knight('B8', False), Bishop('C8', False), Queen('D8', False),
                            King('E8', False), Bishop('F8', False), Knight('G8', False), Rook('H8', False)]
                          ]
        else:
            # falta implementação
            pass
        self.__insert_pieces()

    def get_piece(self, pos: tuple[int, int]) -> Type[Piece]:
        return self.matrix[pos[0]][pos[1]]
    
    def get_position(self, piece: Type[Piece]) -> tuple[int, int]:
        for i in range(self.linhas):
            for j in range(self.colunas):
                if piece == self.matrix[i][j]:
                    return (i, j)
        return None

    def __insert_pieces(self) -> None:
        for i in range(self.linhas):
            for j in range(self.colunas):
                piece: Piece = self.get_piece((i, j))
                if piece is not None:
                    piece.board = self
                    if piece.get_is_white():
                        self.white.append(piece)
                    else:
                        self.black.append(piece)

    def __add_piece(self, piece: Type[Piece], pos: tuple[int, int]) -> None:
        self.matrix[pos[0]][pos[1]] = piece
        piece.board = self
        if piece.get_is_white():
            self.white.append(piece)
        else:
            self.black.append(piece)
    
    def __delete_piece(self, pos: tuple[int, int]) -> None:
        piece = self.get_piece(pos)
        self.matrix[pos[0]][pos[1]] = None
        if piece.get_is_white():
            self.white.remove(piece)
        else:
            self.black.remove(piece)

    def move_piece(self, pos_old: tuple[int, int], pos_new: tuple[int, int], passant: bool = False) -> None:
        piece = self.get_piece(pos_old)
        self.matrix[pos_old[0]][pos_old[1]] = None
        if self.get_piece(pos_new) is not None:
            self.__delete_piece(pos_new)
        self.matrix[pos_new[0]][pos_new[1]] = piece
        if passant:
            self.__delete_piece((pos_new[0]-1, pos_new[1]))
    
    def promotion(self, piece: Type[Piece], pos: tuple[int, int]) -> None:
        self.__delete_piece(pos)
        self.__add_piece(piece, pos)

    def desenhar_tabuleiro(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                # desenha os quadrados vizinhos com cores diferentes
                if linha % 2 == 0:
                    self.__desenhar_linha(linha, coluna, 'white', 'dark green')
                else:
                    self.__desenhar_linha(linha, coluna, 'dark green', 'white')

    def __desenhar_linha(self, linha, coluna, primeira_cor, segunda_cor):
        if coluna % 2 == 0:
            pygame.draw.rect(self.tela, primeira_cor, (coluna*self.tam, linha*self.tam, self.tam, self.tam))
        else:
            pygame.draw.rect(self.tela, segunda_cor, (coluna*self.tam, linha*self.tam, self.tam, self.tam))
