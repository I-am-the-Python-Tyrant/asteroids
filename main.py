import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    
    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for item in asteroids:
            for bullet in shots:
                if bullet.collides_with(item):
                    log_event("asteroid_shot")
                    item.split()
                    bullet.kill()
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #print(f"Current value of Clock: {dt}")
            
        


if __name__ == "__main__":
    main()
