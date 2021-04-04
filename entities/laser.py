import pygame
from functools import partial
from random import randrange

from entities.entity import Entity
import utils.effects as effects
from utils.globals import Globals
from utils.task import Task

class Laser(Entity):
  @staticmethod
  def generate_lasers(group, display, player):
    for i in range(randrange(2, 5)):
      x = randrange(0, Globals.display_rect.width - 50)
      group.add(Laser(display, player, x))

  def __init__(self, display, player, x):
    # Settings
    self.color = "#ee5555"
    self.width = 50
    self.intangible = True

    # Rects
    self.player = player
    super().__init__(display, self.color, x + self.width / 2, 0, 1, 
      Globals.display_rect.height)

    # Tasks
    self.tasks.add(
      Task(partial(effects.expand_horizontal, self, self.width / Globals.fps, 
        "center"), duration=1), 
      Task(partial(effects.toggle_visible, self, False), delay=1), 
      Task(partial(effects.toggle_visible, self, True), delay=1.1),
      Task(partial(effects.flash, self, "#ffffff", 10), delay=1.1),
      Task(self.kill, delay=1.3)
    )

  def update(self):
    self.tasks.update()
    if not self.intangible and pygame.sprite.collide_rect(self, self.player):
      self.player.hit()