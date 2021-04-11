import pygame
from random import randrange, choice
from functools import partial

from utils.globals import Globals
from utils.task import Task
from entities.platform import Platform
from entities.laser import Laser
from entities.rock import Rock
from entities.ball import Ball

class Spawner():
  def __init__(self, player):
    self.player = player
    self.obstacles = pygame.sprite.Group()
    self.obstacle_list = [
        {'function': self.spawn_lasers, 'loops': 4, 'loop_timer': 0.5},
        {'function': self.spawn_rocks, 'loops': 6, 'loop_timer': 0.2},
        {'function': self.spawn_balls, 'loops': 2, 'loop_timer': 1.5},
    ]
    self.schedule()
  
  def schedule(self):
    def pick_obstacle():
      obstacle = choice(self.obstacle_list)
      # Creates a new task object, preserving data in obstacle_list
      self.tasks.add(Task(**obstacle))

    def generate_platform():
      Platform.group.add(Platform(-100, 470, 100, 25, 2, 0, breakable=True))

    self.tasks = pygame.sprite.Group()
    self.tasks.add(
      Task(pick_obstacle, loops=True, loop_timer=3.5),
      Task(generate_platform, loops=True, loop_timer=10)
    )

  def spawn_lasers(self):
    for i in range(randrange(2, 4)):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Laser(self.player, x))

  def spawn_rocks(self):
    for i in range(randrange(4, 6)):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Rock(self.player, x))
    
  def spawn_balls(self):
    self.obstacles.add(Ball(self.player, 2.5))
    self.obstacles.add(Ball(self.player, -2.5))