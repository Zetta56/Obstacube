import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task

class Platform(pygame.sprite.Sprite):
  """
  Defines basic platforms. This also manages platform groups and doesn't 
  inherit from entity, since it's required within entity
  """
  @classmethod
  def reset_group(cls):
    cls.group = pygame.sprite.Group()
    cls.group.add(Platform(0, Globals.floor_y, Globals.display_rect.width, 
      Globals.display_rect.height - Globals.floor_y))
    #cls.group.add(Platform(350, 500, 120, 50, 0.1, 0))

  def __init__(self, x, y, width, height, velx=0, vely=0, breakable=False):
    super().__init__()
    self.color = "#dddddd"
    self.rect = pygame.Rect(x, y, width, height)
    self.pos = pygame.Vector2(self.rect.x, self.rect.y)
    self.vel = pygame.Vector2(velx, vely)
    self.tasks = pygame.sprite.Group()

    # Breaking
    self.visible = True
    self.breakable = breakable
    self.breaking = False
  
  def schedule(self):
    def toggle_visible(visibility):
      self.visible = visibility

    if self.breakable and not self.breaking:
      self.breaking = True
      self.tasks.add(
        Task(partial(toggle_visible, False), loops=4, loop_timer=0.25),
        Task(partial(toggle_visible, True), delay=0.125, loops=3, loop_timer=0.25),
        Task(self.kill, delay=1)
      )

  def update(self):
    if self.breaking:
      self.tasks.update()
    self.pos += self.vel
    self.rect.x = self.pos.x
    self.rect.y = self.pos.y

  def draw(self):
    if self.visible:
      pygame.draw.rect(Globals.display, pygame.Color(self.color), self.rect)