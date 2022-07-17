import pygame
import sys

from utils.globals import Globals
from utils.helpers import save_score
from utils.spawner import Spawner
from utils.sounds import Sounds
from interfaces.scoreboard import Scoreboard
from interfaces.button import Button
from interfaces.start import Start
from interfaces.results import Results
from interfaces.status_effect import StatusEffect
from interfaces.pause import Pause
from entities.bullet import Bullet

class Main():
  def __init__(self):
    self.clock = pygame.time.Clock()
    self.reset_game()
  
  def reset_game(self):
    """Resets game objects, game-state, and tasks"""
    Globals.reset()
    Button.reset()
    Bullet.reset()
    StatusEffect.reset()
    self.scoreboard = Scoreboard()
    self.spawner = Spawner(self.scoreboard)
    self.player = self.spawner.player
    self.scoreboard.update_lives(self.player.lives)
    self.start = Start()
    self.pause = Pause()
    self.results = Results(self.reset_game)

  def check_events(self):
    """Handles pygame events, such as quitting and keydowns"""
    for event in pygame.event.get():
      # Meta
      if event.type == pygame.QUIT:
        Globals.running = False
      # Mouse
      if event.type == pygame.MOUSEBUTTONDOWN:
        for button in Button.list:
          if button.button_rect.collidepoint(pygame.mouse.get_pos()):
            button.function()
      # Keydown
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          Globals.running = False
        if event.key == pygame.K_RETURN:
          if not Globals.playing: 
            self.start.start_button.function()
          if Globals.game_over: 
            self.results.replay_button.function()
        if event.key == pygame.K_ESCAPE:
          if Globals.playing and not Globals.game_over:
            Globals.paused = not Globals.paused
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          self.player.jump()

  def check_inputs(self):
    """Responds to keypress inputs"""
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and self.player.rect.left > Globals.display_rect.left:
      self.player.vel.x = -1 * self.player.speed
    elif key[pygame.K_RIGHT] and self.player.rect.right < Globals.display_rect.right:
      self.player.vel.x = self.player.speed
    else:
      self.player.vel.x = 0

  def update(self):
    """Updates game objects"""
    Globals.score += Globals.score_rate
    StatusEffect.group.update()
    Bullet.group.update()
    self.scoreboard.update_score()
    self.spawner.update()

  def draw(self):
    """Rerenders game objecs and screen"""
    Globals.display.fill(pygame.Color(Globals.bg_color))
    for platform in self.spawner.platforms: platform.draw()
    self.spawner.items.draw(Globals.display)
    self.player.draw()
    for obstacle in self.spawner.obstacles: obstacle.draw()
    for bullet in Bullet.group: bullet.draw()
    self.scoreboard.blit()
    for status_effect in StatusEffect.group:
      status_effect.draw()

  def run(self):
    """Runs main game"""
    Sounds.bgm.play(-1)
    while Globals.running:
      self.clock.tick(Globals.fps)
      self.check_events()
      
      if not Globals.playing:
        self.start.blit()
      elif Globals.paused:
        self.pause.blit()
      elif Globals.game_over:
        self.results.tasks.update()
      else:
        self.check_inputs()
        self.update()
        self.draw()
      pygame.display.update()
      

# Runs game if this file is called directly
if __name__ == "__main__":
  pygame.init()
  game = Main()
  game.run()
  # Properly close game
  save_score()
  pygame.quit()
  sys.exit()