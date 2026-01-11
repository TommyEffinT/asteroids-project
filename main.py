import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    pygame.init() # game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
          log_state()

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 return          # allows the closure of the window
          player.update(dt)    
          screen.fill("black")
          
          
          player.draw(screen)      
          pygame.display.flip()
          dt = clock.tick(60) / 1000 # fps set to 60 # make sure dt updates before player.update uses it
          
          

if __name__ == "__main__":
    main()
