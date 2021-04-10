import pygame
import math
from utils.globals import Globals

def draw_polygon(rect, color, num_sides, rotation=0):
  """Draws a polygon"""
  points = []
  for i in range(num_sides):
    # Calculate angle measure of 2pi in radians
    angle = 2 * math.pi * i / num_sides + math.radians(rotation)
    # Get points based on angles around circle
    point_x = rect.centerx + (rect.width / 2) * math.cos(angle)
    point_y = rect.centery - (rect.height / 2) * math.sin(angle)
    points.append((int(point_x), int(point_y)))
  pygame.draw.polygon(Globals.display, color, points)