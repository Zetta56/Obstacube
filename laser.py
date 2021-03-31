import pygame
from random import randrange

from helpers import Task
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
    self.warning_timer = 1
    self.destroy_timer = 0.5
    #self.task = Task()

    # Rects
    super().__init__(display, self.color, x + self.width / 2, 0, 0, SCREEN_HEIGHT)
    
  def update(self):
    if self.size.x <= self.width:
      expand_horizontal(self, self.width, self.warning_timer)
    elif self.destroy_timer > 0:
      self.destroy_timer -= 1 / FPS
      self.color = "#ffffff"
    else:
      self.rect.width += 10
      self.rect.x -= 5
      self.kill()
    # else:
    #   self.color = "#ffffff"
    #   self.destroy.tick(self.explode)
    # done = expand_horizontal(self, self.width, self.warning_timer)
    # if done:
    #   self.color = "#ffffff"
    #   self.rect.width += 20
    #   self.rect.x -= 5
    #   done = self.task.delay(self.explode, 500)
    #   if done:
    #     self.task.delay(self.explode, 500)
      # try:
      #   if pygame.time.get_ticks() > self.elapsed + self.destroy_timer: 
      #     self.color = "#ffffff"
      #     self.rect.width += 20
      #     self.rect.x -= 5
          
      #     self.kill()
      # except:
      #   self.elapsed = pygame.time.get_ticks()

  # def explode(self):
    
  #   self.kill()

  def draw(self):
    pygame.draw.rect(self.display, pygame.Color(self.color), self.rect)