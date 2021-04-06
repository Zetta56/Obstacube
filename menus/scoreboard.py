import pygame
from utils.globals import Globals
from menus.text import Text

class Scoreboard():
  def __init__(self):
    # Settings
    self.color = "#dddddd"
    self.font_size = 28
    self.update()

  def update(self):
    self.lives = Text(f'Lives: {Globals.lives}', self.font_size)
    self.lives.rect.top = Globals.display_rect.top + 20
    self.lives.rect.left = Globals.display_rect.left + 20

  def blit(self):
    self.lives.blit()