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

    # Static Content
    def reset():
      if Globals.game_over: 
        Globals.game_over = False
        function()
    self.message = Text("Game Over", 54, (self.tab_rect.centerx, 
      self.tab_rect.top + 80))
    self.get_scores()
    self.replay_button = Button("Replay", "#22aa22", reset,
      (self.tab_rect.centerx, self.tab_rect.bottom - 80))
    self.schedule()

  def schedule(self):
    def blit_tab():
      Globals.display.fill(self.tab_color, self.tab_rect)
      self.message.blit()

    def blit_content():
      self.score.blit()
      self.high_score.blit()
      self.replay_button.blit()

    self.tasks = pygame.sprite.Group()
    self.tasks.add(
      Task(blit_tab, delay=0.75, loops=True),
      Task(blit_content, delay=1.5, loops=True)
    )

  def get_scores(self):
    """Updated high score and renders scores"""
    if Globals.score > Globals.high_score:
      with open("high_score.txt", "w") as f:
        f.write(str(Globals.score))
    high_score = max(Globals.score, Globals.high_score)

    self.score = Text(f"Score: {Globals.score}", 36, 
      (self.tab_rect.centerx, self.tab_rect.centery - 25))
    self.high_score = Text(f"Best Score: {high_score}", 24, 
      (self.tab_rect.centerx, self.tab_rect.centery + 25))

  def update(self):
    self.get_scores()
    self.tasks.update()