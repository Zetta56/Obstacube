import pygame
from entity import Entity

def create_platforms(display):
  platforms = pygame.sprite.Group()
  # Floor
  platforms.add(Platform(display, 0, display.get_rect().height - 40, 
                         display.get_rect().width, 40))
  # Floating Platforms
  platforms.add(Platform(display, 350, 450, 150, 50))
  return platforms

class Platform(Entity):
  def __init__(self, display, x, y, width, height):
    # Settings
    self.color = "#eeeeee"

    # Rects
    super().__init__(display, self.color, x, y, width, height)