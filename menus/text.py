import pygame

class Text():
  def __init__(self, display, center, font_size, color="#dddddd"):
    self.display = display
    self.font = pygame.font.SysFont(None, font_size)
    self.image = self.font.render("Score: 5", True, pygame.Color(color))
    self.rect = self.image.get_rect()
    self.rect.center = center

  def blit(self):
    self.display.blit(self.image, self.rect)