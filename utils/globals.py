import pygame

class Globals():
  # Settings
  fps = 60
  floor_y = 560
  display = pygame.display.set_mode((600, 600))
  display_rect = display.get_rect()
  max_items = 3
  score_rate = 1
  
  # Status
  running = True
  playing = False
  paused = False
  game_over = False

  @classmethod
  def reset(cls):
    cls.game_over = False
    cls.bg_color = "#111111"
    cls.level_timer = 0
    cls.score = 0
    with open("high_score.txt") as f:
      cls.high_score = int(f.readline())