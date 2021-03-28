import pygame

from player import Player
from platform import create_platforms

# Initializing game objects
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((600, 600))
display_rect = display.get_rect()
platforms = create_platforms(display)
player = Player(display, platforms)

running = True
while running:
  clock.tick(60) # Max: 60FPS
  # Events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Keydown
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        player.jump()
  
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and player.rect.left > display_rect.left:
    player.velocity.x = -1 * player.speed
  elif key[pygame.K_RIGHT] and player.rect.right < display_rect.right:
    player.velocity.x = player.speed
  else:
    player.velocity.x = 0

  # Updating Screen
  display.fill(pygame.Color("#111111"))
  for platform in platforms:
    platform.draw()
  player.update()
  player.draw()
  pygame.display.update()

pygame.quit() # Properly closing game