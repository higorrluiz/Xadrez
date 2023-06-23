import pygame
import os
from importador import ASSETS_PATH, STATE_PATH
from classes.bishop import Bishop
from classes.queen import Queen
from classes.knight import Knight
from classes.rook import Rook


class Menu:
    def __init__(self, tela: pygame.Surface, game_loop: bool, game_state: bool) -> None:
        self.saved_state = os.stat(STATE_PATH).st_size != 0

        self.tela = tela
        self.game_loop = game_loop
        self.game_state = game_state
        self.background = pygame.image.load(ASSETS_PATH + "background.jpg")
        self.background = pygame.transform.scale(self.background, self.tela.get_size())
        self.button_width = self.tela.get_width() // 4
        self.button_height = self.tela.get_height() // 10
        self.button_x = self.tela.get_width() // 2 - self.button_width // 2
        self.button_y = self.tela.get_height() // 2 - self.button_height // 2
        if self.saved_state: self.botao_continue = pygame.image.load(ASSETS_PATH + "continue_button.png")
        self.botao_play = pygame.image.load(ASSETS_PATH + "play_button.png")
        self.botao_exit = pygame.image.load(ASSETS_PATH + "exit_button.jpg")
        self.botao_options = pygame.image.load(ASSETS_PATH + "options_button.png")
        if self.saved_state: self.botao_continue_rect = self.botao_play.get_rect(topleft=(self.button_x, self.button_y - self.button_height * 1.5))
        self.botao_play_rect = self.botao_play.get_rect(topleft=(self.button_x, self.button_y))
        self.botao_options_rect = self.botao_options.get_rect(topleft=(self.button_x, self.button_y + self.button_height * 1.5))
        self.botao_exit_rect = self.botao_exit.get_rect(topleft=(self.button_x, self.button_y + self.button_height * 3))
        self.fonte = pygame.font.SysFont('Arial', self.tela.get_height() // 10)
        self.texto_titulo = self.fonte.render('Xadrez 2', True, (255, 255, 255))
        self.peca_images_white = {
            "white queen": pygame.transform.scale(pygame.image.load("assets/images/white queen.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "white rook": pygame.transform.scale(pygame.image.load("assets/images/white rook.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "white bishop": pygame.transform.scale(pygame.image.load("assets/images/white bishop.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "white knight": pygame.transform.scale(pygame.image.load("assets/images/white knight.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            }
        self.peca_images_black = {
            "black queen": pygame.transform.scale(pygame.image.load("assets/images/black queen.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "black rook": pygame.transform.scale(pygame.image.load("assets/images/black rook.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "black bishop": pygame.transform.scale(pygame.image.load("assets/images/black bishop.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            "black knight": pygame.transform.scale(pygame.image.load("assets/images/black knight.png"), (self.tela.get_width() // 8, self.tela.get_height() // 8)),
            }

    def draw(self) -> tuple[bool, str]:
        self.tela.blit(self.background, (0, 0))
        self.tela.blit(self.texto_titulo, (self.tela.get_width() // 2 - self.texto_titulo.get_width() // 2, self.tela.get_height() // 10))
        if self.saved_state:self.tela.blit(self.botao_continue, self.botao_continue_rect)
        self.tela.blit(self.botao_play, self.botao_play_rect)
        self.tela.blit(self.botao_options, self.botao_options_rect)
        self.tela.blit(self.botao_exit, self.botao_exit_rect)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if (event.type == self.botao_exit) or (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if self.saved_state and self.botao_continue_rect.collidepoint(mouse_pos):
                    self.game_state = "continue_game"
                    self.game_loop = True
                elif self.botao_play_rect.collidepoint(mouse_pos):
                    self.game_state = "mode_selection"
                    self.game_loop = True
                elif self.botao_exit_rect.collidepoint(mouse_pos):
                    self.game_loop = False
                elif self.botao_options_rect.collidepoint(mouse_pos):
                    self.game_state = "options"
        return self.game_loop, self.game_state
    
    def options(self, show_possible_moves: bool) -> tuple[bool, str]:
        self.tela.blit(self.background, (0, 0))
        fonte = pygame.font.SysFont('Arial', self.tela.get_height() // 20)
        texto_opcoes = fonte.render('Mostrar movimentos possíveis', True, (0, 0, 0))
        texto_opcoes_fundo = pygame.Surface((texto_opcoes.get_width() + 20, texto_opcoes.get_height() + 10))
        texto_opcoes_fundo.fill((255, 255, 255))
        texto_opcoes_fundo.blit(texto_opcoes, (10, 5))
        self.tela.blit(texto_opcoes_fundo, (self.tela.get_width() // 2 - texto_opcoes_fundo.get_width() // 2, self.tela.get_height() // 4 - texto_opcoes_fundo.get_height() // 2))
        texto_ativado = fonte.render('ATIVADO', True, (255, 255, 255))
        texto_desativado = fonte.render('DESATIVADO', True, (255, 255, 255))
        botao_voltar = pygame.Rect(self.tela.get_width() // 2 - 100, self.tela.get_height() - 100, 200, 50)
        texto_voltar = fonte.render('VOLTAR', True, (0, 0, 0))
        cor_ativado = (0, 255, 0) if show_possible_moves else (128, 128, 128)
        cor_desativado = (255, 0, 0) if not show_possible_moves else (128, 128, 128)
        padding_ativado = (200 - texto_ativado.get_width()) // 2
        padding_desativado = (200 - texto_desativado.get_width()) // 2
        pygame.draw.rect(self.tela, cor_ativado, (self.tela.get_width() // 2 - 200, self.tela.get_height() // 2, 200, 50))
        pygame.draw.rect(self.tela, cor_desativado, (self.tela.get_width() // 2, self.tela.get_height() // 2, 200, 50))
        self.tela.blit(texto_ativado, ((self.tela.get_width() // 2) - texto_ativado.get_width() - padding_ativado, self.tela.get_height() // 2 + 25 - texto_ativado.get_height() // 2))
        self.tela.blit(texto_desativado, ((self.tela.get_width() // 2) + padding_desativado, self.tela.get_height() // 2 + 25 - texto_desativado.get_height() // 2))
        pygame.draw.rect(self.tela, (0, 0, 0), botao_voltar, 2)
        self.tela.blit(texto_voltar, (self.tela.get_width() // 2 - texto_voltar.get_width() // 2, self.tela.get_height() - 75 - texto_voltar.get_height() // 2))
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if botao_voltar.collidepoint(mouse_pos):
                    self.game_state = "menu"
                elif (self.tela.get_width() // 2 - 200) <= mouse_pos[0] <= (self.tela.get_width() // 2 - 200 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    show_possible_moves = True
                elif (self.tela.get_width() // 2) <= mouse_pos[0] <= (self.tela.get_width() // 2 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    show_possible_moves = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.tela.get_width() // 2 - 200) <= mouse_pos[0] <= (self.tela.get_width() // 2 - 200 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    cor_ativado = (0, 128, 0)
                elif (self.tela.get_width() // 2) <= mouse_pos[0] <= (self.tela.get_width() // 2 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    cor_desativado = (128, 0, 0)
            if event.type == pygame.MOUSEBUTTONUP:
                if (self.tela.get_width() // 2 - 200) <= mouse_pos[0] <= (self.tela.get_width() // 2 - 200 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    show_possible_moves = True
                    cor_ativado = (0, 255, 0)
                elif (self.tela.get_width() // 2) <= mouse_pos[0] <= (self.tela.get_width() // 2 + 200) and (self.tela.get_height() // 2) <= mouse_pos[1] <= (self.tela.get_height() // 2 + 50):
                    show_possible_moves = False
                    cor_desativado = (255, 0, 0)
        pygame.draw.rect(self.tela, cor_ativado, (self.tela.get_width() // 2 - 200, self.tela.get_height() // 2, 200, 50), 2)
        pygame.draw.rect(self.tela, cor_desativado, (self.tela.get_width() // 2, self.tela.get_height() // 2, 200, 50), 2)
        pygame.display.update()
        return show_possible_moves, self.game_state
    
    def end_game(self, text_1: str, text_2: str) -> tuple[bool, str]:
        self.saved_state = False
        self.tela.blit(self.background, (0, 0))
        fonte = pygame.font.SysFont('Arial', self.tela.get_height() // 20)
        texto_xeque = fonte.render(text_1, True, (0, 0, 0))
        texto_xeque_fundo = pygame.Surface((texto_xeque.get_width() + 20, texto_xeque.get_height() + 10))
        texto_xeque_fundo.fill((255, 255, 255))
        texto_xeque_fundo.blit(texto_xeque, (10, 5))
        self.tela.blit(texto_xeque_fundo, (self.tela.get_width() // 2 - texto_xeque_fundo.get_width() // 2, self.tela.get_height() // 4 - texto_xeque_fundo.get_height() // 2))
        if text_2 != '': texto_vencedor = fonte.render(text_2, True, (255, 255, 255))
        botao_voltar = pygame.Rect(self.tela.get_width() // 2 - 100, self.tela.get_height() - 100, 200, 50)
        texto_voltar = fonte.render('VOLTAR', True, (0, 0, 0))
        if text_2 != '': self.tela.blit(texto_vencedor, ((self.tela.get_width() // 2) - texto_vencedor.get_width() // 2, self.tela.get_height() // 2 + texto_vencedor.get_height() // 2))
        pygame.draw.rect(self.tela, (0, 0, 0), botao_voltar, 2)
        self.tela.blit(texto_voltar, (self.tela.get_width() // 2 - texto_voltar.get_width() // 2, self.tela.get_height() - 75 - texto_voltar.get_height() // 2))
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if botao_voltar.collidepoint(mouse_pos):
                    self.game_state = "menu"
        if text_2 != '':
            texto_vencedor_fundo = pygame.Surface((texto_vencedor.get_width() + 20, texto_vencedor.get_height() + 10))
            texto_vencedor_fundo.fill((0, 0, 0))
            texto_vencedor_fundo.blit(texto_vencedor, (10, 5))
            self.tela.blit(texto_vencedor_fundo, (self.tela.get_width() // 2 - texto_vencedor_fundo.get_width() // 2, self.tela.get_height() // 2 + texto_vencedor_fundo.get_height() // 2))

        pygame.display.update()
        return self.game_loop, self.game_state
    
    def checkmate(self, color: str) -> tuple[bool, str]:
        winner_text = f'O jogador {color.upper()} venceu!'
        return self.end_game('XEQUE-MATE', winner_text)
    
    def tie(self) -> tuple[bool, str]:
        return self.end_game('EMPATE', '')
    
    def promotion(self, peca, white_turn):
        self.tela.blit(self.background, (0, 0))
        texto_promocao = self.fonte.render('PROMOÇÃO', True, (0, 0, 0))
        texto_promocao_fundo = pygame.Surface((texto_promocao.get_width() + 20, texto_promocao.get_height() + 10))
        texto_promocao_fundo.fill((255, 255, 255))
        texto_promocao_fundo.blit(texto_promocao, (10, 5))
        self.tela.blit(texto_promocao_fundo, (self.tela.get_width() // 2 - texto_promocao_fundo.get_width() // 2, self.tela.get_height() // 4 - texto_promocao_fundo.get_height() // 2))
        fonte_meio = pygame.font.SysFont('Arial', self.tela.get_height() // 20)
        texto_meio = fonte_meio.render("Escolha a peça para promover", True, (0, 0, 0))
        texto_meio_fundo = pygame.Surface((texto_meio.get_width() + 20, texto_meio.get_height() + 10))
        texto_meio_fundo.fill((255, 255, 255))
        texto_meio_fundo.blit(texto_meio, (10, 5))
        self.tela.blit(texto_meio_fundo, ((self.tela.get_width() // 2) - texto_meio.get_width() // 2, self.tela.get_height() // 2 + texto_meio.get_height() // 2))
        num_pecas = len(self.peca_images_white)
        largura_disponivel = self.tela.get_width() - 20
        largura_peca = largura_disponivel // num_pecas
        y = self.tela.get_height() // 2 + texto_promocao.get_height() * 2
        x = largura_peca - 10
        images = self.peca_images_white if white_turn else self.peca_images_black
        peca_rects = []
        chosen = False
        for key in images:
            peca_image = images[key]
            peca_rect = pygame.Rect(x, y, peca_image.get_width(), peca_image.get_height())
            peca_rects.append(peca_rect)
            self.tela.blit(peca_image, (x, y))
            x += peca_image.get_width() + 10
        while not chosen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            for rect in peca_rects:
                if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                    if peca_rects.index(rect) == 0:
                        peca.promote(Queen(peca.get_pos_str(), white_turn))
                    if peca_rects.index(rect) == 1:
                        peca.promote(Rook(peca.get_pos_str(), white_turn))
                    if peca_rects.index(rect) == 2:
                        peca.promote(Bishop(peca.get_pos_str(), white_turn)) 
                    if peca_rects.index(rect) == 3:
                        peca.promote(Knight(peca.get_pos_str(), white_turn))
                    chosen = True

            pygame.display.update()

    def mode_selection(self, ia_toggled: bool):
        ia_difficulty = 1
        self.tela.blit(self.background, (0, 0))
        fonte_meio = pygame.font.SysFont('Arial', self.tela.get_height() // 15)
        texto = fonte_meio.render('Selecionar modo de jogo', True, (0, 0, 0))
        texto_fundo = pygame.Surface((texto.get_width() + 20, texto.get_height() + 10))
        texto_fundo.fill((255, 255, 255))
        texto_fundo.blit(texto, (10, 5))
        self.tela.blit(texto_fundo, (self.tela.get_width() // 2 - texto_fundo.get_width() // 2, self.tela.get_height() // 4 - texto_fundo.get_height() // 2))
        botao_2 = pygame.image.load(ASSETS_PATH + "player_v_player.png")
        button_x = self.tela.get_width() // 2 - botao_2.get_width() // 2

        if not ia_toggled:
            botao_solo = pygame.image.load(ASSETS_PATH + "player_v_cpu.png")
            botao_2_rect = botao_2.get_rect(topleft=(button_x, self.button_y + self.button_height * 1.5))
        else:
            botao_solo = pygame.image.load(ASSETS_PATH + "player_v_cpu_toggled.png")
            botao_easy = pygame.image.load(ASSETS_PATH + "easy_button.png")
            botao_medium = pygame.image.load(ASSETS_PATH + "mid_button.png")
            botao_hard = pygame.image.load(ASSETS_PATH + "hard_button.png")
            botao_easy_rect = botao_easy.get_rect(topleft=(self.button_x - self.button_width * 1.2, self.button_y + self.button_height * 1.5))
            botao_medium_rect = botao_medium.get_rect(topleft=(self.button_x, self.button_y + self.button_height * 1.5))
            botao_hard_rect = botao_hard.get_rect(topleft=(self.button_x + self.button_width * 1.2, self.button_y + self.button_height * 1.5))
            botao_2_rect = botao_2.get_rect(topleft=(button_x, self.button_y + self.button_height * 3))
            self.tela.blit(botao_easy, botao_easy_rect)
            self.tela.blit(botao_medium, botao_medium_rect)
            self.tela.blit(botao_hard, botao_hard_rect)

        botao_solo_rect = botao_solo.get_rect(topleft=(button_x, self.button_y))
        self.tela.blit(botao_solo, botao_solo_rect)
        self.tela.blit(botao_2, botao_2_rect)
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if (event.type == self.botao_exit) or (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if botao_solo_rect.collidepoint(mouse_pos):
                    ia_toggled = not ia_toggled
                elif botao_2_rect.collidepoint(mouse_pos):
                    self.game_state = "new_game"
                elif botao_easy_rect.collidepoint(mouse_pos):
                    self.game_state = "new_game"
                    ia_difficulty = 1
                elif botao_medium_rect.collidepoint(mouse_pos):
                    self.game_state = "new_game"
                    ia_difficulty = 2
                elif botao_hard_rect.collidepoint(mouse_pos):
                    self.game_state = "new_game"
                    ia_difficulty = 3
        
        return self.game_state, ia_toggled, ia_difficulty