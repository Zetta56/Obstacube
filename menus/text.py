import pygame
from utils.globals import Globals

class Text():
  def __init__(self, text, font_size, center=(0, 0), color="#dddddd"):
    self.font = pygame.font.Font("assets/russo_one.ttf", font_size)
    self.image = self.font.render(text, True, pygame.Color(color))
    self.rect = self.image.get_rect()
    self.rect.center = center

  def blit(self):
    Globals.display.blit(self.image, self.rect)