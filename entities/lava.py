import pygame
from utils.globals import Globals
from utils.task import Task
from entities.entity import Entity

class Lava(Entity):
  def __init__(self, player):
    # Settings
    self.color = "#eb4034"
    super().__init__(self.color, 0, Globals.display_rect.bottom, 
      Globals.display_rect.width, 100)
    self.player = player
    self.vel.y = -0.5
    self.schedule()

  def schedule(self):
    def stabilize():
      self.vel.y = 0

    def fall():
      self.vel.y = 2

    self.tasks.add(Task(stabilize, delay=2))
    self.tasks.add(Task(fall, delay=4))

  def update(self):
    self.tasks.update()

    # Update position and check for collisions
    super().update()
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()