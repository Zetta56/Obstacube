import pygame
from utils.globals import Globals
from menus.button import Button
from menus.text import Text

class Pause():
  def __init__(self):
    # Tab
    self.tab_color = "#555555"
    self.tab_rect = pygame.Rect(0, 0, 300, 300)
    self.tab_rect.center = Globals.display_rect.center

    def resume():
      if Globals.paused:
        Globals.paused = False
    
    def exit():
      if Globals.paused:
        Globals.running = False

    self.message = Text("Paused", 48, (self.tab_rect.centerx, 
      self.tab_rect.centery - 80))
    self.resume_button = Button("Resume", "#22aa22", resume,
      (self.tab_rect.centerx, self.tab_rect.centery + 10), font_size=24)
    self.exit_button = Button("Exit", "#777777", exit,
      (self.tab_rect.centerx, self.tab_rect.centery + 80), font_size=24)

  def blit(self):
    Globals.display.fill(self.tab_color, self.tab_rect)
    self.message.blit()
    self.resume_button.blit()
    self.exit_button.blit()