import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship.
    ship = Ship(screen)
    # Set the background color.
    bg_color = (56, 50, 168)
 # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        # Watch for keyboard and mouse events.
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
 
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()