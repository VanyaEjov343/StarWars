import pygame


class Settings():
    def __init__(self):
        self.ship_speed = 2
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = pygame.image.load('images/sky.bmp')
