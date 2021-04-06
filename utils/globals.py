import pygame

class Globals():
    # Settings
    fps = 60
    max_lives = 1
    display = pygame.display.set_mode((600, 600))
    display_rect = display.get_rect()

    # State
    bg_color = "#111111"
    lives = max_lives
    running = True
    playing = False
    paused = False
    game_over = False