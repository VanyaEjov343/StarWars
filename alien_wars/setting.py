import pygame


class Settings():
    def __init__(self):
        self.ship_speed = 2
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = pygame.image.load('images/sky.bmp')
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = ('red')

