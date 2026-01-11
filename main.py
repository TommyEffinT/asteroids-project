import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    pygame.init() # game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
          log_state()

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 return          # allows the closure of the window

          screen.fill("black")
          pygame.display.flip()
          dt = clock.tick(60) / 1000 # fps set to 60
          

if __name__ == "__main__":
    main()
