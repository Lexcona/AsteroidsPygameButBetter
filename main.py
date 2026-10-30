import pygame

from libs import scoring
from libs.logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from texture.player import Player
from texture.asteroid import Asteroid
from texture.asteroidfield import AsteroidField
from texture.shot import Shot
from texture.star import Star, StarField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Star.containers = (updatable, drawable)
    StarField.containers = (updatable)

    # Make starts go BRRRRRRRRRRR
    star_system = StarField()
    ASS_TURD_oids_LMAOOOOOOOOOO = AsteroidField()
    big_blessed_doug = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    scoring.score_update()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # STAGE 1 - CLEAR THE STAGE
        screen.fill('black')

        # STAGE 2 - UPDATE VARIOUS POEPLE AND ANIMALS (numbers, theyre)
        updatable.update(dt)
        for asteroid in asteroids:
            # CHECK IF HIT THE PLAYER
            if big_blessed_doug.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # CHECK IF HITTING A SHOT
            for shot in shots:
                if shot.collides_with(asteroid):
                    # THIS ASTEROID GOT HIT BY THIS SHOT!!!!
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # STAGE 3 - DRAW EVERYONE TO SCREEN
        for droble in drawable:
            droble.draw(screen)

        screen.blit(scoring.scoreText, (10, 10))

        # STAGE 4 - FLIP???
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)

if __name__ == "__main__":
    main()
