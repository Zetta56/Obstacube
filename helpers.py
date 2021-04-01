import pygame
import math
from constants import *

class StopException(Exception):
  pass

def draw_polygon(display, color, rect, num_sides, rotation=0):
  """Draws a polygon"""
  points = []
  for i in range(num_sides):
    # Gets i fractions of 2pi (total angle measure of circle)
    angle = 2 * math.pi * i / num_sides + rotation
    # Get points based on circle's angle
    point_x = rect.centerx + (rect.width / 2) * math.cos(angle)
    point_y = rect.centery + (rect.height / 2) * math.sin(angle)
    points.append([int(point_x), int(point_y)])
  pygame.draw.polygon(display, color, points)