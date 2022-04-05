import pygame
from setting import Settings


class Ship():

    def __init__(self, ai_game):
        self.screen = ai_game
        self.settings = Settings()
        self.screen_rect = ai_game.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_bottom:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):

        self.screen.blit(self.image, self.rect)

