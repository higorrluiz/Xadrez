import pygame 
from pygame.locals import *

from classes import *
from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.queen import Queen
from classes.rook import Rook

black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (68, 68))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (68, 68))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (68, 68))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (68, 68))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (68, 68))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (68, 68))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (68, 68))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (68, 68))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (68, 68))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (68, 68))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (68, 68))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

pos_x = 0
lista_pos_x=[]
for i in range(9):
    lista_pos_x.append(pos_x)
    pos_x = pos_x + 68.75


black_pieces = [Rook((lista_pos_x[0],0),"black"), Knight((lista_pos_x[1],0), "black"), Bishop((lista_pos_x[2],0),"black"), King((lista_pos_x[3],0),"black"), Queen((lista_pos_x[4],0),"black"), Bishop((lista_pos_x[5],0),"black"), Knight((lista_pos_x[6],0),"black"), Rook((lista_pos_x[7],0),"black")]
black_pawns =[]

pos_y = 68.75 * 7

white_pieces = [Rook((lista_pos_x[0],pos_y),"white"), Knight((lista_pos_x[1],pos_y), "white"), Bishop((lista_pos_x[2],pos_y),"white"), King((lista_pos_x[3],pos_y),"white"), Queen((lista_pos_x[4],pos_y),"white"), Bishop((lista_pos_x[5],pos_y),"white"), Knight((lista_pos_x[6],pos_y),"white"), Rook((lista_pos_x[7],pos_y),"white")]
white_pawns = []
