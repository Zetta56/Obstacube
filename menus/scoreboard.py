import pygame

class Scoreboard():
  def __init__(self, display, player):
    # Settings
    self.color = "#dddddd"
    self.font = pygame.font.SysFont(None, 32)

    # Rects
    self.display = display
    self.player = player

    # Info
    self.lives = self.player.lives
    self.lives_image = self.font.render(f'Lives: {self.lives}', 
      True, pygame.Color(self.color))

  def update(self):
    if self.player.lives != self.lives:
      self.lives = self.player.lives
      self.lives_image = self.font.render(f'Lives: {self.lives}', 
        True, pygame.Color(self.color))

  def blit(self):
    self.display.blit(self.lives_image, (20, 20))