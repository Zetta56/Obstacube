import pygame
from utils.globals import Globals
from menus.text import Text

class Scoreboard():
  def __init__(self):
    # Settings
    self.color = "#dddddd"
    self.font_size = 28
    self.get_stats()

  def get_stats(self):
    self.lives = Text(f'Lives: {Globals.lives}', self.font_size)
    self.lives.rect.top = Globals.display_rect.top + 20
    self.lives.rect.left = Globals.display_rect.left + 20

    self.score = Text(f'Score: {Globals.score}', self.font_size)
    self.score.rect.top = Globals.display_rect.top + 20
    self.score.rect.right = Globals.display_rect.right - 20

  def update(self):
    self.get_stats()

  def blit(self):
    self.lives.blit()
    self.score.blit()