import pygame

class Entity(pygame.sprite.Sprite):
  def __init__(self, display, color, x, y, width, height):
    super().__init__()
    self.color = color
    self.visible = True
    self.tasks = pygame.sprite.Group()

    # Rects
    self.display = display
    self.rect = pygame.Rect(x, y, width, height)
    self.position = pygame.Vector2(self.rect.x, self.rect.y)
    self.velocity = pygame.Vector2(0, 0)
    self.length = pygame.Vector2(self.rect.width, self.rect.height)

  def draw(self):
    if self.visible:
      pygame.draw.rect(self.display, pygame.Color(self.color), self.rect)