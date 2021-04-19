import pygame
from random import randrange
from utils.globals import Globals

class Item(pygame.sprite.Sprite):
  def __init__(self, group, player, image_path):
    super().__init__()
    self.group = group
    self.player = player
    self.preimage = pygame.image.load(image_path).convert_alpha()
    self.image = pygame.transform.scale(self.preimage, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = self.get_valid_x()
    self.rect.y = Globals.floor_y - self.rect.height
    
  def __copy__(self):
    return self.__class__(self.group, self.player)

  def get_valid_x(self):
    """Tries to get x-coord where item isn't overlapping with any others"""
    for attempts in range(3):
      x = randrange(0, Globals.display_rect.width - self.rect.width)
      if all(x + self.rect.width < item.rect.left or x > item.rect.right
          for item in self.group):
        break
    return x