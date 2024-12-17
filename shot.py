from cicleshape import CicleShape
class Shot:
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.SHOT_RADIUS = 5
        shots = pygame.sprite.Group()

    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)