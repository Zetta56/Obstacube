import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task
from entities.entity import Entity
from entities.platform import Platform

class Player(Entity):
  def __init__(self, platforms, scoreboard):
    # Settings
    self.color = "#dddddd"
    self.start_x = Globals.display_rect.width / 2
    self.start_y = 500
    self.size = 30
   # self.gravity = 0.2
    self.speed = 5
    self.jump_power = 7.5
    self.max_jumps = 1

    # Rects
    self.platforms = Platform.group
    self.scoreboard = scoreboard
    super().__init__(self.color, self.start_x, self.start_y, 
                     self.size, self.size, use_physics=True)
    
    # State
    #self.onGround = False
    self.jumps = self.max_jumps
    self.intangible = False

  def schedule(self):
    def toggle_visible(visibility):
      self.visible = visibility

    def toggle_tangible(tangibility):
      self.intangible = not tangibility

    self.tasks.add(
      Task(partial(toggle_visible, False), loops=3, loop_timer=0.5),
      Task(partial(toggle_visible, True), delay=0.25, loops=3, loop_timer=0.5),
      Task(partial(toggle_tangible, True), delay=1.5)
    )

  def jump(self):
    """Jump at constant velocity if conditions are met"""
    if self.onGround and self.jumps > 0:
      self.vel.y = -1 * self.jump_power
      self.jumps -= 1
      self.onGround = False

  def hit(self):
    if not self.intangible:
      Globals.lives -= 1
      self.scoreboard.update_lives()
      self.intangible = True

      if Globals.lives > 0: 
        self.schedule()
      else: 
        self.visible = False
        Globals.game_over = True

  def update(self):
    self.tasks.update()
    if self.onGround:
      self.jumps = self.max_jumps
    
    # Update player's position before collision detection
    super().update()
    self.detect_platforms()