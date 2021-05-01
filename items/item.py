import pygame
from random import randrange
from utils.globals import Globals
from utils.task import Task

class Item(pygame.sprite.Sprite):
  group = pygame.sprite.Group()

  def __init__(self, player, image):
    super().__init__()
    self.player = player
    self.image = pygame.transform.scale(image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = self.get_valid_x()
    self.rect.y = Globals.floor_y - self.rect.height
    Item.group.add(self)
    
  def __copy__(self):
    return self.__class__(self.player)

  def get_valid_x(self):
    """Tries to get x-coord that isn't overlapping with other items or player"""
    for attempts in range(3):
      x = randrange(0, Globals.display_rect.width - self.rect.width)
      if ((x < self.player.rect.left or x > self.player.rect.right) and 
          all(x + self.rect.width < item.rect.left or x > item.rect.right 
          for item in Item.group)):
        break
    return x

  def update(self):
    if self.undo_effect is not None and self.duration > 0:
      Globals.status_effects.add(StatusEffect(self.image, self.undo_effect, self.duration))
      self.kill()