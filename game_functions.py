"""
Author: Jay Soto
Date: 01/30/2016
Version: 2.5.6
"""

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''respond to key presses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # create a new bullet and add it to the bullets group:
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''respond to key releases'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    '''updates everything on the screen and flips (updates) screen'''
    # Redraw the screen everytime through the loop:
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets BEHIND ship and aliens:
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Redraw the ship:
    ship.blitme()

    # Make the most recently drawn (updated) screen visible:
    pygame.display.flip()

def update_bullets(bullets):
    """Update the position of bullets and get rid of old bullets"""
    # update bullet positions:
    bullets.update()

    # get rid of old bullets:
    for bullet in bullets.copy(): 
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)