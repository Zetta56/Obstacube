import pygame
from random import randrange, choice
from functools import partial
from copy import copy

from utils.globals import Globals
from utils.task import Task
from entities.platform import Platform
from entities.laser import Laser
from entities.rock import Rock
from entities.ball import Ball

from items.medkit import Medkit

class Spawner():
  def __init__(self, player, scoreboard):
    self.player = player
    self.scoreboard = scoreboard

    # Items
    self.items = pygame.sprite.Group()
    self.item_list = [
      Medkit(self.player, self.scoreboard)
    ]

    # Obstacles
    self.obstacles = pygame.sprite.Group()
    self.obstacle_list = [
      Task(self.spawn_lasers, loops=4, loop_timer=0.5),
      Task(self.spawn_rocks, loops=6, loop_timer=0.2),
      Task(self.spawn_balls, loops=2, loop_timer=1.5)
    ]
    self.schedule()
  
  def schedule(self):
    def generate_obstacle():
      obstacle_task = choice(self.obstacle_list)
      self.tasks.add(copy(obstacle_task))

    def generate_platform():
      Platform.group.add(Platform(-100, 470, 100, 25, 2, 0, breakable=True))

    def generate_item():
      if len(self.items) < Globals.max_items:
        item = choice(self.item_list)
        self.items.add(copy(item))

    self.tasks = pygame.sprite.Group()
    self.tasks.add(
      Task(generate_obstacle, loops=True, loop_timer=3.5),
      Task(generate_platform, loops=True, loop_timer=10),
      Task(generate_item, loops=True, loop_timer=1)
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

  def update(self):
    self.tasks.update()
    self.obstacles.update()
    self.items.update()