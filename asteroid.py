import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (pygame.Vector2(random.uniform(20, 50), random.uniform(20, 50)) * 1.2).rotate(random.uniform(0, 360))
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (pygame.Vector2(random.uniform(20, 50), random.uniform(20, 50)) * 1.2).rotate(-random.uniform(0, 360))
    
        