"""DEPRECATED"""

import pygame

def toggle_visible(obj, visibility):
  """Toggles visibility of object"""
  obj.visible = visibility

def toggle_tangible(obj, tangibility):
  """Toggles tangibility of object"""
  obj.intangible = not tangibility

def flash(obj, color, expansion_size=0):
  """Changes object color and expands it outward"""
  obj.color = color
  obj.rect.width = obj.length.x + expansion_size
  obj.rect.height = obj.length.y + expansion_size
  obj.rect.x = obj.position.x - expansion_size / 2
  obj.rect.y = obj.position.y - expansion_size / 2
  obj.intangible = False

def expand_horizontal(obj, expansion_size, start="left"):
  """Expands a rect horizontally from specified starting line
  
   start: baseline to expand from
     left: from left to right
     center: from center out
     right: from right to left
  """
  # Move x-position
  if start == "center":
    obj.position.x -= expansion_size / 2
  if start == "right":
    obj.position.x -= expansion_size
  obj.rect.x = obj.position.x
  # Increase width
  obj.length.x += expansion_size
  obj.rect.width = obj.length.x