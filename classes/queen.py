import pygame
from classes.piece import Piece
from importador import POSICOES_TABULEIRO


class Queen(Piece):

    def __init__(self, pos: str, is_white: bool) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white queen.png') if is_white else 
            pygame.image.load('assets/images/black queen.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'q'
    
    def possible_moves(self, check: bool) -> None:
        # limpa a lista de movimentos e pega a posicao da peca
        self.moves = []
        linha, coluna = self.get_pos()

        # movimentos para cima
        aux_linha = linha + 1
        aux_coluna = coluna
        piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))
        
        # movimentos para baixo
        aux_linha = linha - 1
        aux_coluna = coluna
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))

        # movimentos para direita
        aux_linha = linha
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_coluna <= 7:
            self.moves.append((aux_linha, aux_coluna))
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))

        # movimentos para esquerda
        aux_linha = linha
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_coluna >= 0:
            self.moves.append((aux_linha, aux_coluna))
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))

        # movimentos para diagonal 1 (cima e esquerda)
        aux_linha = linha + 1
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7 and aux_coluna >= 0:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha += 1
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))
        
        # movimentos para diagonal 2 (cima e direita)
        aux_linha = linha + 1
        aux_coluna = coluna + 1 
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha <= 7 and aux_coluna <= 7:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha += 1
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))

        # movimentos para diagonal 3 (baixo e esquerda)
        aux_linha = linha - 1
        aux_coluna = coluna - 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0 and aux_coluna >= 0:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha -= 1
            aux_coluna -= 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))

        # movimentos para diagonal 4 (baixo e direita)
        aux_linha = linha - 1
        aux_coluna = coluna + 1
        piece = self.board.get_piece((aux_linha, aux_coluna))
        while piece is None and aux_linha >= 0 and aux_coluna <= 7:
            self.moves.append((aux_linha, aux_coluna))
            aux_linha -= 1
            aux_coluna += 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
        if piece is not None and piece.is_white != self.is_white:
            self.moves.append((aux_linha, aux_coluna))
    
        self.verify_moves(check)
