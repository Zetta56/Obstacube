import pygame
from utils.globals import Globals
from menus.button import Button

class Start():
  def __init__(self):
    # Title
    self.font = pygame.font.Font("assets/russo_one.ttf", 72)
    self.title = self.font.render("Obstacube", True, pygame.Color("#dddddd"))
    self.title_rect = self.title.get_rect()
    self.title_rect.center = (Globals.display_rect.centerx, 
      Globals.display_rect.centery - 60)

    # Button
    def start():
      Globals.playing = True
    self.start_button = Button("Play", "#22aa22", start,
      (Globals.display_rect.centerx, Globals.display_rect.centery + 60))

  def blit(self):
    Globals.display.blit(self.title, self.title_rect)
    self.start_button.blit()