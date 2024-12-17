import pygame
from constants import *
from circleshape import CircleShape
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        #self.SHOT_RADIUS = 5
        shots = pygame.sprite.Group()

    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)