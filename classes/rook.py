import pygame
from classes.piece import Piece
from importador import POSICOES_TABULEIRO


class Rook(Piece):

    def __init__(self, pos: str, is_white: bool, moved: bool = False) -> None:
        super().__init__(pos, is_white)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images/white rook.png') if is_white else pygame.image.load('assets/images/black rook.png'),
            (68, 68)
        )
        self.rect = self.image.get_rect(topleft=POSICOES_TABULEIRO[pos])
        self.name = 'r'
        self.moved = moved

    def get_moved(self) -> bool:
        return self.moved

    def possible_moves(self,x_atual, y_atual,tela):
        x1_valido = x_atual+(68.75/2)
        y1_valido=y_atual+68.75+(68.75/2)
        x2_valido = x1_valido
        y2_valido= y1_valido +68.75
        pygame.draw.circle(tela, (207,14,14), (x1_valido,y1_valido), 10) 
        pygame.draw.circle(tela, (207,14,14), (x2_valido,y2_valido), 10)
        return (x_atual,y_atual+(68.75)), (x_atual,y_atual+68.75*2)
    
    # def possible_moves(self) -> None:
    #     # limpa a lista de movimentos e pega a posicao da peca
    #     self.moves = []
    #     linha, coluna = self.get_pos()

    #     # movimentos para cima
    #     aux_linha = linha + 1
    #     aux_coluna = coluna
    #     piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
    #     while piece is None and aux_linha <= 7:
    #         self.moves.append((aux_linha, aux_coluna))
    #         aux_linha += 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if piece is not None and piece.is_white != self.is_white:
    #         self.moves.append((aux_linha, aux_coluna))
        
    #     # movimentos para baixo
    #     aux_linha = linha - 1
    #     aux_coluna = coluna
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     while piece is None and aux_linha >= 0:
    #         self.moves.append((aux_linha, aux_coluna))
    #         aux_linha -= 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if piece is not None and piece.is_white != self.is_white:
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimentos para direita
    #     aux_linha = linha
    #     aux_coluna = coluna + 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     while piece is None and aux_coluna <= 7:
    #         self.moves.append((aux_linha, aux_coluna))
    #         aux_coluna += 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if piece is not None and piece.is_white != self.is_white:
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimentos para esquerda
    #     aux_linha = linha
    #     aux_coluna = coluna - 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     while piece is None and aux_coluna >= 0:
    #         self.moves.append((aux_linha, aux_coluna))
    #         aux_coluna -= 1
    #         piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if piece is not None and piece.is_white != self.is_white:
    #         self.moves.append((aux_linha, aux_coluna))

    def move(self, pos: tuple[int, int]) -> None:
        self.moved = True
        super().move(pos)
        pass
