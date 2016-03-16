"""
Author: Jay Soto
Date: 01/30/2016
Version: 2.5.6
"""

import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game(): # Initialize game, settings, and screen object:
    pygame.init()
    ai_settings = Settings() # creates a variable to store our Settings class
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Creates a ship from the "ship" class and stores it in a variable called "ship"
    ship = Ship(ai_settings, screen)

    # Make a group to store the bullets in:
    bullets = Group()

    # Starts the main loop for the game:
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

# Runs the function we created:
run_game()