import pygame
from constants import *

def expand_horizontal(obj, max_width, time):
  distance = max_width / (time * FPS)
  if obj.size.x <= max_width:
    # Move x-position left
    obj.position.x -= distance / 2
    obj.rect.x = obj.position.x
    # Increase width
    obj.size.x += distance
    obj.rect.width = obj.size.x
    return False
  return True