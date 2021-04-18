import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task
from utils.helpers import draw_polygon
from entities.entity import Entity
from entities.platform import Platform

class Rock(Entity):
  def __init__(self, player, platforms, x):
    self.color = "#ee5555"
    self.size = 30
    self.speed = 10

    super().__init__(self.color, x, -1 * self.size, self.size, self.size)
    self.player = player
    self.platforms = platforms
    self.schedule()

  def schedule(self):
    def slide_down(duration):
      self.pos.y += (0.5 * self.size) / (duration * Globals.fps)
      self.rect.y = self.pos.y

    def wiggle_left(distance):
      self.pos.x -= distance
      self.rect.x = self.pos.x

    def wiggle_right(distance):
      self.pos.x += distance
      self.rect.x = self.pos.x

    def drop():
      self.vel.y = self.speed

    self.tasks.add(
      Task(partial(slide_down, 1), duration=1),
      Task(partial(wiggle_left, 5), delay=1, loops=5, loop_timer=0.2),
      Task(partial(wiggle_right, 5), delay=1.1, loops=5, loop_timer=0.2),
      Task(drop, delay=2.1)
    )

  def update(self):
    self.tasks.update()
    super().update()

    # Collisions
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()
      self.kill()
    if pygame.sprite.spritecollideany(self, self.platforms):
      self.kill()

  def draw(self):
      draw_polygon(self.rect, self.color, num_sides=3, rotation=30)