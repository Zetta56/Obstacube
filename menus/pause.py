import pygame
from utils.globals import Globals
from menus.button import Button

class Pause():
  def __init__(self):
    # Tab
    self.tab_color = "#555555"
    self.tab_rect = pygame.Rect(0, 0, 300, 300)
    self.tab_rect.center = Globals.display_rect.center

    # Message
    self.font = pygame.font.Font("assets/russo_one.ttf", 48)
    self.message = self.font.render("Paused", True, pygame.Color("#dddddd"))
    self.message_rect = self.message.get_rect()
    self.message_rect.center = (self.tab_rect.centerx, self.tab_rect.centery - 80)

    # Resume Button
    def resume():
      if Globals.paused: Globals.paused = False
    self.resume_button = Button("Resume", "#22aa22", resume,
      (self.tab_rect.centerx, self.tab_rect.centery + 10), font_size=24)
    
    # Exit Button
    def exit():
      if Globals.paused: Globals.running = False
    self.exit_button = Button("Exit", "#777777", exit,
      (self.tab_rect.centerx, self.tab_rect.centery + 80), font_size=24)

  def blit(self):
    Globals.display.fill(self.tab_color, self.tab_rect)
    Globals.display.blit(self.message, self.message_rect)
    self.resume_button.blit()
    self.exit_button.blit()