import pygame
from random import randint

pygame.init()
player_pos = [485, 10] # Axi X: Max 685px / Min 285Px | Axi Y: Max Min 615px Min 10px
player_step = 40
background = pygame.image.load('game_background.jpg')
car = pygame.image.load('car_01.png')
janela = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Meu Primeiro Jogo')

class Hurdle:
    def __init__(self, hurdle_pos_x, hurdle_pos_y, hurdle_step):
        self.image = pygame.image.load('trafic_cone.png')
        self.hurdle_pos_x = hurdle_pos_x
        self.hurdle_pos_y = hurdle_pos_y
        self.hurdle_step = hurdle_step

    def move(self):
        self.hurdle_pos_y += self.hurdle_step
        if self.hurdle_pos_y >= 900:
            self.hurdle_pos_y = -100

    def draw(self, surface):
        surface.blit(self.image, (self.hurdle_pos_x, self.hurdle_pos_y))


cone1 = Hurdle(325, -200, 30)
cone2 = Hurdle(515, 0, 30)
cone3 = Hurdle(700, 500, 30)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_w] and player_pos[1] <= 685:
        player_pos[1] -= player_step
    if comandos[pygame.K_s] and player_pos[1 <= 10]:
        player_pos[1] += player_step
    if comandos[pygame.K_d]:
        player_pos[0] += player_step
    if comandos[pygame.K_a]:
        player_pos[0] -= player_step

    cone1.move()
    cone2.move()
    cone3.move()

    janela.blit(background, (0, 0))
    janela.blit(car, (player_pos[0], player_pos[1]))
    cone1.draw(janela)
    cone2.draw(janela)
    cone3.draw(janela)
    pygame.display.update()

pygame.quit()