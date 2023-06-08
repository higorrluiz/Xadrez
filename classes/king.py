import pygame
from classes.piece import Piece
from classes.rook import Rook
from importador import POSICOES_TABULEIRO


class King(Piece):

    def __init__(self, pos: str, is_white: bool, moved: bool = False) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white king.png') if is_white else pygame.image.load('assets/images/black king.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'k'
        self.moved = moved
        
    def get_moved(self) -> bool:
        return self.moved
    
    def possible_moves(self, check: bool) -> None:
        # limpa a lista de movimentos e pega a posicao da peca
        self.moves = []
        linha, coluna = self.get_pos()

        # movimento para cima
        aux_linha = linha + 1
        aux_coluna = coluna
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and aux_linha <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para baixo
        aux_linha = linha - 1
        aux_coluna = coluna
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and aux_linha >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para direita
        aux_linha = linha
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para esquerda
        aux_linha = linha
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para diagonal 1 (cima e esquerda)
        aux_linha = linha + 1
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para diagonal 2 (cima e direita)
        aux_linha = linha + 1
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para diagonal 3 (baixo e esquerda)
        aux_linha = linha - 1
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento para diagonal 4 (baixo e direita)
        aux_linha = linha - 1
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # para o movimento do rei, sempre devem ser feitas todas as verificacoes
        self.verify_moves(True)

        if not self.moved and not check:
            # roque maior
            p1: Piece = self.board.get_piece((linha, 1))
            p2: Piece = self.board.get_piece((linha, 2))
            p3: Piece = self.board.get_piece((linha, 3))
            rook: Piece = self.board.get_piece((linha, 0))
            if (p1 is None and p2 is None and p3 is None and isinstance(rook, Rook) and 
                rook.get_is_white() == self.is_white and not rook.get_moved()):
                cont = self.board.match.cont
                self.move((linha, 3))
                if not self.board.match.king_is_checked(self.is_white):
                    self.move((linha, 2))
                    if not self.board.match.king_is_checked(self.is_white):
                        self.moves.append((linha, 2))  # movimento
                    self.move((linha, 3))
                    self.move((linha, 4))
                else:
                    self.move((linha, 4))
                self.board.match.cont = cont

            # roque menor
            p1 = self.board.get_piece((linha, 5))
            p2 = self.board.get_piece((linha, 6))
            rook = self.board.get_piece((linha, 7))
            if (p1 is None and p2 is None and isinstance(rook, Rook) and 
                rook.get_is_white() == self.is_white and not rook.get_moved()):
                cont = self.board.match.cont
                self.move((linha, 5))
                if not self.board.match.king_is_checked(self.is_white):
                    self.move((linha, 6))
                    if not self.board.match.king_is_checked(self.is_white):
                        self.moves.append((linha, 6))  # movimento
                    self.move((linha, 5))
                    self.move((linha, 4))
                else:
                    self.move((linha, 4))
                self.board.match.cont = cont

    def move(self, pos: tuple[int, int], mock: bool = False) -> None:
        self.moved = True
        column = self.get_column()
        # verifica se eh roque
        if abs(column - pos[1]) > 1:
            # roque maior
            if pos[1] == 2:
                rook: Rook = self.board.get_piece((pos[0], 0))
                rook_column = 3    
            # roque menor
            elif pos[1] == 6:
                rook: Rook = self.board.get_piece((pos[0], 7))
                rook_column = 5
            else:
                raise Exception("Invalid movement!")
            super().move(pos, mock)
            self.board.match.decrement_cont()
            rook.move((pos[0], rook_column), mock)
        else:
            super().move(pos, mock)
