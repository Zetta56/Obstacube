import pygame
from utils.globals import Globals 
from menus.text import Text

class Button(pygame.sprite.Sprite):
  button_group = pygame.sprite.Group()

  @classmethod
  def add_to_group(cls, button):
    # Group used to detect click events in main loop
    cls.button_group.add(button)

  def __init__(self, text, color, function, center, width=200, 
      height=60, text_color="#dddddd", font_size=28):
    super().__init__()
    # Button
    self.button_color = color
    self.button_rect = pygame.Rect(0, 0, width, height)
    self.button_rect.center = center
    self.text = Text(text, font_size, self.button_rect.center)
    self.function = function

    # Grouping
    self.add_to_group(self)

  def blit(self):
    Globals.display.fill(self.button_color, self.button_rect)
    self.text.blit()