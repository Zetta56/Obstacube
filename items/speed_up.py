import pygame

from utils.globals import Globals
from interfaces.status_effect import StatusEffect
from items.item import Item

class SpeedUp(Item):
  image = pygame.image.load("assets/speed_up.png").convert_alpha()

  def __init__(self, player):
    super().__init__(player, SpeedUp.image)
    self.duration = 10

  def undo_effect(self):
    self.player.speed = 5

  def update(self):
    if pygame.sprite.collide_rect(self, self.player):
      self.player.speed = 10
      StatusEffect.group.add(
        StatusEffect("double_jump", SpeedUp.image, self.undo_effect, self.duration)
      )
      self.kill()