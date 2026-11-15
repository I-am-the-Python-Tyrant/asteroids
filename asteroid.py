import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    #def move(self, dt):
    #    unit_vector = pygame.Vector2(0, 1)
    #    rotated_vector = unit_vector.rotate(self.rotation)
    #    rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
    #    self.position += rotated_with_speed_vector
    def  update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            unit_vector1 = self.velocity.rotate(angle)
            unit_vector2 = self.velocity.rotate(-angle)
            split1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            split2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            #split1.velocity.rotate(angle)
            #split2.velocity.rotate(-angle)
            rotated_vector1 = unit_vector1.rotate(angle)
            rotated_with_speed_vector1 = rotated_vector1 * 1.2
            split1.velocity += rotated_with_speed_vector1
            rotated_vector2 = unit_vector2.rotate(-angle)
            rotated_with_speed_vector2 = rotated_vector2 * 1.2
            split2.velocity += rotated_with_speed_vector2