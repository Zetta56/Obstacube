import pygame
from utils.globals import Globals

class Entity(pygame.sprite.Sprite):
  def __init__(self, color, x, y, width, height, platforms=None, physics=False):
    super().__init__()
    self.visible = True
    self.onGround = False
    self.physics = physics
    self.gravity = 0.25
    self.tasks = pygame.sprite.Group()

    # Rects
    self.platforms = platforms
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
    """Stop entity from moving into platforms"""
    platform = pygame.sprite.spritecollideany(self, self.platforms)
    # Check which side player came from at previous frame 
    # to accomadate for spritecollideany's overlap requirement
    if platform:
      # From Left
      if self.rect.right - self.vel.x <= platform.rect.left:
        self.pos.x = platform.rect.left - self.rect.width
      # From Right
      if self.rect.left - self.vel.x >= platform.rect.right:
        self.pos.x = platform.rect.right
      # From Top (adding 1 in order to pass spritecollideany)
      if self.rect.bottom - self.vel.y <= platform.rect.top + 1:
        self.pos.y = platform.rect.top - self.rect.height + 1
        self.vel.y = 0
        self.pos += platform.vel # carry entity along platform
        self.onGround = True
        platform.schedule()
      # From Bottom
      if self.rect.top - self.vel.y >= platform.rect.bottom:
        self.pos.y = platform.rect.bottom
        self.vel.y = 0
        
      # Apply position changes
      self.rect.x = self.pos.x
      self.rect.y = self.pos.y
    else:
      self.onGround = False

  def update(self):
    # Optionally update with physics
    if self.physics and not self.onGround:
      self.fall()
    if self.platforms:
      self.detect_platforms()
    self.pos += self.vel
    self.rect.x = self.pos.x
    self.rect.y = self.pos.y

  def draw(self):
    if self.visible:
      pygame.draw.rect(Globals.display, pygame.Color(self.color), self.rect)