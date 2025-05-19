import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    update_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (update_group, drawable_group)
    Asteroid.containers = (asteroid_group, update_group, drawable_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shot_group, update_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((0, 0, 0))
        update_group.update(dt)

        for asteroid in asteroid_group:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        
        for sprite in drawable_group:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()