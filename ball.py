import pygame
import json
import random

f = open('settings.json')
data = json.load(f)
screen_settings = data["Screen"]
block_settings = data["Block"]

class Ball:
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("images/Ball.png")
        self.image = pygame.transform.scale(self.image, (round(screen_settings["width"]/60), round(screen_settings["width"]/60)))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.center = (x, y)
        
        directions = [-1, 1]

        self.dx = random.choice(directions)
        self.dy = random.choice(directions)
    
    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0 or self.rect.right > screen_settings['width']:
            self.dx *= -1 

        if self.rect.top < 0:
            self.dy *= -1

        if self.rect.bottom > screen_settings['height']:
            return True

        return False
    def split(self):
        return [Ball(self.screen, self.rect.centerx, self.rect.centery), Ball(self.screen, self.rect.centerx, self.rect.centery)]

    def blitme(self):
        self.screen.blit(self.image, self.rect)