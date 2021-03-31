import pygame

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

    def draw(self):
        pygame.draw.rect(self.display, pygame.Color(self.color), self.rect)