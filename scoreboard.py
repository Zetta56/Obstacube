import pygame

class Scoreboard():
  def __init__(self, display, player):
    self.color = "#dddddd"
    self.font = pygame.font.SysFont(None, 24)

    self.display = display
    self.player = player

    self.lives = self.player.lives
    self.lives_image = self.font.render(f'Lives: {self.player.lives}', 
      True, pygame.Color(self.color))

  def update(self):
    if self.player.lives != self.lives:
      self.lives = self.player.lives
      self.lives_image = self.font.render(f'Lives: {self.player.lives}', 
        True, pygame.Color(self.color))

  def blit(self):
    self.display.blit(self.lives_image, (30, 30))