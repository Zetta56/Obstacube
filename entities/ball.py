import pygame
from utils.sounds import Sounds
from utils.helpers import draw_polygon
from entities.entity import Entity

class Ball(Entity):
  size = 40 # Used for positioning in spawner

  def __init__(self, player, platforms, x, y, speed):
    # Settings
    self.color = "#ee5555"
    self.rotation = 0
    self.rotation_rate = 10
    self.jump_power = 3
    self.player = player
    if speed > 0: self.rotation_rate *= -1

    # Positioning
    super().__init__(self.color, x, y, Ball.size, Ball.size, 
      platforms=platforms, physics=True)
    self.vel.x = speed

  def update(self):
    self.tasks.update()
    self.rotation += self.rotation_rate
    if self.onGround:
      Sounds.ball.play()
      self.vel.y = -1 * self.jump_power

    # Update position and check for collisions
    super().update()
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()

  def draw(self):
      draw_polygon(self.rect, self.color, num_sides=6, rotation=self.rotation)