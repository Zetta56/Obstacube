import pygame
from functools import partial

from entities.entity import Entity
import utils.effects as effects
from utils.globals import Globals
from utils.task import Task

class Player(Entity):
  def __init__(self, display, platforms):
    # Settings
    self.color = "#dddddd"
    self.start_x = display.get_rect().width / 2
    self.start_y = 500
    self.size = 30
    self.gravity = 0.2
    self.speed = 5
    self.jump_power = 7.5
    self.lives = 1
    self.max_jumps = 1

    # Rects
    self.platforms = platforms
    super().__init__(display, self.color, self.start_x, self.start_y, 
                     self.size, self.size)
    
    # State
    self.onGround = False
    self.jumps = self.max_jumps
    self.intangible = False

  def jump(self):
    """Jump at constant velocity if conditions are met"""
    if self.onGround and self.jumps > 0:
      self.lives -= 1
      self.velocity.y = -1 * self.jump_power
      self.jumps -= 1
      self.onGround = False

  def hit(self):
    if not self.intangible:
      self.intangible = True
      self.lives -= 1

      if self.lives > 0:
        self.tasks.add(
          Task(partial(effects.toggle_visible, self, False), loops=3, loop_timer=0.5),
          Task(partial(effects.toggle_visible, self, True), delay=0.25, loops=3, loop_timer=0.5),
          Task(partial(effects.toggle_tangible, self, True), delay=1.5)
        )
      else:
        Globals.game_over = True
 
  def detect_platforms(self):
    """Stop player from crashing into platforms"""
    platform = pygame.sprite.spritecollideany(self, self.platforms)
    if platform:
      # Check which side player came from at previous frame
      if self.rect.right - self.velocity.x <= platform.rect.left:
        self.position.x = platform.rect.left - self.rect.width
        self.velocity.x = 0
      if self.rect.left - self.velocity.x >= platform.rect.right:
        self.position.x = platform.rect.right
        self.velocity.x = 0
      # Adding 1 in order to pass spritecollideany check
      if self.rect.bottom - self.velocity.y <= platform.rect.top + 1:
        self.position.y = platform.rect.top - self.rect.height + 1
        self.velocity.y = 0
        self.jumps = self.max_jumps
        self.onGround = True
      if self.rect.top - self.velocity.y >= platform.rect.bottom:
        self.position.y = platform.rect.bottom
        self.velocity.y = 0
      
      # Apply position changes
      self.rect.x = self.position.x
      self.rect.y = self.position.y
    else:
      self.onGround = False

  def update(self):
    self.tasks.update()
    # Apply gravity if player isn't touching top of platform
    if not self.onGround:
      self.velocity.y += self.gravity
    
    # Update position and rect before collision detection
    self.position += self.velocity
    self.rect.x = self.position.x
    self.rect.y = self.position.y
    self.detect_platforms()