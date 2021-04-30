import pygame
from utils.globals import Globals
from utils.helpers import save_score
from utils.task import Task
from interfaces.button import Button

class Results():
  def __init__(self, function):
    # Tab
    self.tab_color = "#555555"
    self.text_color = "#dddddd"
    self.tab_rect = pygame.Rect(0, 0, 400, 400)
    self.tab_rect.center = Globals.display_rect.center
      
    # Message
    self.message_font = pygame.font.Font("assets/russo_one.ttf", 54)
    self.message = self.message_font.render("Game Over", True, 
      pygame.Color(self.text_color))
    self.message_rect = self.message.get_rect()
    self.message_rect.center = (self.tab_rect.centerx, self.tab_rect.top + 80)

    # Scores
    self.score_font = pygame.font.Font("assets/russo_one.ttf", 36)
    self.update_score()
    self.high_score_font = pygame.font.Font("assets/russo_one.ttf", 24)
    self.update_high_score()

    # Button
    def reset():
      if Globals.game_over: 
        function()
    self.replay_button = Button("Replay", "#22aa22", reset,
      (self.tab_rect.centerx, self.tab_rect.bottom - 80))
    self.schedule()

  def schedule(self):
    def blit_tab():
      save_score()
      Globals.display.fill(self.tab_color, self.tab_rect)
      Globals.display.blit(self.message, self.message_rect)

    def blit_content():
      self.update_score()
      self.update_high_score()
      Globals.display.blit(self.score, self.score_rect)
      Globals.display.blit(self.high_score, self.high_score_rect)
      self.replay_button.blit()

    self.tasks = pygame.sprite.Group()
    self.tasks.add(
      Task(blit_tab, delay=0.75),
      Task(blit_content, delay=1.5)
    )

  def update_score(self):
    """Re-renders score"""
    self.score = self.score_font.render(f"Score: {Globals.score}",
      True, pygame.Color(self.text_color))
    self.score_rect = self.score.get_rect()
    self.score_rect.center = (self.tab_rect.centerx, self.tab_rect.centery - 25)

  def update_high_score(self):
    """Re-renders high score"""
    high_score = max(Globals.score, Globals.high_score)
    self.high_score = self.high_score_font.render(f"Best Score: {high_score}",
      True, pygame.Color(self.text_color))
    self.high_score_rect = self.high_score.get_rect()
    self.high_score_rect.center = (self.tab_rect.centerx, self.tab_rect.centery + 25)