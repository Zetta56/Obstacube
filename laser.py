import pygame
from collections import deque
from functools import partial
from random import randrange

from constants import *
from animations import *
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
    def hide():
      self.rect.width = 0

    def flash():
      self.color = "#ffffff"
      self.rect.width  = self.width + 10
      self.rect.x = self.position.x - 5

    self.actions.extend([
      {'duration': 1, 'function': partial(expand_horizontal, self, self.width, 1)}, 
      {'duration': 0.25, 'function': hide},
      {'duration': 0.25, 'function': flash},
      {'duration': 0, 'function': self.kill}
    ])

  def update(self):
    self.call_action()