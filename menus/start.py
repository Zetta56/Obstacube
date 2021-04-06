import pygame
from utils.globals import Globals
from menus.button import Button
from menus.text import Text

class Start():
  def __init__(self):
    def start():
        Globals.playing = True

    self.title = Text("Obstacube", 72, (Globals.display_rect.centerx, 
      Globals.display_rect.centery - 60))
    self.start_button = Button("Play", "#22aa22", start,
      (Globals.display_rect.centerx, Globals.display_rect.centery + 60))

  def blit(self):
    self.title.blit()
    self.start_button.blit()