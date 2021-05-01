import pygame

from utils.globals import Globals
from interfaces.status_effect import StatusEffect
from items.item import Item

class DoubleJump(Item):
  image = pygame.image.load("assets/double_jump.png").convert_alpha()

  def __init__(self, player):
    super().__init__(player, DoubleJump.image)
    self.duration = 10

  def undo_effect(self):
    self.player.max_jumps = 1

  def update(self):
    if pygame.sprite.collide_rect(self, self.player):
      self.player.max_jumps = 2
      StatusEffect.group.add(
        StatusEffect("double_jump", DoubleJump.image, self.undo_effect, self.duration)
      )
      self.kill()