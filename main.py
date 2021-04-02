import pygame
import sys

from helpers.settings import Settings
from entities.player import Player
from entities.platform import Platform
from entities.laser import Laser
from scoreboard import Scoreboard

class Main():
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.display = pygame.display.set_mode(
      (Settings.screen_width, Settings.screen_height))
    self.display_rect = self.display.get_rect()
    self.platforms = Platform.create_platforms(self.display)
    self.player = Player(self.display, self.platforms)
    self.scoreboard = Scoreboard(self.display, self.player)
    self.lasers = pygame.sprite.Group()
    self.level_timer = 0

  def check_events(self):
    """Handles pygame events, such as quitting and keydowns"""
    for event in pygame.event.get():
      # Meta
      if event.type == pygame.QUIT:
        Settings.running = False
      # Keydown
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          Settings.running = False
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
    self.level_timer -= 1 / Settings.fps
    if self.level_timer <= 0:
      Laser.generate_lasers(self.lasers, self.display, self.player)
      self.level_timer = 1.25

  def draw_and_update(self):
    """Updates game objects and re-renders screen"""
    self.display.fill(pygame.Color("#111111"))
    for platform in self.platforms:
      platform.draw()
    if self.lasers != None:
      for laser in self.lasers:
        laser.update()
        laser.draw()
    self.player.update()
    self.player.draw()
    self.scoreboard.update()
    self.scoreboard.blit()
    pygame.display.update()

  def run(self):
    """Runs main game"""
    while Settings.running:
      # Events, timers, and inputs
      self.clock.tick(Settings.fps)
      self.check_events()
      if not Settings.game_over:
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