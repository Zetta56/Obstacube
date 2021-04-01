import pygame
from constants import *
from helpers import StopException

def hide(obj):
  obj.rect.width = 0

def show(obj):
  obj.rect.width = obj.length.x

def flash(obj, expansion_size):
  obj.color = "#ffffff"
  obj.rect.width = obj.length.x + expansion_size
  obj.rect.height = obj.length.y + expansion_size
  obj.rect.x = obj.position.x - expansion_size / 2
  obj.rect.y = obj.position.y - expansion_size / 2

def expand_horizontal(obj, max_width, duration):
  """Ëxpands a rect horizontally from its midline"""
  distance = max_width / (duration * FPS)
  if obj.length.x <= max_width:
    # Move x-position left
    obj.position.x -= distance / 2
    obj.rect.x = obj.position.x
    # Increase width
    obj.length.x += distance
    obj.rect.width = obj.length.x
    return False
  return True

class Animation(pygame.sprite.Sprite):
  def __init__(self, function, delay=0, duration=0, loops=1, loop_timer=0):
    super().__init__()
    self.function = function
    self.delay = delay
    self.loops = loops
    self.max_duration = duration
    self.duration = duration
    self.max_loop_timer = loop_timer
    self.loop_timer = loop_timer

  def wait(self, timer):
    """Ticks timer and raises StopException if timer isn't finished ticking"""
    setattr(self, timer, getattr(self, timer) - 1 / FPS)
    if getattr(self, timer) >= 0:
      raise StopException

  def update(self):
    try:
      self.wait("delay")
      self.wait("loop_timer")
      self.function()
      self.wait("duration")

      # If there are still loops remaining, reset timers
      if self.loops > 1:
        self.loops -= 1
        self.loop_timer = self.max_loop_timer
        self.duration = self.max_duration
      else:
        self.kill()
    except StopException:
      return