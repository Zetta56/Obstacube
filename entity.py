import pygame
from constants import FPS
from collections import deque

class Entity(pygame.sprite.Sprite):
    def __init__(self, display, color, x, y, width, height):
        super().__init__()
        self.display = display
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.position = pygame.Vector2(self.rect.x, self.rect.y)
        self.velocity = pygame.Vector2(0, 0)
        self.length = pygame.Vector2(self.rect.width, self.rect.height)
        self.animations = pygame.sprite.Group()

    def draw(self):
        pygame.draw.rect(self.display, pygame.Color(self.color), self.rect)