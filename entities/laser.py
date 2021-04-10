import pygame
from functools import partial
from random import randrange

from utils.globals import Globals
from entities.entity import Entity
from utils.task import Task

class Laser(Entity):
  def __init__(self, player, x):
    # Settings
    self.color = "#ee5555"
    self.width = 50
    self.intangible = True

    # Rects
    self.player = player
    super().__init__(self.color, x + self.width / 2, 0, 1, 
      Globals.display_rect.height)
    self.schedule()
  
  def schedule(self):
    def expand_horizontal(duration):
      expansion_size = self.width / Globals.fps * duration
      self.position.x -= expansion_size / 2
      self.rect.x = self.position.x
      self.length.x += expansion_size
      self.rect.width = self.length.x

    def hide():
      self.visible = False

    def flash(expansion_size):
      self.visible = True
      self.color = "#ffffff"
      self.rect.width = self.length.x + expansion_size
      self.rect.x = self.position.x - expansion_size / 2
      self.intangible = False

    self.tasks.add(
      Task(partial(expand_horizontal, 1), duration=1), 
      Task(partial(hide), delay=1), 
      Task(partial(flash, 10), delay=1.1),
      Task(self.kill, delay=1.3)
    )

  def update(self):
    self.tasks.update()
    if not self.intangible and pygame.sprite.collide_rect(self, self.player):
      self.player.hit()