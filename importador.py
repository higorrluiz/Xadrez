import pygame 
from pygame.locals import *


# black_queen = pygame.image.load('assets/images/black queen.png')
# black_queen = pygame.transform.scale(black_queen, (68, 68))
# black_queen_small = pygame.transform.scale(black_queen, (45, 45))
# black_king = pygame.image.load('assets/images/black king.png')
# black_king = pygame.transform.scale(black_king, (68, 68))
# black_king_small = pygame.transform.scale(black_king, (45, 45))
# black_rook = pygame.image.load('assets/images/black rook.png')
# black_rook = pygame.transform.scale(black_rook, (68, 68))
# black_rook_small = pygame.transform.scale(black_rook, (45, 45))
# black_bishop = pygame.image.load('assets/images/black bishop.png')
# black_bishop = pygame.transform.scale(black_bishop, (68, 68))
# black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
# black_knight = pygame.image.load('assets/images/black knight.png')
# black_knight = pygame.transform.scale(black_knight, (68, 68))
# black_knight_small = pygame.transform.scale(black_knight, (45, 45))
# black_pawn = pygame.image.load('assets/images/black pawn.png')
# black_pawn = pygame.transform.scale(black_pawn, (65, 65))
# black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
# white_queen = pygame.image.load('assets/images/white queen.png')
# white_queen = pygame.transform.scale(white_queen, (68, 68))
# white_queen_small = pygame.transform.scale(white_queen, (45, 45))
# white_king = pygame.image.load('assets/images/white king.png')
# white_king = pygame.transform.scale(white_king, (68, 68))
# white_king_small = pygame.transform.scale(white_king, (45, 45))
# white_rook = pygame.image.load('assets/images/white rook.png')
# white_rook = pygame.transform.scale(white_rook, (68, 68))
# white_rook_small = pygame.transform.scale(white_rook, (45, 45))
# white_bishop = pygame.image.load('assets/images/white bishop.png')
# white_bishop = pygame.transform.scale(white_bishop, (68, 68))
# white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
# white_knight = pygame.image.load('assets/images/white knight.png')
# white_knight = pygame.transform.scale(white_knight, (68, 68))
# white_knight_small = pygame.transform.scale(white_knight, (45, 45))
# white_pawn = pygame.image.load('assets/images/white pawn.png')
# white_pawn = pygame.transform.scale(white_pawn, (68, 68))
# white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

tamanho = 68.75

POSICOES_TABULEIRO = {
    'A8':(tamanho*0,tamanho*0), 'B8':(tamanho*1,tamanho*0), 'C8':(tamanho*2,tamanho*0), 'D8':(tamanho*3,tamanho*0), 'E8':(tamanho*4,tamanho*0), 'F8':(tamanho*5,tamanho*0), 'G8':(tamanho*6,tamanho*0), 'H8':(tamanho*7,tamanho*0),
    'A7':(tamanho*0,tamanho*1), 'B7':(tamanho*1,tamanho*1), 'C7':(tamanho*2,tamanho*1), 'D7':(tamanho*3,tamanho*1), 'E7':(tamanho*4,tamanho*1), 'F7':(tamanho*5,tamanho*1), 'G7':(tamanho*6,tamanho*1), 'H7':(tamanho*7,tamanho*1),
    'A6':(tamanho*0,tamanho*2), 'B6':(tamanho*1,tamanho*2), 'C6':(tamanho*2,tamanho*2), 'D6':(tamanho*3,tamanho*2), 'E6':(tamanho*4,tamanho*2), 'F6':(tamanho*5,tamanho*2), 'G6':(tamanho*6,tamanho*2), 'H6':(tamanho*7,tamanho*2),      
    'A5':(tamanho*0,tamanho*3), 'B5':(tamanho*1,tamanho*3), 'C5':(tamanho*2,tamanho*3), 'D5':(tamanho*3,tamanho*3), 'E5':(tamanho*4,tamanho*3), 'F5':(tamanho*5,tamanho*3), 'G5':(tamanho*6,tamanho*3), 'H5':(tamanho*7,tamanho*3),
    'A4':(tamanho*0,tamanho*4), 'B4':(tamanho*1,tamanho*4), 'C4':(tamanho*2,tamanho*4), 'D4':(tamanho*3,tamanho*4), 'E4':(tamanho*4,tamanho*4), 'F4':(tamanho*5,tamanho*4), 'G4':(tamanho*6,tamanho*4), 'H4':(tamanho*7,tamanho*4),
    'A3':(tamanho*0,tamanho*5), 'B3':(tamanho*1,tamanho*5), 'C3':(tamanho*2,tamanho*5), 'D3':(tamanho*3,tamanho*5), 'E3':(tamanho*4,tamanho*5), 'F3':(tamanho*5,tamanho*5), 'G3':(tamanho*6,tamanho*5), 'H3':(tamanho*7,tamanho*5),
    'A2':(tamanho*0,tamanho*6), 'B2':(tamanho*1,tamanho*6), 'C2':(tamanho*2,tamanho*6), 'D2':(tamanho*3,tamanho*6), 'E2':(tamanho*4,tamanho*6), 'F2':(tamanho*5,tamanho*6), 'G2':(tamanho*6,tamanho*6), 'H2':(tamanho*7,tamanho*6),
    'A1':(tamanho*0,tamanho*7), 'B1':(tamanho*1,tamanho*7), 'C1':(tamanho*2,tamanho*7), 'D1':(tamanho*3,tamanho*7), 'E1':(tamanho*4,tamanho*7), 'F1':(tamanho*5,tamanho*7), 'G1':(tamanho*6,tamanho*7), 'H1':(tamanho*7,tamanho*7),
}

POSICOES_TABULEIRO_LISTA = [
    [(tamanho*0,tamanho*7), (tamanho*1,tamanho*7), (tamanho*2,tamanho*7), (tamanho*3,tamanho*7), (tamanho*4,tamanho*7), (tamanho*5,tamanho*7), (tamanho*6,tamanho*7), (tamanho*7,tamanho*7)],
    [(tamanho*0,tamanho*6), (tamanho*1,tamanho*6), (tamanho*2,tamanho*6), (tamanho*3,tamanho*6), (tamanho*4,tamanho*6), (tamanho*5,tamanho*6), (tamanho*6,tamanho*6), (tamanho*7,tamanho*6)],
    [(tamanho*0,tamanho*5), (tamanho*1,tamanho*5), (tamanho*2,tamanho*5), (tamanho*3,tamanho*5), (tamanho*4,tamanho*5), (tamanho*5,tamanho*5), (tamanho*6,tamanho*5), (tamanho*7,tamanho*5)],      
    [(tamanho*0,tamanho*4), (tamanho*1,tamanho*4), (tamanho*2,tamanho*4), (tamanho*3,tamanho*4), (tamanho*4,tamanho*4), (tamanho*5,tamanho*4), (tamanho*6,tamanho*4), (tamanho*7,tamanho*4)],
    [(tamanho*0,tamanho*3), (tamanho*1,tamanho*3), (tamanho*2,tamanho*3), (tamanho*3,tamanho*3), (tamanho*4,tamanho*3), (tamanho*5,tamanho*3), (tamanho*6,tamanho*3), (tamanho*7,tamanho*3)],
    [(tamanho*0,tamanho*2), (tamanho*1,tamanho*2), (tamanho*2,tamanho*2), (tamanho*3,tamanho*2), (tamanho*4,tamanho*2), (tamanho*5,tamanho*2), (tamanho*6,tamanho*2), (tamanho*7,tamanho*2)],
    [(tamanho*0,tamanho*1), (tamanho*1,tamanho*1), (tamanho*2,tamanho*1), (tamanho*3,tamanho*1), (tamanho*4,tamanho*1), (tamanho*5,tamanho*1), (tamanho*6,tamanho*1), (tamanho*7,tamanho*1)],
    [(tamanho*0,tamanho*0), (tamanho*1,tamanho*0), (tamanho*2,tamanho*0), (tamanho*3,tamanho*0), (tamanho*4,tamanho*0), (tamanho*5,tamanho*0), (tamanho*6,tamanho*0), (tamanho*7,tamanho*0)]
]

COLUNAS = dict({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7})

COLUNAS_STR = "ABCDEFGH"
