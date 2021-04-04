import pygame
from utils.globals import Globals

class Scoreboard():
  def __init__(self, player):
    # Settings
    self.color = "#dddddd"
    self.font = pygame.font.SysFont(None, 32)

    # Info
    self.player = player
    self.lives = self.player.lives
    self.lives_image = self.font.render(f'Lives: {self.lives}', 
      True, pygame.Color(self.color))

  def update(self):
    if self.player.lives != self.lives:
      self.lives = self.player.lives
      self.lives_image = self.font.render(f'Lives: {self.lives}', 
        True, pygame.Color(self.color))

  def blit(self):
    Globals.display.blit(self.lives_image, (20, 20))