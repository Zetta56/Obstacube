import pygame
from utils.globals import Globals
from utils.task import Task

class StatusEffect(pygame.sprite.Sprite):
  @classmethod
  def reset(cls):
    cls.default_pos = (20, 70)
    cls.index = 0
    cls.group = pygame.sprite.Group()

  def __init__(self, name, icon, undo_effect, duration):
    super().__init__()
    self.name = name
    self.index = StatusEffect.index
    self.x = StatusEffect.default_pos[0] + self.index * 40
    self.size = 35

    # Icon
    self.icon = pygame.transform.scale(icon, (self.size, self.size))
    self.icon_rect = self.icon.get_rect()
    self.icon_rect.topleft = (self.x, StatusEffect.default_pos[1])
    
    # Shadow
    self.shadow = self.icon.copy()
    # BLEND_RGBA_MULT Formula for (r,g,b,a): color = (original * new) / 256
    self.shadow.fill((80, 80, 80), None, pygame.BLEND_RGBA_MULT)
    self.shadow_rect = self.shadow.get_rect()
    self.shadow_rect.topleft = (self.x, StatusEffect.default_pos[1])

    # Timers and events
    self.start_time = pygame.time.get_ticks()
    self.time_elapsed = 0
    self.undo_effect = undo_effect
    self.duration = duration
    self.schedule()

    StatusEffect.index += 1
    self.handle_duplicate()

  def realign(self):
    """Repositions status effect using index"""
    self.x = StatusEffect.default_pos[0] + self.index * 40
    self.icon_rect.x = self.x
    self.shadow_rect.x = self.x

  def handle_duplicate(self):
    """Replaces duplicate status effect with current one"""
    for status_effect in StatusEffect.group:
      if status_effect.name == self.name and status_effect is not self:
        self.index = status_effect.index
        self.realign()
        status_effect.kill()
        StatusEffect.index -= 1

  def schedule(self):
    def expire():
      # Realigns other status effects
      for status_effect in StatusEffect.group:
        if status_effect.index > self.index:
          status_effect.index -= 1
          status_effect.realign()

      StatusEffect.index -= 1
      self.undo_effect()
      self.kill()

    self.tasks = pygame.sprite.Group()
    self.tasks.add(Task(expire, delay=self.duration))

  def update(self):
    self.tasks.update()
    self.time_elapsed = int((pygame.time.get_ticks() - self.start_time) / 1000)

  def draw(self):
    Globals.display.blit(self.icon, self.icon_rect)
    Globals.display.blit(self.shadow, self.shadow_rect, (0, 0, self.shadow_rect.width, 
      (self.shadow_rect.height / self.duration) * self.time_elapsed))