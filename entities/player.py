import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task
from utils.sounds import Sounds
from interfaces.status_effect import StatusEffect
from entities.entity import Entity
from entities.platform import Platform

class Player(Entity):
  def __init__(self, platforms, scoreboard):
    # Settings
    self.color = "#dddddd"
    self.start_x = Globals.display_rect.width / 2
    self.start_y = 500
    self.size = 30
    self.speed = 5
    self.jump_power = 7.5
    self.max_jumps = 1
    self.max_lives = 3

    # References
    self.scoreboard = scoreboard
    super().__init__(self.color, self.start_x, self.start_y, 
      self.size, self.size, platforms=platforms, physics=True)

    # State
    self.jumps = self.max_jumps
    self.lives = self.max_lives
    self.intangible = False

  def schedule(self):
    def toggle_visible(visibility):
      self.visible = visibility

    def toggle_tangible():
      if not any(status_effect for status_effect in StatusEffect.group
          if status_effect.name == "shield"):
        self.intangible = False

    self.tasks.add(
      Task(partial(toggle_visible, False), loops=3, loop_timer=0.5),
      Task(partial(toggle_visible, True), delay=0.25, loops=3, loop_timer=0.5),
      Task(toggle_tangible, delay=1.5)
    )

  def jump(self):
    """Jump at constant velocity if player still has jumps"""
    if self.jumps > 0:
      self.vel.y = -1 * self.jump_power
      self.jumps -= 1
      self.onGround = False

  def hit(self):
    if not self.intangible:
      self.lives -= 1
      self.scoreboard.update_lives(self.lives)
      self.intangible = True
      Sounds.hit.play()

      if self.lives > 0: 
        self.schedule()
      else: 
        self.visible = False
        Globals.game_over = True

  def update(self):
    self.tasks.update()
    if self.onGround:
      self.jumps = self.max_jumps
    super().update()