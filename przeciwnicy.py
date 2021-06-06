

import pygame
import random
from pygame.locals import *
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

FPS = 60
FramePerSec = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#musi być przed inicjacją obiektu
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
przeciwnik = Rybka()
owoc = Owoc()
enemies = pygame.sprite.Group()
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(przeciwnik.surf, przeciwnik.rect)
    przeciwnik.update()
    screen.blit(owoc.surf, owoc.rect)
    owoc.update()
    pygame.display.flip()
    FramePerSec.tick(FPS)
