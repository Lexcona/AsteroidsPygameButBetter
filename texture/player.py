import pygame

from constants import *
from libs import sounds
from texture.shot import Shot
from texture.circleshape import CircleShape

class Player(CircleShape):
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown -= dt

    def move(self, dt: float) -> None:
        move_vect = pygame.Vector2(0, 1)
        move_vect = move_vect.rotate(self.rotation)
        move_vect *= (PLAYER_SPEED * dt)
        self.position += move_vect

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        new_shot = Shot(self.position.x, self.position.y)
        unit_vect = pygame.Vector2(0,1)
        rotated_vect = unit_vect.rotate(self.rotation)
        new_shot.velocity = rotated_vect * PLAYER_SHOOT_SPEED

        sounds.shoot()