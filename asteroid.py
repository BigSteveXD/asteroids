from CircleShape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        line_width = 2
        self.x += (self.velocity * dt)####
        pygame.draw.circle(screen, "white", self.x, self.y, self.radius, line_width)

    def update(self):
