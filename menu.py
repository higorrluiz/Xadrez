import pygame
import os
from importador import ASSETS_PATH, STATE_PATH


class Menu:
    def __init__(self, tela, game_loop, game_state):
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
        if self.saved_state: self.botao_continue = pygame.image.load(ASSETS_PATH + "play_button.png")
        self.botao_play = pygame.image.load(ASSETS_PATH + "play_button.png")
        self.botao_exit = pygame.image.load(ASSETS_PATH + "exit_button.jpg")
        self.botao_options = pygame.image.load(ASSETS_PATH + "options_button.png")
        if self.saved_state: self.botao_continue_rect = self.botao_play.get_rect(topleft=(self.button_x, self.button_y - self.button_height * 1.5))
        self.botao_play_rect = self.botao_play.get_rect(topleft=(self.button_x, self.button_y))
        self.botao_options_rect = self.botao_options.get_rect(topleft=(self.button_x, self.button_y + self.button_height * 1.5))
        self.botao_exit_rect = self.botao_exit.get_rect(topleft=(self.button_x, self.button_y + self.button_height * 3))
        self.fonte = pygame.font.SysFont('Arial', self.tela.get_height() // 10)
        self.texto_titulo = self.fonte.render('Xadrez 2', True, (255, 255, 255))

    def draw(self):
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
                    self.game_state = "new_game"
                    self.game_loop = True
                elif self.botao_exit_rect.collidepoint(mouse_pos):
                    self.game_loop = False
                elif self.botao_options_rect.collidepoint(mouse_pos):
                    self.game_state = "options"
        return self.game_loop, self.game_state
    
    def options(self, show_possible_moves):
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
    
    def checkmate(self, color):
        self.tela.blit(self.background, (0, 0))
        fonte = pygame.font.SysFont('Arial', self.tela.get_height() // 20)
        texto_xeque = fonte.render('XEQUE-MATE', True, (0, 0, 0))
        texto_xeque_fundo = pygame.Surface((texto_xeque.get_width() + 20, texto_xeque.get_height() + 10))
        texto_xeque_fundo.fill((255, 255, 255))
        texto_xeque_fundo.blit(texto_xeque, (10, 5))
        self.tela.blit(texto_xeque_fundo, (self.tela.get_width() // 2 - texto_xeque_fundo.get_width() // 2, self.tela.get_height() // 4 - texto_xeque_fundo.get_height() // 2))
        texto_vencedor = fonte.render(f"O jogador {color.upper()} venceu!", True, (255, 255, 255))
        botao_voltar = pygame.Rect(self.tela.get_width() // 2 - 100, self.tela.get_height() - 100, 200, 50)
        texto_voltar = fonte.render('VOLTAR', True, (0, 0, 0))
        self.tela.blit(texto_vencedor, ((self.tela.get_width() // 2) - texto_vencedor.get_width() // 2, self.tela.get_height() // 2 + texto_vencedor.get_height() // 2))
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
        texto_vencedor_fundo = pygame.Surface((texto_vencedor.get_width() + 20, texto_vencedor.get_height() + 10))
        texto_vencedor_fundo.fill((0, 0, 0))
        texto_vencedor_fundo.blit(texto_vencedor, (10, 5))
        self.tela.blit(texto_vencedor_fundo, (self.tela.get_width() // 2 - texto_vencedor_fundo.get_width() // 2, self.tela.get_height() // 2 + texto_vencedor_fundo.get_height() // 2))

        pygame.display.update()
        return self.game_loop, self.game_state