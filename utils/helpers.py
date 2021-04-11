import pygame
import math
from utils.globals import Globals

def save_score():
  """Saves current score to text file if it's a new record"""
  if Globals.score > Globals.high_score:
    with open("high_score.txt", "w") as f:
      f.write(str(Globals.score))

def draw_polygon(rect, color, num_sides, rotation=0):
  """Draws a regular polygon"""
  points = []
  for i in range(num_sides):
    # Calculate angle measure of 2pi in radians
    angle = 2 * math.pi * i / num_sides + math.radians(rotation)
    # Get points based on angles around circle
    point_x = rect.centerx + (rect.width / 2) * math.cos(angle)
    point_y = rect.centery - (rect.height / 2) * math.sin(angle)
    points.append((int(point_x), int(point_y)))
  pygame.draw.polygon(Globals.display, color, points)