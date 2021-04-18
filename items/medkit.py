import pygame

from utils.globals import Globals
from items.item import Item

class Medkit(Item):
  def __init__(self, player, scoreboard):
    super().__init__(player, "assets/medkit.png")
    self.scoreboard = scoreboard

  def __copy__(self):
    return self.__class__(self.player, self.scoreboard)

  def update(self):
    if pygame.sprite.collide_rect(self, self.player):
      Globals.lives = min(Globals.max_lives, Globals.lives + Globals.max_lives / 2)
      self.scoreboard.update_lives()
      self.kill()