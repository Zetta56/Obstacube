import pygame
from helpers.settings import Settings

class StopException(Exception):
  pass

class Task(pygame.sprite.Sprite):
  """Schedules functions to run at the right time

   function: the function you want to schedule
   delay: wait time before function is called
   duration: function duration per loop
   loops: number of times to call function 
     True: loop forever
   loop_timer: wait time between loops

  Note: time is measured in seconds
  """
  def __init__(self, function, delay=0, duration=0, loops=1, loop_timer=0):
    super().__init__()
    self.function = function
    self.delay = delay
    self.duration = duration
    self.loops = loops
    self.loop_timer = 0 # Ignore loop_timer during first loop

    # Used to reset attributes
    self.max_duration = duration
    self.max_loop_timer = loop_timer

  def wait(self, timer):
    """Ticks timer and raises StopException if timer isn't finished ticking"""
    setattr(self, timer, getattr(self, timer) - 1 / Settings.fps)
    if getattr(self, timer) > 0:
      raise StopException

  def update(self):
    try:
      self.wait("delay")
      self.wait("loop_timer")
      self.function()
      self.wait("duration")

      # If there are still loops remaining, reset timers
      if self.loops is True:
        self.loop_timer = self.max_loop_timer
        self.duration = self.max_duration
      elif self.loops > 1:
        self.loops -= 1
        self.loop_timer = self.max_loop_timer
        self.duration = self.max_duration
      else:
        self.kill()
    except StopException:
      return