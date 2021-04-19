import pygame
from functools import partial

from utils.globals import Globals
from utils.task import Task
from entities.entity import Entity

class Platform(Entity):
  def __init__(self, x, y, width, height, vel=(0, 0), breakable=False):
    self.breakable = breakable
    self.breaking = False
    self.color = "#dddddd"

    # Rect
    super().__init__(self.color, x, y, width, height)
    self.vel.x = vel[0]
    self.vel.y = vel[1]
  
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
    super().update()
    if self.breaking:
      self.tasks.update()