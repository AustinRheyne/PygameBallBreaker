import pygame
import json

f = open('settings.json')
data = json.load(f)
screen_settings = data["Screen"]
block_settings = data["Block"]


class Paddle:
    def __init__(self, screen):
        self.image = pygame.image.load('images/Paddle.png')
        self.image = pygame.transform.scale(self.image, (round(screen_settings["width"]/8), round(screen_settings['width']/40)))
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.bottom = self.screen.get_rect().bottom - screen_settings["height"]/40
        self.rect.centerx = self.screen.get_rect().centerx
    
    def move(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]

        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > screen_settings["width"]:
            self.rect.right = screen_settings["width"]
        
    def check_ball_hit(self, ball):
        # If ball hits top
        if self.rect.top < ball.rect.bottom < self.rect.bottom:
            if self.rect.left < ball.rect.right < self.rect.right or self.rect.right > ball.rect.left > self.rect.left:
                ball.dy *= -1
        
        #elif because the top triggers the left and right collision

        # If ball hits left or right
        elif self.rect.right > ball.rect.left > self.rect.left or self.rect.left < ball.rect.right < self.rect.right:
            if self.rect.top < ball.rect.top < self.rect.bottom or self.rect.top < ball.rect.bottom < self.rect.bottom:
                ball.dy *= -1
                ball.dx *= -1


    def blitme(self):
        self.screen.blit(self.image, self.rect)
