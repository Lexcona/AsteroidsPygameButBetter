import random

import pygame

import extra

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    _textures: dict[int, pygame.Surface] = {}

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-40, 40)
        self.texture = self._get_texture(radius)

    @classmethod
    def _get_texture(cls, radius:float) -> pygame.Surface:
        size = max(1, round(radius * 2))
        if size not in cls._textures:
            image, _ = extra.load_image("astroid.png")
            cls._textures[size] = pygame.transform.smoothscale(image, (size, size))
        return cls._textures[size]

    def draw(self, screen: pygame.Surface) -> None:
        texture = pygame.transform.rotate(self.texture, self.rotation)
        screen.blit(texture, texture.get_rect(center=self.position))

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.rotation = (self.rotation + self.rotation_speed * dt) % 360

    def split(self):
        self.kill()

        # Is this a small asteroid? if so, just let it die
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        NEW_ASTEROID_SPEED = 1.2
        random_angle = random.uniform(20, 50)
        first_asteroid_movement = self.velocity.rotate(random_angle)
        second_asteroid_movement = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_asteroid_movement * NEW_ASTEROID_SPEED
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = second_asteroid_movement * NEW_ASTEROID_SPEED
