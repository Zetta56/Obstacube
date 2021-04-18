import pygame
from random import randrange
from utils.globals import Globals

class Item(pygame.sprite.Sprite):
  def __init__(self, player, image_path):
    super().__init__()
    self.player = player
    self.preimage = pygame.image.load(image_path).convert_alpha()
    self.image = pygame.transform.scale(self.preimage, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = randrange(0, Globals.display_rect.width - self.rect.width)
    self.rect.y = Globals.floor_y - self.rect.height

  def __copy__(self):
    return self.__class__(self.player)