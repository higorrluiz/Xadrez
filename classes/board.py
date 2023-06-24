import pygame
from typing import Type
from classes.piece import Piece
from classes.pawn import Pawn
from classes.rook import Rook
from classes.knight import Knight
from classes.bishop import Bishop
from classes.queen import Queen
from classes.king import King
from importador import *


class Board():

    def __init__(self, tela: pygame.Surface, tam: float, arq: str = None) -> None:
        self.match = None

        self.linhas = 8
        self.colunas = 8
        self.tam = tam
        self.tela = tela

        self.white = []
        self.black = []
        self.white_group=pygame.sprite.Group()
        self.black_group = pygame.sprite.Group()

        self.matrix = []
        if arq is None:
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
            handle = open(arq, 'r')
            linhas = handle.readlines()
            handle.close()

            matrix = [linha.strip() for linha in linhas[:8]]
            moved_string = linhas[8:9][0].strip()
            
            piece: Piece
            index = 0
            self.matrix = []
            for i, linha in enumerate(matrix, 1):
                aux = []
                for j, char in zip(COLUNAS_STR, linha):
                    if char == '-': piece = None
                    else:
                        is_white = (char == char.lower())
                        pos = j + str(i)
                        if char.upper() == 'P': piece = Pawn(pos, is_white)
                        elif char.upper() == 'N': piece = Knight(pos, is_white)
                        elif char.upper() == 'B': piece = Bishop(pos, is_white)
                        elif char.upper() == 'Q': piece = Queen(pos, is_white)
                        else:
                            moved = (moved_string[index].upper() == 'T')
                            index += 1
                            if char.upper() == 'R': piece = Rook(pos, is_white, moved)
                            else: piece = King(pos, is_white, moved)  # char.upper() == 'K'
                    aux.append(piece)
                self.matrix.append(aux)
                
        self.__insert_pieces()

    def save_state(self, arq: str, config: list[bool], ia_difficulty: int) -> None:
        moved_list = []
        handle = open(arq, 'w')
        for i in range(self.linhas):  # 0 - 7
            for j in range(self.colunas):
                piece: Piece = self.get_piece((i, j))
                if piece is None: 
                    handle.write('-')
                else:
                    handle.write(piece.name.lower() if piece.is_white else piece.name.upper())
                    if isinstance(piece, Rook) or isinstance(piece, King): moved_list.append(piece.moved)
            handle.write('\n')
        for moved in moved_list:  # 8
            handle.write('T' if moved else 'F')
        handle.write('\n')
        passant: list[Piece] = [self.match.passant_white, self.match.passant_black]
        for p in passant:  # 9
            if p is not None:
                pos = p.get_pos()
                handle.write(f'{pos[0]}{pos[1]}')
            else: 
                handle.write('--')
        handle.write('\n')
        handle.write(f'{self.match.cont}')  # 10
        handle.write('\n')
        for value in config: handle.write('T' if value else 'F')  # 11
        handle.write('\n')
        handle.write(f'{ia_difficulty}')  # 12
        handle.close()

    def get_piece(self, pos: tuple[int, int]) -> Type[Piece]:
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return self.matrix[pos[0]][pos[1]]
        else:
            return None
        
    def get_pieces(self, is_white: bool) -> list[Piece]:
        return self.white if is_white else self.black
    
    def get_king(self, is_white: bool) -> King:
        if is_white:
            for piece in self.white:
                if isinstance(piece, King): return piece
        else:
            for piece in self.black:
                if isinstance(piece, King): return piece

    def __insert_pieces(self) -> None:
        for i in range(self.linhas):
            for j in range(self.colunas):
                piece: Piece = self.get_piece((i, j))
                if piece is not None:
                    piece.board = self
                    if piece.get_is_white():
                        self.white.append(piece)
                        self.white_group.add(piece)
                    else:
                        self.black.append(piece)
                        self.black_group.add(piece)

    def __add_piece(self, piece: Type[Piece], pos: tuple[int, int], mock: bool = False) -> None:
        self.matrix[pos[0]][pos[1]] = piece
        piece.board = self
        if piece.get_is_white():
            self.white.append(piece)
            if not mock: self.white_group.add(piece)
        else:
            self.black.append(piece)
            if not mock: self.black_group.add(piece)
    
    def __delete_piece(self, pos: tuple[int, int], mock: bool = False) -> None:
        if not mock: self.match.set_cont_zero()
        piece = self.get_piece(pos)
        self.matrix[pos[0]][pos[1]] = None
        if piece.get_is_white():
            self.white.remove(piece)
            if not mock: self.white_group.remove(piece)
        else:
            self.black.remove(piece)
            if not mock: self.black_group.remove(piece)

    def move_piece(self, pos_old: tuple[int, int], pos_new: tuple[int, int], 
                   passant: bool = False, mock: bool = False) -> None:
        piece: Piece = self.get_piece(pos_old)
        if not mock:
            movimento = POSICOES_TABULEIRO_LISTA[pos_new[0]][pos_new[1]]
            piece.rect.x = movimento[0]
            piece.rect.y = movimento[1]
        self.matrix[pos_old[0]][pos_old[1]] = None
        if self.get_piece(pos_new) is not None:
            self.__delete_piece(pos_new, mock)
        self.matrix[pos_new[0]][pos_new[1]] = piece
        if passant:
            aux = 1 if piece.is_white else -1
            self.__delete_piece((pos_new[0]-aux, pos_new[1]), mock)
    
    def promotion(self, piece: Type[Piece], pos: tuple[int, int], mock: bool = False) -> None:
        self.__delete_piece(pos, mock)
        self.__add_piece(piece, pos, mock)

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

    def printa(self) -> None:
        for linha in reversed(self.matrix):
            for p in linha:
                if p is not None:
                    print((p.name).lower() if p.is_white else (p.name).upper(), end=' ')
                else:
                    print('-', end=' ')
            print()
        print()
        print()
