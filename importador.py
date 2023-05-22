import pygame 
from pygame.locals import *

from classes import *
# from classes.rook import Rook

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


# black_pieces = [Rook((lista_pos_x[0],0),"black"), Knight((lista_pos_x[1],0), "black"), Bishop((lista_pos_x[2],0),"black"), King((lista_pos_x[3],0),"black"), Queen((lista_pos_x[4],0),"black"), Bishop((lista_pos_x[5],0),"black"), Knight((lista_pos_x[6],0),"black"), Rook((lista_pos_x[7],0),"black")]
black_pawns =[]

# black_pieces2 = [Rook('8A',"black")]#, Knight('8B', "black"), Bishop('8C',"black"), King('8D',"black"), Queen('8E',"black"), Bishop('8F',"black"), Knight('8G',"black"), Rook('8H',"black")]


pos_y = 68.75 * 7

# white_pieces = [Rook((lista_pos_x[0],pos_y),"white"), Knight((lista_pos_x[1],pos_y), "white"), Bishop((lista_pos_x[2],pos_y),"white"), King((lista_pos_x[3],pos_y),"white"), Queen((lista_pos_x[4],pos_y),"white"), Bishop((lista_pos_x[5],pos_y),"white"), Knight((lista_pos_x[6],pos_y),"white"), Rook((lista_pos_x[7],pos_y),"white")]
white_pawns = []


tamanho=68.75
POSICOES_TABULEIRO = {
    '8A':(tamanho*0,0), '8B':(tamanho*1,0),'8C':(tamanho*2,0),'8D':(tamanho*3,0),'8E':(tamanho*4,0),'8F':(tamanho*5,0),'8G':(tamanho*6,0),'8H':(tamanho*7,0),
    '7A':(tamanho*0,tamanho), '7B':(tamanho*1,tamanho),'7C':(tamanho*2,tamanho),'7D':(tamanho*3,tamanho),'7E':(tamanho*4,tamanho),'7F':(tamanho*5,tamanho),'7G':(tamanho*6,tamanho),'7H':(tamanho*7,tamanho),
    '6A':(tamanho*0,tamanho*2), '6B':(tamanho*1,tamanho*2),'6C':(tamanho*2,tamanho*2),'6D':(tamanho*3,tamanho*2),'6E':(tamanho*4,tamanho*2),'6F':(tamanho*5,tamanho*2),'6G':(tamanho*6,tamanho*2),'6H':(tamanho*6,tamanho*2),      
    '5A':(tamanho*0,tamanho*3), '5B':(tamanho*1,tamanho*3),'5C':(tamanho*2,tamanho*3),'5D':(tamanho*3,tamanho*3),'5E':(tamanho*4,tamanho*3),'5F':(tamanho*5,tamanho*3),'5G':(tamanho*6,tamanho*3),'5H':(tamanho*7,tamanho*3),
    '4A':(tamanho*0,tamanho*4), '4B':(tamanho*1,tamanho*4),'4C':(tamanho*2,tamanho*4),'4D':(tamanho*3,tamanho*4),'4E':(tamanho*4,tamanho*4),'4F':(tamanho*5,tamanho*4),'4G':(tamanho*6,tamanho*4),'4H':(tamanho*7,tamanho*4),
    '3A':(tamanho*0,tamanho*5), '3B':(tamanho*1,tamanho*5),'3C':(tamanho*2,tamanho*5),'3D':(tamanho*3,tamanho*5),'3E':(tamanho*4,tamanho*5),'3F':(tamanho*5,tamanho*5),'3G':(tamanho*6,tamanho*5),'3H':(tamanho*7,tamanho*5),
    '2A':(tamanho*0,tamanho*6), '2B':(tamanho*1,tamanho*6),'2C':(tamanho*2,tamanho*6),'2D':(tamanho*3,tamanho*6),'2E':(tamanho*4,tamanho*6),'2F':(tamanho*5,tamanho*6),'2G':(tamanho*6,tamanho*6),'2H':(tamanho*7,tamanho*6),
    '1A':(tamanho*0,tamanho*7), '1B':(tamanho*1,tamanho*7),'1C':(tamanho*2,tamanho*7),'1D':(tamanho*3,tamanho*7),'1E':(tamanho*4,tamanho*7),'1F':(tamanho*5,tamanho*7),'1G':(tamanho*6,tamanho*7),'1H':(tamanho*7,tamanho*7),
    }


posicoes_pawns_pretos = ['7A','7B','7C','7D','7E','7F','7G','7H']
posicoes_pawns_brancos = ['2A','2B','2C','2D','2E','2F','2G','2H']
