import pygame
from classes.piece import Piece
from importador import POSICOES_TABULEIRO


class Knight(Piece):

    def __init__(self, pos: str, is_white: bool) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white knight.png') if is_white else 
            pygame.image.load('assets/images/black knight.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'n'

    def possible_moves(self, check: bool) -> None:
        # limpa a lista de movimentos e pega a posicao da peca
        self.moves = []
        linha, coluna = self.get_pos()

        # movimento em L (para cima e direita)
        aux_linha = linha + 2
        aux_coluna = coluna + 1
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para cima e esquerda)
        aux_linha = linha + 2
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para baixo e direita)
        aux_linha = linha - 2
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para baixo e esquerda)
        aux_linha = linha - 2
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para direita e cima)
        aux_linha = linha + 1
        aux_coluna = coluna + 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para direita e baixo)
        aux_linha = linha - 1
        aux_coluna = coluna + 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna <= 7):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para esquerda e cima)
        aux_linha = linha + 1
        aux_coluna = coluna - 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha <= 7 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        # movimento em L (para esquerda e baixo)
        aux_linha = linha - 1
        aux_coluna = coluna - 2
        piece = self.board.get_piece((aux_linha, aux_coluna))
        if ((piece is None or piece.is_white != self.is_white) and 
            aux_linha >= 0 and aux_coluna >= 0):
            self.moves.append((aux_linha, aux_coluna))

        self.verify_moves(check)
