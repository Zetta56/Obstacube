import pygame
from random import choice
from functools import partial

from utils.globals import Globals
from utils.task import Task
from utils.helpers import draw_polygon
from entities.entity import Entity

class Rock(Entity):
  def __init__(self, player, platforms, x):
    self.color = "#ee5555"
    self.size = 30
    self.speed = 10

    super().__init__(self.color, x, -1 * self.size, self.size, self.size)
    self.player = player
    self.platforms = platforms
    self.can_drop = False
    self.schedule()

  def schedule(self):
    def slide_down(duration):
      self.position.y += (0.5 * self.size) / (duration * Globals.fps)
      self.rect.y = self.position.y

    def wiggle_left(distance):
      self.position.x -= distance
      self.rect.x = self.position.x

    def wiggle_right(distance):
      self.position.x += distance
      self.rect.x = self.position.x

    def drop():
      self.can_drop = True

    self.tasks.add(
      Task(partial(slide_down, 1), duration=1),
      Task(partial(wiggle_left, 5), delay=1, loops=5, loop_timer=0.2),
      Task(partial(wiggle_right, 5), delay=1.1, loops=5, loop_timer=0.2),
      Task(drop, delay=2.1)
    )

  def update(self):
    # Movement
    self.tasks.update()
    if self.can_drop:
      self.position.y += self.speed
      self.rect.y = self.position.y

    # Collisions
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()
      self.kill()
    if pygame.sprite.spritecollideany(self, self.platforms):
      self.kill()

  def draw(self):
      draw_polygon(self.rect, self.color, num_sides=3, rotation=30)