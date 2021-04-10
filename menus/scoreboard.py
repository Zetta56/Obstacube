import pygame
from utils.globals import Globals

class Scoreboard():
  def __init__(self):
    # Settings
    self.text_color = "#dddddd"
    self.font = pygame.font.Font("assets/russo_one.ttf", 28)
    self.update_lives()
    self.update_score()

  def update_lives(self):
    """Re-renders lives"""
    self.lives = self.font.render(f'Lives: {Globals.lives}', True, 
      pygame.Color(self.text_color))
    self.lives_rect = self.lives.get_rect()
    self.lives_rect.topleft = (Globals.display_rect.top + 20, 20)

  def update_score(self):
    """Re-renders score"""
    self.score = self.font.render(f'Score: {Globals.score}', True, 
      pygame.Color(self.text_color))
    self.score_rect = self.score.get_rect()
    self.score_rect.topright = (Globals.display_rect.right - 20, 20)

  def blit(self):
    Globals.display.blit(self.lives, self.lives_rect)
    Globals.display.blit(self.score, self.score_rect)