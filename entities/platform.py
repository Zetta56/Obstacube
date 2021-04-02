import pygame
from entities.entity import Entity

class Platform(Entity):
  @staticmethod
  def create_platforms(display):
    """Instantiates group of platforms"""
    platforms = pygame.sprite.Group()
    platforms.add(Platform(display, 0, display.get_rect().height - 40, 
                           display.get_rect().width, 40))
    platforms.add(Platform(display, 350, 450, 150, 50))
    return platforms

  def __init__(self, display, x, y, width, height):
    self.color = "#dddddd"
    super().__init__(display, self.color, x, y, width, height)