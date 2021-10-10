import pygame
import os

class Sounds():
  pygame.mixer.init()
  laser = pygame.mixer.Sound("sounds/laser.wav")
  laser.set_volume(0.05)
  hit = pygame.mixer.Sound("sounds/hit.wav")
  hit.set_volume(0.3)
  item = pygame.mixer.Sound("sounds/item.wav")
  item.set_volume(0.1)
  shot = pygame.mixer.Sound("sounds/shot.wav")
  shot.set_volume(0.1)
  rock = pygame.mixer.Sound("sounds/rock.wav")
  rock.set_volume(0.1)
  lava = pygame.mixer.Sound("sounds/lava.wav")
  lava.set_volume(0.1)
  ball = pygame.mixer.Sound("sounds/ball.wav")
  ball.set_volume(0.1)