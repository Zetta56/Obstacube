import pygame

from utils.globals import Globals
from interfaces.status_effect import StatusEffect
from items.item import Item

class Medkit(Item):
  image = pygame.image.load("assets/medkit.png").convert_alpha()

  def __init__(self, player, scoreboard):
    super().__init__(player, Medkit.image)
    self.scoreboard = scoreboard

  def __copy__(self):
    return self.__class__(self.player, self.scoreboard)

  def update(self):
    if (self.player.lives != self.player.max_lives and
        pygame.sprite.collide_rect(self, self.player)):
      self.player.lives = min(self.player.max_lives, int(self.player.lives + 
        self.player.max_lives / 2))
      self.scoreboard.update_lives(self.player.lives)
      self.kill()