import pygame
import math

def draw_polygon(display, color, rect, num_sides, rotation=0):
  points = []
  for i in range(num_sides):
    # Gets i fractions of circle's total angle measure
    angle = 2 * math.pi * i / num_sides + rotation
    point_x = rect.centerx + (rect.width / 2) * math.cos(angle)
    point_y = rect.centery + (rect.height / 2) * math.sin(angle)
    points.append([int(point_x), int(point_y)])
  pygame.draw.polygon(display, color, points)