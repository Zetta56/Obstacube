import pygame
from utils.globals import Globals
from menus.button import Button
from menus.text import Text

class Results():
  def __init__(self):
    # Tab
    self.tab_color = "#555555"
    self.tab_rect = pygame.Rect(0, 0, 400, 400)
    self.tab_rect.center = Globals.display_rect.center

    # Content
    def printa():
      print("a")

    self.score = Text((self.tab_rect.centerx, self.tab_rect.top + 80), 48)
    self.replay_button = Button((self.tab_rect.centerx, 
      self.tab_rect.bottom - 80), "#55dd55", "Replay", printa)

  def blit(self):
    Globals.display.fill(self.tab_color, self.tab_rect)
    self.score.blit()
    self.replay_button.blit()