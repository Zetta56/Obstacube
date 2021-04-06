import pygame
from utils.globals import Globals
from utils.task import Task
from menus.button import Button
from menus.text import Text

class Results():
  def __init__(self, function):
    # Tab
    self.tab_color = "#555555"
    self.tab_rect = pygame.Rect(0, 0, 400, 400)
    self.tab_rect.center = Globals.display_rect.center

    # Content
    def reset():
      if Globals.game_over:
        Globals.lives = Globals.max_lives
        Globals.game_over = False
        function()

    self.message = Text("Game Over", 54, (self.tab_rect.centerx, 
      self.tab_rect.top + 80))
    self.score = Text("Score: 5", 36, (self.tab_rect.centerx, 
      self.tab_rect.centery - 25))
    self.high_score = Text("Best Score: 10", 24, (self.tab_rect.centerx, 
      self.tab_rect.centery + 25))
    self.replay_button = Button("Replay", "#22aa22", reset,
      (self.tab_rect.centerx, self.tab_rect.bottom - 80))

    # Tasks
    def blit_content():
      self.score.blit()
      self.high_score.blit()
      self.replay_button.blit()

    self.tasks = pygame.sprite.Group()
    self.tasks.add(Task(blit_content, delay=1, loops=True))

  def blit(self):
    Globals.display.fill(self.tab_color, self.tab_rect)
    self.message.blit()