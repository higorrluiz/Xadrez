from typing import Type
import pygame
from classes.piece import Piece
from importador import POSICOES_TABULEIRO

class Pawn(Piece):

    def __init__(self, pos: str, is_white: bool) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white pawn.png') if is_white else 
            pygame.image.load('assets/images/black pawn.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'p'

    def promote(self, piece: Type[Piece]) -> None:
        self.board.promotion(piece, self.get_pos())
    
    def possible_moves(self, check: bool) -> None:
        # limpa a lista de movimentos e pega a posicao da peca
        self.moves = []
        linha, coluna = self.get_pos()

        if self.is_white:
            # movimento simples para frente
            aux_linha = linha + 1
            aux_coluna = coluna
            piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
            if aux_linha <= 7 and piece is None:
                self.moves.append((aux_linha, aux_coluna))

                # movimento duplo para frente
                aux_linha = linha + 2
                piece = self.board.get_piece((aux_linha, aux_coluna))
                if linha == 1 and piece is None:
                    self.moves.append((aux_linha, aux_coluna))

            # movimento de captura para a esquerda
            aux_linha = linha + 1
            aux_coluna = coluna - 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            passant_piece = self.board.get_piece((linha, aux_coluna))
            if ((piece is not None and not piece.is_white) or
               (passant_piece is not None and self.board.match.passant_black == passant_piece)):
                self.moves.append((aux_linha, aux_coluna))

            # movimento de captura para a direita
            aux_linha = linha + 1
            aux_coluna = coluna + 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            passant_piece = self.board.get_piece((linha, aux_coluna))
            if ((piece is not None and not piece.is_white) or 
               (passant_piece is not None and self.board.match.passant_black == passant_piece)):
                self.moves.append((aux_linha, aux_coluna))
        else:
            # movimento simples para frente
            aux_linha = linha - 1
            aux_coluna = coluna
            piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
            if aux_linha >= 0 and piece is None:
                self.moves.append((aux_linha, aux_coluna))
            
                # movimento duplo para frente
                aux_linha = linha - 2
                piece = self.board.get_piece((aux_linha, aux_coluna))
                if linha == 6 and piece is None:
                    self.moves.append((aux_linha, aux_coluna))

            # movimento de captura para a esquerda
            aux_linha = linha - 1
            aux_coluna = coluna - 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            passant_piece = self.board.get_piece((linha, aux_coluna))
            if ((piece is not None and piece.is_white) or 
               (passant_piece is not None and self.board.match.passant_white == passant_piece)):
                self.moves.append((aux_linha, aux_coluna))

            # movimento de captura para a direita
            aux_linha = linha - 1
            aux_coluna = coluna + 1
            piece = self.board.get_piece((aux_linha, aux_coluna))
            passant_piece = self.board.get_piece((linha, aux_coluna))
            if ((piece is not None and piece.is_white) or 
               (passant_piece is not None and self.board.match.passant_white == passant_piece)):
                self.moves.append((aux_linha, aux_coluna))

        self.verify_moves(check)

    def move(self, pos: tuple[int, int], mock: bool = False) -> None:
        column = self.get_column()
        piece = self.board.get_piece(pos)
        # verifica se eh en passant
        if column != pos[1] and piece is None:
            self.board.move_piece(self.get_pos(), pos, True, mock)
            self.column = pos[1]
            self.row = pos[0]
        else:
            row = self.get_row()
            # verifica se moveu 2 casas
            if abs(row - pos[0]) == 2:
                if self.is_white:
                    self.board.match.passant_white = self
                else:
                    self.board.match.passant_black = self
            super().move(pos, mock)
        if not mock: self.board.match.set_cont_zero()
