import pygame
import sys

from player import Player
from platform import Platform
from laser import Laser
from helpers import *
from constants import *

class Main():
  def __init__(self):
    self.clock = pygame.time.Clock()
    self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.display_rect = self.display.get_rect()
    self.platforms = Platform.create_platforms(self.display)
    self.lasers = Laser.generate_lasers(self.display)
    self.player = Player(self.display, self.platforms)
    self.seconds = 0
    self.running = True

  def check_events(self):
    """Handles pygame events, such as quitting and keydowns"""
    for event in pygame.event.get():
      # Meta
      if event.type == pygame.QUIT:
        self.running = False
      # Keydown
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.running = False
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          self.player.jump()

  def check_inputs(self):
    """Responds to keypress inputs"""
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and self.player.rect.left > self.display_rect.left:
      self.player.velocity.x = -1 * self.player.speed
    elif key[pygame.K_RIGHT] and self.player.rect.right < self.display_rect.right:
      self.player.velocity.x = self.player.speed
    else:
      self.player.velocity.x = 0

  def generate_level(self):
    if self.seconds > 2:
      self.lasers = Laser.generate_lasers(self.display)
      self.seconds -= 2

  def draw_and_update(self):
    """Updates game objects and re-renders screen"""
    self.display.fill(pygame.Color("#111111"))
    for platform in self.platforms:
      platform.draw()
    for laser in self.lasers:
      laser.update()
      laser.draw()
    self.player.update()
    self.player.draw()
    pygame.display.update()

  def run(self):
    """Runs main game"""
    pygame.init()
    while self.running:
      # Events, timers, and inputs
      self.clock.tick(FPS)
      self.seconds += 1 / FPS
      self.check_events()
      self.check_inputs()
      # Updating screen
      self.generate_level()
      self.draw_and_update()

# Runs game if this file is called directly
if __name__ == "__main__":
  game = Main()
  game.run()
  # Properly close game
  pygame.quit()
  sys.exit()