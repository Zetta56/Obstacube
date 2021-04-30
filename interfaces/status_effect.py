import pygame
from utils.globals import Globals
from utils.task import Task

class StatusEffect(pygame.sprite.Sprite):
  default_pos = (20, 70) # position of topleft-most status effect

  def __init__(self, name, icon, undo_effect, duration):
    super().__init__()
    self.name = name
    self.x = StatusEffect.default_pos[0] + len(Globals.status_effects) * 40
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

  def schedule(self):
    def expire():
      expiring = True
      # Moves other effect icons to the left when effect expires
      for status_effect in Globals.status_effects:
        if status_effect.name == self.name and status_effect is not self:
          expiring = False
        if status_effect.x > self.x:
          status_effect.x -= 40
        status_effect.icon_rect.x = status_effect.x
        status_effect.shadow_rect.x = status_effect.x
      if expiring:
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