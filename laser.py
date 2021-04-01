import pygame
from functools import partial
from random import randrange

from constants import *
from effects import *
from entity import Entity

class Laser(Entity):
  @staticmethod
  def generate_lasers(display):
    lasers = pygame.sprite.Group()
    for i in range(randrange(2, 5)):
      x = randrange(0, SCREEN_WIDTH - 50)
      lasers.add(Laser(display, x))
    return lasers

  def __init__(self, display, x):
    # Settings
    self.color = "#ee5555"
    self.width = 50

    # Rects
    super().__init__(display, self.color, x + self.width / 2, 0, 0, SCREEN_HEIGHT)

    # Actions
    self.animations.add(
      Animation(partial(expand_horizontal, self, self.width, 1), 0, 1), 
      Animation(partial(hide, self), 1), 
      Animation(partial(flash, self, 10), 1.2),
      Animation(self.kill, 1.4)
    )

  def update(self):
    self.animations.update()