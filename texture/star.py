import random

import pygame

from constants import *
from texture.circleshape import CircleShape

class Star(CircleShape):
    def __init__(self, x: float, y: float, radius: float = HOT_RADIUS) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        # Star go move thingy
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius


class StarField(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)

        for _ in range(STAR_COUNT):
            self.spawn_star()

    def spawn_star(self) -> None:
        radius = random.uniform(STAR_MIN_RADIUS, STAR_MAX_RADIUS)
        position = pygame.Vector2(
            random.uniform(0, SCREEN_WIDTH),
            random.uniform(0, SCREEN_HEIGHT),
        )
        star = Star(position.x, position.y, radius)

        # drifty thingy (slowly left)
        direction = pygame.Vector2(-1, random.uniform(-0.3, 0.3)).normalize()
        speed = random.uniform(STAR_MIN_SPEED, STAR_MAX_SPEED)
        star.velocity = direction * speed
