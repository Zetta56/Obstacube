import pygame
from utils.globals import Globals 

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

    # Text
    self.font = pygame.font.Font("assets/russo_one.ttf", font_size)
    self.text = self.font.render(text, True, pygame.Color(text_color))
    self.text_rect = self.text.get_rect()
    self.text_rect.center = center

    # Actions
    self.function = function
    self.add_to_group(self)

  def blit(self):
    Globals.display.fill(self.button_color, self.button_rect)
    Globals.display.blit(self.text, self.text_rect)