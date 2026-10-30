import pygame

from libs import extra

from constants import *
from texture.circleshape import CircleShape

class Shot(CircleShape):
    _textures: dict[int, pygame.Surface] = {}

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, HOT_RADIUS)
        self.texture = self._get_texture(self.radius)

    @classmethod
    def _get_texture(cls, radius: float) -> pygame.Surface:
        size = max(1, round(radius * 2))
        if size not in cls._textures:
            image, _ = extra.load_image("textures/bullet.png")
            cls._textures[size] = pygame.transform.smoothscale(image, (size, size))
        return cls._textures[size]

    def draw(self, screen: pygame.Surface) -> None:
        #texture = pygame.transform.rotate(self.texture, self.rotation)
        screen.blit(self.texture, self. texture.get_rect(center=self.position))

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt