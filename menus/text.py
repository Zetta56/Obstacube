import pygame
from utils.globals import Globals

class Text():
  def __init__(self, center, font_size, color="#dddddd"):
    self.font = pygame.font.SysFont(None, font_size)
    self.image = self.font.render("Score: 5", True, pygame.Color(color))
    self.rect = self.image.get_rect()
    self.rect.center = center

  def blit(self):
    Globals.display.blit(self.image, self.rect)