import pygame, sys, os
from pygame import mixer
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

import pygame_menu
import random
import time
import copy 
import pygame_menu.font

FPS = 60
FramePerSec = pygame.time.Clock()

DELAY_BEFORE_START = 3
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
PADDING_TOP = 5
PADDING_BOTTOM = 7

TARGET_POINTS = 100 

POINTS_FOR_FISH = 1 
POINTS_FOR_FRUIT = 2

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        fishes = ["blob2.png", "rybka1.png", "rybka2.png"]
        random_fish = random.randint(0, 2)
        self.surf = pygame.image.load(fishes[random_fish]).convert_alpha()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(PADDING_BOTTOM, SCREEN_HEIGHT - PADDING_BOTTOM)))
        self.speed = 3
    def update(self):
        self.rect.move_ip(-self.speed, 0)
    def speedup(self):
        self.speed = 4

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.surf = pygame.image.load("owocek.png").convert_alpha()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(PADDING_TOP, SCREEN_HEIGHT - PADDING_BOTTOM),))
        self.speed = 4
    def update(self):
        self.rect.move_ip(-self.speed, 0)
    def speedup(self):
        self.speed = 5

class Shark (pygame.sprite.Sprite):
    def __init__(self):
        super(Shark, self).__init__()
        self.surf = pygame.image.load("rekin.png").convert_alpha()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(center = (50, 250))

    def update(self, pressed_button):
        if pressed_button[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_button[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_button[K_RIGHT]:
            self.rect.move_ip(+5,0)
        if pressed_button[K_LEFT]:
            self.rect.move_ip(-5,0)
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
def countdown_delay(init_num, message = 'Start!'):
# countdown before game start
   clock = pygame.time.Clock()

   counter, counter_text = init_num, str(init_num).rjust(3)
   pygame.time.set_timer(pygame.USEREVENT, 1000)
   counter_font = pygame.font.Font("freesansbold.ttf", 30)

   # countdown loop
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.USEREVENT: 
               counter -= 1
               counter_text = str(counter).rjust(3) if counter > 0 else message
           if event.type == pygame.QUIT: 
               running = False

       screen.blit(sea_background, (0,0))
       text = counter_font.render(counter_text, True, pygame.Color('white'))
       text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
       screen.blit(text, text_rect)
       pygame.display.update()
       pygame.display.flip()
       clock.tick(60)
       if counter == 0:
           running = False

   pygame.time.delay(1000)

def game_over(game_result, message_game_won = 'Win!!!', message_game_lost = 'Game Over!'):
   clock = pygame.time.Clock()
   pygame.time.set_timer(pygame.USEREVENT, 1000)
   font = pygame.font.Font("freesansbold.ttf", 30)
   if game_result:
       message = message_game_won
   else:
       message = message_game_lost

   running = True
   while running:
       for event in pygame.event.get():
           # Did the user hit a key?
           if event.type == KEYDOWN:
               # Was it the Escape key? If so, stop the loop
               if event.key == K_ESCAPE:
                   running = False
           if event.type == pygame.QUIT: 
               running = False

       text = font.render(message, True, pygame.Color('white'))
       text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
       screen.blit(text, text_rect)
       pygame.display.update()
       pygame.display.flip()
       clock.tick(60)

   pygame.time.delay(1000)

pygame.display.set_caption("Tranquility")
icon = pygame.image.load('rekin.png')
pygame.display.set_icon(icon)
sea_background=pygame.image.load('tlo.jpg')
sea_background=pygame.transform.scale(sea_background,(SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.get_surface()

# smooth moving the player 
pygame.key.set_repeat(10,10)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                   
#to give player time being ready
countdown_delay(DELAY_BEFORE_START)


mixer.music.load("muzyczka.mp3")
mixer.music.play(-1) #żeby muzyczka grała w pętli

tlo_morze=pygame.image.load('tlo.jpg')

mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
mytheme.title_background_color = (0,0,0)

mytheme.title_font_shadow = True
mytheme.title_shadow_color = (200,200,200)
font = pygame_menu.font.FONT_MUNRO
mytheme.title_font = font
mytheme.title_font_size = 50
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
mytheme.title_offset = (140,100)
mytheme.cursor_color = pygame.Color("pink")

pygame.init()
screen.blit(myimage, (0,0))
menu = pygame_menu.Menu(700, 700,"Tranquility: Obiad Rekinka",
            theme = mytheme)
menu.add.text_input("IMIĘ :" , default = "wpisz swoje imię")
menu.add.button("PLAY")
menu.add.button("O AUTORACH")
menu.add.button("HOW TO PLAY REKINEK")
menu.add.button("WYJŚCIE", pygame_menu.events.EXIT)


pygame.display.update()
pygame.display.flip() 

menu.mainloop(screen)

# Custom event for adding an enemy
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)

# Create our 'player'
player = Shark()

#Sprite groups to hold enemies, and every sprite
#enemies is used for collision detection and position updates
#all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep our main loop running
global points
points = 0
running = True
is_game_won = False

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

        # Adding an enemy
        elif event.type == ADD_ENEMY:
            # Defining criteria for adding an enemy
            if points >= TARGET_POINTS/2 and points < TARGET_POINTS/2 + 1 and len(enemies) == 0:
                new_enemy = Fruit()
            elif len(enemies) == 0:
                new_enemy = Fish()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    
    screen.blit(sea_background, (0,0))

    #draws all spirtes
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
                   
    if points >= TARGET_POINTS:
        running = False
        is_game_won = True
        continue
        
    score_font = pygame.font.Font("freesansbold.ttf", 20)
    score_on_X = SCREEN_WIDTH/100 * 80
    score_on_Y = 10
    
    def score_text(x,y):
        score = score_font.render("SCORE: " + str(points), True, pygame.Color('white'))
        screen.blit(score, (x,y))

    #show the score
    score_text(score_on_X, score_on_Y)

    #adding points, removing enemies or player
    for entity in enemies:
        if pygame.sprite.spritecollide(player, enemies, True):
            if entity == Fruit:
                   points += POINTS_FOR_FRUIT
                   entity.kill()
                   enemies.remove(entity)
            else:
                   enemies.remove(entity)
                   entity.kill()
                   points += POINTS_FOR_FISH
        elif entity.rect.left < 0:
                player.kill()
                running = False
            
    if points >= TARGET_POINTS/2 and points <= TARGET_POINTS/2 + 1:
        for entity in enemies:
            entity.speedup()
    
    score_font = pygame.font.Font("freesansbold.ttf", 20)
    score_on_X = SCREEN_WIDTH/100 * 80
    score_on_Y = 10
    
    def score_text(x,y):
        score = score_font.render("SCORE: " + str (points), True, pygame.Color('white'))
        screen.blit(score,(x,y))
                   
    if points == TARGET_POINTS/2:
        mixer.music.stop()
        mixer.music.unload()
        
    if not pygame.mixer.music.get_busy():
        mixer.music.load("Synapsis.mp3")
        mixer.music.play(-1)

    #Flips everything to the display and adding FPS "border"
    pygame.display.flip()
    FramePerSec.tick(FPS)
     
game_over(is_game_won)
