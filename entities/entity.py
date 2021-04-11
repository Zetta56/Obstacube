import pygame
from entities.platform import Platform
from utils.globals import Globals

class Entity(pygame.sprite.Sprite):
  def __init__(self, color, x, y, width, height, use_physics=False):
    super().__init__()
    self.visible = True
    self.onGround = False
    self.gravity = 0.25
    self.use_physics = use_physics
    self.tasks = pygame.sprite.Group()

    # Rects
    self.rect = pygame.Rect(x, y, width, height)
    self.color = color
    self.pos = pygame.Vector2(self.rect.x, self.rect.y)
    self.vel = pygame.Vector2(0, 0)
    self.length = pygame.Vector2(self.rect.width, self.rect.height)

  def fall(self):
    if self.onGround:
      self.vel.y = 0
    else:
      self.vel.y += self.gravity

  def detect_platforms(self):
    """Stop entity from crashing into platforms"""
    platform = pygame.sprite.spritecollideany(self, Platform.group)
    # Check which side player came from at previous frame
    if platform:
      # From Left
      if self.rect.right - self.vel.x <= platform.rect.left + abs(platform.vel.x):
        self.pos.x = platform.rect.left + platform.vel.x - self.rect.width
      # From Right
      if self.rect.left - self.vel.x >= platform.rect.right - abs(platform.vel.x):
        self.pos.x = platform.rect.right + platform.vel.x
      # From Top
      if self.rect.bottom - self.vel.y <= platform.rect.top + abs(platform.vel.y) + 1:
        # Adding 1 in order to pass spritecollideany check
        self.pos.y = platform.rect.top - self.rect.height + platform.vel.y + 1
        self.vel.y = 0
        self.onGround = True
        if platform.breakable:
          platform.destroy()
      # From Bottom
      if self.rect.top - self.vel.y >= platform.rect.bottom - abs(platform.vel.y):
        self.pos.y = platform.rect.bottom + platform.vel.y
        self.vel.y = 0
        
      # Apply position changes
      self.rect.x = self.pos.x
      self.rect.y = self.pos.y
    else:
      self.onGround = False

  def update(self):
    # Optionally update with physics
    if self.use_physics:
      if not self.onGround:
        self.fall()
      self.detect_platforms()
    self.pos += self.vel
    self.rect.x = self.pos.x
    self.rect.y = self.pos.y

  def draw(self):
    if self.visible:
      pygame.draw.rect(Globals.display, pygame.Color(self.color), self.rect)