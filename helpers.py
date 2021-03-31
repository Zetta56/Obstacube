import pygame
import math
from constants import *

class Task():
  def delay(self, function, timer):
    try:
      if pygame.time.get_ticks() > self.start_time + timer:
        function()
        delattr(self, "start_time")
        return True
    except:
      self.start_time = pygame.time.get_ticks()


# class Task():
#   eventId = 1

#   def __init__(self):
#     self.events = {}

#   def delay(self, function, timer):
#     try:
#       if pygame.time.get_ticks() > self.events.time + timer:
#         function()
#         del self.start[]
#     except:
#       eventId += 1
#       self.events[str(eventId): pygame.time.get_ticks()]

def draw_polygon(display, color, rect, num_sides, rotation=0):
  points = []
  for i in range(num_sides):
    # Gets i fractions of circle's total angle measure
    angle = 2 * math.pi * i / num_sides + rotation
    point_x = rect.centerx + (rect.width / 2) * math.cos(angle)
    point_y = rect.centery + (rect.height / 2) * math.sin(angle)
    points.append([int(point_x), int(point_y)])
  pygame.draw.polygon(display, color, points)