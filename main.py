# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    run = True
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(x,y)
    asteroid_field = AsteroidField()####


    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")#RGB 255 (0,0,0)

        for x in updatable:
            x.update(dt)

        for x in asteroids:
            if(player.check_collision(x)):#asteroid.check_collision(player)
                print("Game over!")
                sys.exit()
            for y in shots:
                if(x.check_collision(y)):
                    x.split()
                    y.kill()

        for x in drawable:
            x.draw(screen)
        #player.update(dt)
        #player.draw(screen)

        pygame.display.flip()#call last
        dt = clock.tick(60) / 1000 #milliseconds to seconds

if __name__ == "__main__":
    main()