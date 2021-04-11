import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task

class Platform(pygame.sprite.Sprite):
  @classmethod
  def reset_group(cls):
    cls.group = pygame.sprite.Group()
    cls.group.add(Platform(0, Globals.display_rect.height - 40, 
      Globals.display_rect.width, 40))
    #cls.group.add(Platform(350, 450, 150, 50))

  def __init__(self, x, y, width, height, velx=0, vely=0, breakable=False):
    super().__init__()
    self.color = "#dddddd"
    self.rect = pygame.Rect(x, y, width, height)
    self.vel = pygame.Vector2(velx, vely)
    self.tasks = pygame.sprite.Group()

    # Breaking
    self.visible = True
    self.breakable = breakable
    self.breaking = False
  
  def destroy(self):
    def toggle_visible(visibility):
      self.visible = visibility

    if not self.breaking:
      self.breaking = True
      self.tasks.add(
        Task(partial(toggle_visible, False), loops=4, loop_timer=0.25),
        Task(partial(toggle_visible, True), delay=0.125, loops=3, loop_timer=0.25),
        Task(self.kill, delay=1)
      )

  def update(self):
    if self.breaking:
      self.tasks.update()
    self.rect.x += self.vel.x
    self.rect.y += self.vel.y

  def draw(self):
    if self.visible:
      pygame.draw.rect(Globals.display, pygame.Color(self.color), self.rect)