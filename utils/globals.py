import pygame

class Globals():
    # Settings
    fps = 60
    max_lives = 1
    score_rate = 1
    display = pygame.display.set_mode((600, 600))
    display_rect = display.get_rect()

    # Status
    running = True
    playing = False
    paused = False
    game_over = False

    @classmethod
    def reset_state(cls):
        cls.bg_color = "#111111"
        cls.lives = cls.max_lives
        cls.level_timer = 0
        cls.score = 0
        with open("high_score.txt") as f:
            cls.high_score = int(f.readline())