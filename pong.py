import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

green = 0, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
white = 255, 255, 255
fluorescent_yellow = 243, 243, 21
key = pygame.key.get_pressed()
up_key = 'up'


class PlayerOne(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.speedx = 5
        self.speedy = 5
        # Places sprite on x,y

    def move(self):
    #Keyboard movements
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if key[pygame.K_RIGHT]:
            self.rect.y += self.speedy

        if key[pygame.K_UP]:
            self.rect.y -= self.speedy

        if key[pygame.K_DOWN]:
            self.rect.x += self.speedx

        key.press('left')  # press the left arrow key

class PlayerTwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        # Places sprite on x,y

    def move(self):
        # Keyboard movements
        if key[pygame.K_A]:
            self.rect.x -= self.speedx

        if key[pygame.K_D]:
            self.rect.y += self.speedy

        if key[pygame.K_W]:
            self.rect.y -= self.speedy

        if key[pygame.K_S]:
            self.rect.x += self.speedx