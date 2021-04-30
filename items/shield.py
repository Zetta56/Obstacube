import pygame

from utils.globals import Globals
from interfaces.status_effect import StatusEffect
from items.item import Item

class Shield(Item):
  image = pygame.transform.scale(
    pygame.image.load("assets/shield.png").convert_alpha(), 
    (50, 50)
  )

  def __init__(self, player):
    super().__init__(player, Shield.image)
    self.duration = 5

  def undo_effect(self):
    self.player.color = "#dddddd"
    self.player.intangible = False

  def update(self):
    if pygame.sprite.collide_rect(self, self.player):
      self.player.intangible = True
      self.player.color = "#306de7"
      Globals.status_effects.add(StatusEffect("shield", Shield.image, 
        self.undo_effect, self.duration))
      self.kill()