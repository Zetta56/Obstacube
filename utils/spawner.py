import pygame
from random import randrange, choice
from functools import partial
from copy import copy

from utils.globals import Globals
from utils.task import Task
from entities.player import Player
from entities.platform import Platform
from entities.laser import Laser
from entities.rock import Rock
from entities.ball import Ball
from entities.lava import Lava
from items.medkit import Medkit
from items.shield import Shield
from items.double_jump import DoubleJump
from items.speed_up import SpeedUp
from entities.drone import Drone

class Spawner():
  def __init__(self, scoreboard):
    # Platforms
    self.platforms = pygame.sprite.Group()
    self.platforms.add(
      Platform(0, Globals.floor_y, Globals.display_rect.width, 
        Globals.display_rect.height - Globals.floor_y)
    )

    # Player & Scoreboard
    self.scoreboard = scoreboard
    self.player = Player(self.platforms, self.scoreboard)

    # Obstacles
    self.obstacles = pygame.sprite.Group()
    self.obstacle_list = [
      Task(self.spawn_lasers, loops=5, loop_timer=0.75),
      Task(self.spawn_rocks, loops=10, loop_timer=0.25),
      Task(self.spawn_balls, loops=3, loop_timer=1.5),
      Task(self.spawn_drones, loops=2, loop_timer=2.5),
      Task(self.spawn_lava)
    ]

    # Items
    self.items = pygame.sprite.Group()
    self.item_list = [
      Medkit(self.player, self.scoreboard),
      Shield(self.player),
      DoubleJump(self.player),
      SpeedUp(self.player)
    ]
    self.schedule()
  
  def schedule(self):
    def generate_obstacle():
      obstacle_task = choice(self.obstacle_list)
      self.tasks.add(copy(obstacle_task))

    def generate_item():
      if len(self.items) < Globals.max_items:
        item = choice(self.item_list)
        self.items.add(copy(item))

    self.tasks = pygame.sprite.Group()
    self.tasks.add(
      Task(generate_obstacle, loops=True, loop_timer=5),
      Task(generate_item, loops=True, loop_timer=5)
    )
  
  def spawn_lasers(self):
    """Creates wave of lasers"""
    for i in range(5):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Laser(self.player, x))

  def spawn_rocks(self):
    """Creates wave of falling rocks"""
    for i in range(randrange(4, 6)):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Rock(self.player, self.platforms, x))
    
  def spawn_balls(self):
    """Creates wave of bouncing balls"""
    self.obstacles.add(Ball(self.player, self.platforms, 
      Globals.display_rect.left - Ball.size, Globals.floor_y - Ball.size, 5))
    self.obstacles.add(Ball(self.player, self.platforms, 
      Globals.display_rect.right, Globals.floor_y - Ball.size, -5))

  def spawn_drones(self):
    """Creates multiple drones that fire bullets"""
    for i in range(3):
      x = choice((-Drone.size, Globals.display_rect.right))
      y = randrange(0, Globals.display_rect.centery)
      velx = randrange(1, 4)
      vely = randrange(2, 4)
      if x > Globals.display_rect.centerx: velx *= -1
      self.obstacles.add(Drone(self.player, self.platforms, x, y, velx, vely))

  def spawn_lava(self):
    def make_platforms():
      self.platforms.add(Platform(-100, 475, 75, 25, (4, 0), breakable=True))

    self.obstacles.add(Lava(self.player))
    self.tasks.add(Task(make_platforms, loops=3, loop_timer=1))

  def update(self):
    self.tasks.update()
    self.player.update()
    self.platforms.update()
    self.obstacles.update()
    self.items.update()