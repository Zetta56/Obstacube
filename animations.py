import pygame
from constants import *

def expand_horizontal(obj, max_width, time):
  """Ëxpands a rect horizontally from midline"""
  distance = max_width / (time * FPS)
  if obj.length.x <= max_width:
    # Move x-position left
    obj.position.x -= distance / 2
    obj.rect.x = obj.position.x
    # Increase width
    obj.length.x += distance
    obj.rect.width = obj.length.x
    return False
  return True