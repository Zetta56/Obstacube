import pygame

from utils.globals import Globals
from utils.task import Task
from entities.entity import Entity

class Bullet(Entity):
  @classmethod
  def reset(cls):
    cls.group = pygame.sprite.Group()

  def __init__(self, player, radius, x, y, velx, vely):
    # Settings
    self.color = "#ee5555"
    self.radius = radius
    self.player = player

    # Vectors
    super().__init__(self.color, x, y, self.radius, self.radius)
    self.vel.x = velx
    self.vel.y = vely

  def update(self):
    super().update()
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()
      self.kill()

  def draw(self):
      pygame.draw.circle(Globals.display, self.color, self.rect.center, self.radius)