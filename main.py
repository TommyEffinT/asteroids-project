import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid


def main():
    pygame.init() # game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
          log_state()

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 return          # allows the closure of the window
              
          
          updatable.update(dt)  
          screen.fill("black")

          for sprite in drawable:
              sprite.draw(screen)   

          pygame.display.flip()
          dt = clock.tick(60) / 1000 # fps set to 60 # make sure dt updates before player.update uses it
          
          
if __name__ == "__main__":
    main()
