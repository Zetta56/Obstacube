import pygame
from constants import FPS
from collections import deque

class Entity(pygame.sprite.Sprite):
    def __init__(self, display, color, x, y, width, height):
        super().__init__()
        # Display
        self.display = display
        self.display_rect = self.display.get_rect()

        # Rect
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.position = pygame.Vector2(self.rect.x, self.rect.y)
        self.velocity = pygame.Vector2(0, 0)
        self.length = pygame.Vector2(self.rect.width, self.rect.height)
        # Action Format: [{'duration': float, 'function': function}
        self.actions = deque([])

    def call_action(self):
        """Call next action in deque for specified duration"""
        action = self.actions[0]
        if action['duration'] >= 0:
          action['function']()
          action['duration'] -= 1 / FPS
        else:
          self.actions.popleft()

    def draw(self):
        pygame.draw.rect(self.display, pygame.Color(self.color), self.rect)