import pygame
import sys
import asyncio

from player import Player
from platform import Platform
from laser import Laser
from helpers import *
from constants import *

# Instantiating game objects and variables
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_rect = display.get_rect()
platforms = Platform.create_platforms(display)
lasers = Laser.generate_lasers(display)
player = Player(display, platforms)
seconds = 0
running = True

while running:
  clock.tick(FPS) # Max: 60FPS
  seconds += 1 / FPS
  
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
  
  # Held Inputs
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and player.rect.left > display_rect.left:
    player.velocity.x = -1 * player.speed
  elif key[pygame.K_RIGHT] and player.rect.right < display_rect.right:
    player.velocity.x = player.speed
  else:
    player.velocity.x = 0
  if seconds > 2:
    lasers = Laser.generate_lasers(display)
    seconds -= 2

  # Updating Screen
  display.fill(pygame.Color("#111111"))
  for platform in platforms:
    platform.draw()
  for laser in lasers:
    laser.update()
    laser.draw()
  player.update()
  player.draw()
  pygame.display.update()

# Properly closing game
pygame.quit()
sys.exit()