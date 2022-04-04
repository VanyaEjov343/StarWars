
import sys
import pygame
from setting import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
            pygame.init()
            self.settings = Settings()

            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

            self.screen = pygame.display.set_mode((800,400))
            pygame.display.set_caption("Alien")
            self.bg_color = self.settings.bg_color
            self.ship = Ship(self.screen)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self, event):
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
    def _check_keyup_events(self, event):
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
    def _update_screen(self):
            self.screen.blit(self.settings.bg_color, (0, 0))
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
