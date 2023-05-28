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

    #     # movimento para cima
    #     aux_linha = linha + 1
    #     aux_coluna = coluna
    #     piece: Piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and aux_linha <= 7):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para baixo
    #     aux_linha = linha - 1
    #     aux_coluna = coluna
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and aux_linha >= 0):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para direita
    #     aux_linha = linha
    #     aux_coluna = coluna + 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and aux_coluna <= 7):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para esquerda
    #     aux_linha = linha
    #     aux_coluna = coluna - 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and 
    #         aux_linha >= 0 and aux_coluna >= 0):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para diagonal 1 (cima e esquerda)
    #     aux_linha = linha + 1
    #     aux_coluna = coluna - 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and 
    #         aux_linha <= 7 and aux_coluna >= 0):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para diagonal 2 (cima e direita)
    #     aux_linha = linha + 1
    #     aux_coluna = coluna + 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and 
    #         aux_linha <= 7 and aux_coluna <= 7):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para diagonal 3 (baixo e esquerda)
    #     aux_linha = linha - 1
    #     aux_coluna = coluna - 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and 
    #         aux_linha >= 0 and aux_coluna >= 0):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # movimento para diagonal 4 (baixo e direita)
    #     aux_linha = linha - 1
    #     aux_coluna = coluna + 1
    #     piece = self.board.get_piece((aux_linha, aux_coluna))
    #     if ((piece is None or piece.is_white != self.is_white) and 
    #         aux_linha >= 0 and aux_coluna <= 7):
    #         self.moves.append((aux_linha, aux_coluna))

    #     # falta considerar cheque nos movimentos básicos

    #     if not self.moved:
    #         # roque maior
    #         p1: Piece = self.board.get_piece((linha, 1))
    #         p2: Piece = self.board.get_piece((linha, 2))
    #         p3: Piece = self.board.get_piece((linha, 3))
    #         rook: Piece = self.board.get_piece((linha, 0))
    #         if (p1 is None and p2 is None and p3 is None and isinstance(rook, Rook) and 
    #             rook.get_is_white() == self.is_white and not rook.get_moved()):
    #             # falta considerar cheque no roque menor
    #             self.moves.append((linha, 0))

    #         # roque menor
    #         p1 = self.board.get_piece((linha, 5))
    #         p2 = self.board.get_piece((linha, 6))
    #         rook = self.board.get_piece((linha, 7))
    #         if (p1 is None and p2 is None and isinstance(rook, Rook) and 
    #             rook.get_is_white() == self.is_white and not rook.get_moved()):
    #             # falta considerar cheque no roque maior
    #             self.moves.append((linha, 7))

    def move(self, pos: tuple[int, int]) -> None:
        self.moved = True
        column = self.get_column()
        # verifica se eh roque
        if abs(column - pos[1]) > 1:
            rook: Rook = self.board.get_piece(pos)
            # roque maior
            if pos[1] == 0:
                king_column = 2
                rook_column = 3
            # roque menor
            elif pos[1] == 7:
                king_column = 6
                rook_column = 5
            else:
                raise Exception("Invalid movement!")
            super().move((self.get_row(), king_column))
            self.board.match.decrement_cont()
            rook.move((rook.get_row(), rook_column))
        else:
            super().move(pos)
