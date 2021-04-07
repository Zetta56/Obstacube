import pygame
import sys

from utils.globals import Globals
from entities.player import Player
from entities.platform import Platform
from entities.laser import Laser
from menus.scoreboard import Scoreboard
from menus.button import Button
from menus.start import Start
from menus.results import Results
from menus.pause import Pause

class Main():
  def __init__(self):
    self.clock = pygame.time.Clock()
    self.reset_game()
  
  def reset_game(self):
    """Resets game objects, game-state, and tasks"""
    Globals.reset_state()
    self.platforms = Platform.create_platforms()
    self.player = Player(self.platforms)
    self.lasers = pygame.sprite.Group()
    self.start = Start()
    self.pause = Pause()
    self.scoreboard = Scoreboard()
    self.results = Results(self.reset_game)

  def check_events(self):
    """Handles pygame events, such as quitting and keydowns"""
    for event in pygame.event.get():
      # Meta
      if event.type == pygame.QUIT:
        Globals.running = False
      # Mouse
      if event.type == pygame.MOUSEBUTTONDOWN:
        for button in Button.button_group:
          if button.button_rect.collidepoint(pygame.mouse.get_pos()):
            button.function()
      # Keydown
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          Globals.running = False
        if event.key == pygame.K_RETURN:
          if not Globals.playing: self.start.start_button.function()
          if Globals.game_over: self.results.replay_button.function()
        if event.key == pygame.K_ESCAPE:
          if Globals.playing and not Globals.game_over:
            Globals.paused = not Globals.paused
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          self.player.jump()

  def check_inputs(self):
    """Responds to keypress inputs"""
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and self.player.rect.left > Globals.display_rect.left:
      self.player.velocity.x = -1 * self.player.speed
    elif key[pygame.K_RIGHT] and self.player.rect.right < Globals.display_rect.right:
      self.player.velocity.x = self.player.speed
    else:
      self.player.velocity.x = 0

  def generate_level(self):
    Globals.level_timer -= 1 / Globals.fps
    if Globals.level_timer <= 0:
      Laser.generate_lasers(self.lasers, self.player)
      Globals.level_timer = 1.25

  def update(self):
    Globals.score += Globals.score_rate
    self.lasers.update()
    self.player.update()
    self.scoreboard.update()

  def draw(self):
    Globals.display.fill(pygame.Color(Globals.bg_color))
    for platform in self.platforms: platform.draw()
    for laser in self.lasers: laser.draw()
    self.player.draw()
    self.scoreboard.blit()

  def run(self):
    """Runs main game"""
    while Globals.running:
      self.clock.tick(Globals.fps)
      self.check_events()
      
      if not Globals.playing:
        self.start.blit()
      elif Globals.paused:
        self.pause.blit()
      elif Globals.game_over:
        self.player.visible = False
        self.draw()
        self.results.update()
      else:
        self.check_inputs()
        self.update()
        self.draw()
        self.generate_level()
      pygame.display.update()
      

# Runs game if this file is called directly
if __name__ == "__main__":
  pygame.init()
  game = Main()
  game.run()
  # Properly close game
  pygame.quit()
  sys.exit()