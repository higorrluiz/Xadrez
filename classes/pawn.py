from typing import Type
import pygame
from classes.piece import Piece
from importador import POSICOES_TABULEIRO

class Pawn(Piece):

    def __init__(self, pos: str, is_white: bool) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white pawn.png') if is_white else pygame.image.load('assets/images/black pawn.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'p'

    def possible_moves(self,x_atual, y_atual,tela):
        x1_valido = x_atual+(68.75/2)
        y1_valido=y_atual+68.75+(68.75/2)
        x2_valido = x1_valido
        y2_valido= y1_valido +68.75
        pygame.draw.circle(tela, (207,14,14), (x1_valido,y1_valido), 10) 
        pygame.draw.circle(tela, (207,14,14), (x2_valido,y2_valido), 10)
        return (x_atual,y_atual+(68.75)), (x_atual,y_atual+68.75*2)

    def promote(self, piece: Type[Piece]) -> None:
        self.board.promotion(piece, self.get_position())
    
    # def possible_moves(self) -> None:
    #     # limpa a lista de movimentos e pega a posicao da peca
    #     self._moves = []
    #     linha, coluna = self.get_position()

    #     if self._is_white:
    #         # movimento simples para frente
    #         aux_linha = linha + 1
    #         aux_coluna = coluna
    #         piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
    #         if aux_linha <= 7 and piece is None:
    #             self._moves.append((aux_linha, aux_coluna))

    #             # movimento duplo para frente
    #             aux_linha = linha + 2
    #             piece = self.board.get_piece((aux_linha, aux_coluna))
    #             if linha == 1 and aux_linha <= 7 and piece is None:
    #                 self._moves.append((aux_linha, aux_coluna))

    #         # movimento de captura para a esquerda
    #         aux_linha = linha + 1
    #         aux_coluna = coluna - 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #         passant_piece = self.board.get_piece((linha, aux_coluna))
    #         if ((piece is not None or (passant_piece is not None and self.board.match.passant_black == passant_piece)) 
    #             and aux_linha <= 7 and aux_coluna >= 0):
    #             self._moves.append((aux_linha, aux_coluna))

    #         # movimento de captura para a direita
    #         aux_linha = linha + 1
    #         aux_coluna = coluna + 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #         passant_piece = self.board.get_piece((linha, aux_coluna))
    #         if ((piece is not None or (passant_piece is not None and self.board.match.passant_black == passant_piece)) 
    #             and aux_linha <= 7 and aux_coluna <= 7):
    #             self._moves.append((aux_linha, aux_coluna))
    #     else:
    #         # movimento simples para frente
    #         aux_linha = linha - 1
    #         aux_coluna = coluna
    #         piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
    #         if aux_linha >= 0 and piece is None:
    #             self._moves.append((aux_linha, aux_coluna))
            
    #             # movimento duplo para frente
    #             aux_linha = linha - 2
    #             piece = self.board.get_piece((aux_linha, aux_coluna))
    #             if linha == 6 and aux_linha >= 0 and piece is None:
    #                 self._moves.append((aux_linha, aux_coluna))

    #         # movimento de captura para a esquerda
    #         aux_linha = linha - 1
    #         aux_coluna = coluna - 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #         passant_piece = self.board.get_piece((linha, aux_coluna))
    #         if ((piece is not None or (passant_piece is not None and self.board.match.passant_white == passant_piece)) 
    #             and aux_linha >= 0 and aux_coluna >= 0):
    #             self._moves.append((aux_linha, aux_coluna))

    #         # movimento de captura para a direita
    #         aux_linha = linha - 1
    #         aux_coluna = coluna + 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #         passant_piece = self.board.get_piece((linha, aux_coluna))
    #         if ((piece is not None or (passant_piece is not None and self.board.match.passant_white == passant_piece)) 
    #             and aux_linha >= 0 and aux_coluna <= 7):
    #             self._moves.append((aux_linha, aux_coluna))

    def move(self, pos: tuple[int, int]) -> None:
        column = self.get_column()
        piece = self.board.get_piece(pos)
        # verifica se eh en passant
        if column != pos[1] and piece is None:
            self.board.move_piece(self.get_position(), pos, True)
            pos_column = self._inv_map()[pos[1]]
            pos_row = str(pos[0] + 1)
            self._position = pos_column + pos_row
        else:
            row = self.get_row()
            # verifica se moveu 2 casas
            if abs(row - pos[0]) == 2:
                if self._is_white:
                    self.board.match.passant_white = self
                else:
                    self.board.match.passant_black = self
            super().move(pos)