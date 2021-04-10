import pygame
from random import randrange, choice
from functools import partial

from utils.globals import Globals
from utils.task import Task
from entities.laser import Laser
from entities.rock import Rock

class Courses():
  def __init__(self, player, platforms):
    self.player = player
    self.platforms = platforms
    self.obstacles = pygame.sprite.Group()
    self.course_list = [
        {'function': self.generate_lasers, 'loops': 4, 'loop_timer': 0.5},
        {'function': self.generate_rocks, 'loops': 6, 'loop_timer': 0.2}
    ]
    self.schedule()
  
  def schedule(self):
    def pick_course():
      course = choice(self.course_list)
      # Creates a new task object, preserving data in course_list
      self.tasks.add(Task(**course))

    self.tasks = pygame.sprite.Group()
    self.tasks.add(Task(pick_course, loops=True, loop_timer=3.5))

  def generate_lasers(self):
    for i in range(randrange(2, 4)):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Laser(self.player, x))

  def generate_rocks(self):
    for i in range(randrange(4, 6)):
      x = randrange(0, Globals.display_rect.width)
      self.obstacles.add(Rock(self.player, self.platforms, x))