import pygame
from utils.globals import Globals
from entities.entity import Entity

class Platform(Entity):
  @staticmethod
  def create_platforms():
    """Instantiates group of platforms"""
    platforms = pygame.sprite.Group()
    platforms.add(Platform(0, Globals.display_rect.height - 40, 
      Globals.display_rect.width, 40))
    #platforms.add(Platform(350, 450, 150, 50))
    return platforms

  def __init__(self, x, y, width, height):
    self.color = "#dddddd"
    super().__init__(self.color, x, y, width, height)