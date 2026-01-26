import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init() # game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0


    while True:
          log_state()

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 return          # allows the closure of the window
              
          
          updatable.update(dt)  

          for asteroid in asteroids:
              if player.collides_with(asteroid):
                 log_event("player_hit")
                 print("Game over!")
                 sys.exit()

          screen.fill("black")

          for sprite in drawable:
              sprite.draw(screen)   

          pygame.display.flip()
          dt = clock.tick(60) / 1000 # fps set to 60 # make sure dt updates before player.update uses it
          
          
if __name__ == "__main__":
    main()
