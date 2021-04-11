import pygame
from utils.globals import Globals

class Entity(pygame.sprite.Sprite):
  def __init__(self, color, x, y, width, height):
    super().__init__()
    self.visible = True
    self.tasks = pygame.sprite.Group()

    # Rects
    self.rect = pygame.Rect(x, y, width, height)
    self.color = color
    self.position = pygame.Vector2(self.rect.x, self.rect.y)
    self.velocity = pygame.Vector2(0, 0)
    self.length = pygame.Vector2(self.rect.width, self.rect.height)

  def update(self):
    self.position += self.velocity
    self.rect.x = self.position.x
    self.rect.y = self.position.y

  def draw(self):
    if self.visible:
      pygame.draw.rect(Globals.display, pygame.Color(self.color), self.rect)