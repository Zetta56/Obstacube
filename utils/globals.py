import pygame

class Globals():
    # Settings
    fps = 60
    display = pygame.display.set_mode((600, 600))
    display_rect = display.get_rect()

    # State
    bg_color = "#111111"
    running = True
    game_over = False