import pygame
from menus.button import Button
from menus.text import Text

class Results():
  def __init__(self, display):
    # Tab
    self.display = display
    self.tab_color = "#555555"
    self.tab_rect = pygame.Rect(0, 0, 400, 400)
    self.tab_rect.center = self.display.get_rect().center

    # Content
    def printa():
      print("a")

    self.score = Text(self.display, (self.tab_rect.centerx, 
      self.tab_rect.top + 80), 48)
    self.replay_button = Button(self.display, (self.tab_rect.centerx, 
      self.tab_rect.bottom - 80), "#55dd55", "Replay", printa)

  def blit(self):
    self.display.fill(self.tab_color, self.tab_rect)
    self.score.blit()
    self.replay_button.blit()