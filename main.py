import pygame 
from pygame.locals import *
from sys import exit
from classes.pawn import Pawn
from classes.piece import Dummy
from importador import *
from tabuleiro import Tabuleiro
import math


pygame.init()
altura= 550
largura=550
tam_quadrado = 68.75 #tamanho quadrado linha
botao_exit=769
GREEN   = (  0,255,  0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()



peça = None
tabuleiro = Tabuleiro(tela)

def selecionado(x,y):
    x=x/tam_quadrado
    y=y/tam_quadrado
    vermelho = math.floor(x)*tam_quadrado
    rosa = math.floor(y)*tam_quadrado
    amarelo = math.ceil(x) * tam_quadrado
    azul = math.ceil(y) * tam_quadrado

    pygame.draw.line(tela,(255,0,0),(vermelho,rosa),(amarelo,rosa),2)
    pygame.draw.line(tela,(255,0,0),(amarelo,rosa),(amarelo,azul),2)
    pygame.draw.line(tela,(255,0,0),(vermelho,azul),(amarelo,azul),2)
    pygame.draw.line(tela,(255,0,0),(vermelho,rosa),(vermelho,azul),2)
sel_x,sel_y=20000,30000
x,y=0,0

def posicao_do_quadrado():#pega a posicao do quadro clicado pelo mouse
    mouse = pygame.mouse.get_pos()
    x_novo=math.floor(mouse[0]/tam_quadrado)*tam_quadrado
    y_novo=math.floor(mouse[1]/tam_quadrado)*tam_quadrado
    return x_novo, y_novo

x=0
black_pawns_group=pygame.sprite.Group()
for pos in posicoes_pawns_pretos:
    print(f"{pos}:#{POSICOES_TABULEIRO[pos]}")
    black_pawns.append(Pawn(pos,"black",pos))
    black_pawns_group.add(black_pawns[-1])
    x= x+ 68.75


peça = Dummy()
while True:
    tela.fill('black')
       
    tabuleiro.desenhar_tabuleiro()
    tabuleiro.desenhar_peças_pretas()
    tabuleiro.desenhar_peças_brancas()

    black_pawns_group.draw(tela)
    black_pawns_group.update()

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if (event.type == botao_exit) or (event.type == QUIT):
            pygame.quit()
            exit()
        #permite selecao nas peças pretas
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(black_pawns)):
                if black_pawns[i].rect.collidepoint(mouse_pos):#checa se o mouse cliclou em um peão preto
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1] 
                    peça = black_pawns[i]
                    peça.selecionado = True
                    print(posicao_do_quadrado())
                    
                
            for j in black_pieces:#checa se o mouse cliclou em um peça preta
                if j.rect.collidepoint(mouse_pos):
                    sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                    peça = j
                    peça.selecionado = True
                    

            if peça.selecionado == True and not (peça.rect.collidepoint(mouse_pos)):#se a peça esta selecionada e o usuario
                x=posicao_do_quadrado()[0]
                y=posicao_do_quadrado()[1]
                sel_x,sel_y = mouse_pos[0],mouse_pos[1]
                
                if movimentos_validos[0] == (x,y) or movimentos_validos[1] == (x,y):
                    peça.rect.x= x
                    peça.rect.y= y
                    peça.selecionado = False
                
    if peça.selecionado == True:
        x_bolinha=math.ceil(peça.rect.left/tam_quadrado)*tam_quadrado
        y_bolinha=math.floor(peça.rect.top/tam_quadrado)*tam_quadrado
        movimentos_validos  = peça.mostrar_movimentos_validos(x_bolinha,y_bolinha,tela)
    selecionado(sel_x,sel_y)
    












    pygame.display.flip()

    #Setting FPS
    clock.tick(60)
    pygame.display.update


