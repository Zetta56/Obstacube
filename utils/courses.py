import pygame
from random import randrange, choice
from functools import partial

from utils.globals import Globals
from utils.task import Task
from entities.laser import Laser

class Courses():
  def __init__(self, player):
    self.obstacles = pygame.sprite.Group()
    self.course_list = [
        {'function': partial(self.generate_lasers, player), 
          'loops': 3, 'loop_timer': 0.5},
    ]
    self.schedule()
  
  def schedule(self):
    def pick_course():
      course = choice(self.course_list)
      # Creates a new task object, preserving data in course_list
      self.tasks.add(Task(**course))

    self.tasks = pygame.sprite.Group()
    self.tasks.add(Task(pick_course, loops=True, loop_timer=2.5))

  def generate_lasers(self, player):
    for i in range(randrange(2, 4)):
      x = randrange(0, Globals.display_rect.width - 50)
      self.obstacles.add(Laser(player, x))