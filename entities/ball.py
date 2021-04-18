import pygame
import math
from random import randrange

from utils.globals import Globals
from utils.task import Task
from utils.helpers import draw_polygon
from entities.entity import Entity

class Ball(Entity):
  def __init__(self, player, speed):
    # Settings
    self.color = "#ee5555"
    self.size = 40
    self.rotation = 0
    self.rotation_rate = 10
    self.jump_power = 3
    self.player = player

    # Positioning
    if speed > 0: 
      self.rotation_rate *= -1
      x = Globals.display_rect.left - self.size
    else: 
      x = Globals.display_rect.right
    super().__init__(self.color, x, Globals.floor_y - self.size, 
      self.size, self.size, use_physics=True)
    self.vel.x = speed

  def update(self):
    self.tasks.update()
    self.rotation += self.rotation_rate
    if self.onGround:
      self.vel.y = -1 * self.jump_power

    # Update position and check for collisions
    super().update()
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()

  def draw(self):
      draw_polygon(self.rect, self.color, num_sides=6, rotation=self.rotation)