import pygame
from utils.globals import Globals
from utils.task import Task
from utils.helpers import draw_polygon
from entities.entity import Entity
from entities.bullet import Bullet

class Drone(Entity):
  size = 40 # Used for positioning in spawner

  def __init__(self, player, platforms, x, y, velx, vely):
    # Settings
    self.color = "#ee5555"
    self.rotation = 0
    self.rotation_rate = 2

    # Bullets
    self.bullet_speed = 3
    self.cooldown = 1000
    self.clock = pygame.time.Clock()
    self.timer = self.cooldown

    # Positioning
    super().__init__(self.color, x, y, Drone.size, Drone.size)
    self.player = player
    self.platforms = platforms
    self.vel.x = velx
    self.vel.y = vely

  def update(self):
    self.tasks.update()
    self.rotation += self.rotation_rate

    # Fires bullets
    # Note: Not using tasks here because bullets must use drone's current
    # location as it updates and not initial location
    self.timer += self.clock.tick()
    if self.timer > self.cooldown:
      directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))
      for direction in directions:
        Bullet.group.add(Bullet(self.player, 10, self.rect.x, self.rect.y,
          direction[0] * self.bullet_speed, direction[1] * self.bullet_speed))
      self.timer = 0

    # Update position and check for collisions
    super().update()
    if pygame.sprite.collide_rect(self, self.player):
      self.player.hit()
    if (pygame.sprite.spritecollideany(self, self.platforms) or 
        self.rect.y > Globals.display_rect.height):
      self.kill()

  def draw(self):
      draw_polygon(self.rect, self.color, num_sides=8, rotation=self.rotation)