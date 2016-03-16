"""
Author: Jay Soto
Date: 01/30/2016
Version: 2.5.6
"""

class Settings():
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's settings """
        # Screen settings:
        self.screen_width = 800
        self.screen_height = 600

        # ---------------R--G--B--- (RED, GREEN, BLUE):
        self.bg_color = (0, 0, 0)
        
        # Ship settings:
        self.ship_speed_factor = 1.5

        # Bullet settings:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200
        self.bullets_allowed = 4