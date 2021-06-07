
import pygame, sys,os
from pygame.locals import *
from pygame import mixer
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

import random

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

pygame.display.set_caption("Tranquility")
icon = pygame.image.load('rekin.png')
pygame.display.set_icon(icon)
tlo_morze=pygame.image.load('tlo.jpg')
screen = pygame.display.get_surface()

class Rekin (pygame.sprite.Sprite):
    def __init__(self):
        super(Rekin, self).__init__()
        self.surf = pygame.image.load("rekin.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (50, 250))

    def update(self, klawisze_wcisniete):
        if klawisze_wcisniete[K_UP]:
            self.rect.move_ip(0, -5)
        if klawisze_wcisniete[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Rybka(pygame.sprite.Sprite):
    def __init__(self):
        super(Rybka, self).__init__()
        rybki = ["blob2.png", "rybka1.png", "rybka2.png"]
        wylosowana = random.randint(0, 2)
        self.surf = pygame.image.load(rybki[wylosowana]).convert()
        #self.surf = pygame.Surface((36,36))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),))
        self.speed = random.randint(3, 5)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Owoc(pygame.sprite.Sprite):
    def __init__(self):
        super(Owoc, self).__init__()
        self.surf = pygame.image.load("owocek.png").convert()
        #self.surf = pygame.Surface((36,36))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),))
        self.speed = random.randint(2, 4)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create our 'player'
player = Rekin()

# Create groups to hold enemy sprites, and every sprite
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep our main loop running
running = True

# Our main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            new_enemy = Rybka()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies
    enemies.update()

    # Fill the screen with black
    #screen.fill((0, 0, 0))
    screen.blit(tlo_morze, (0,0))

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player and stop the loop
        player.kill()
        running = False

    # Flip everything to the display
    pygame.display.flip()
    FramePerSec.tick(FPS)
