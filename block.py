#51 wide, 8px gap
import pygame
import random
import json

f = open('settings.json')
data = json.load(f)
screen_settings = data["Screen"]
block_settings = data["Block"]
class Block:
    def __init__(self, screen, x, y, row):
        images = ['images/tile000.png', 'images/tile001.png', 'images/tile002.png', 'images/tile003.png']
            
        self.image = pygame.image.load(images[row])
        self.image = pygame.transform.scale(self.image, (
                round(screen_settings["width"]/block_settings["columns"]),
                (round((screen_settings["width"]/block_settings["columns"])/2))
            ))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.x = x
        self.rect.y = y

    def check_ball_hit(self, ball):
        # If ball hits top or bottom
        if self.rect.top < ball.rect.top < self.rect.bottom or self.rect.top < ball.rect.bottom < self.rect.bottom:
            if self.rect.left < ball.rect.left < self.rect.right or self.rect.right > ball.rect.right > self.rect.left:
                ball.dy *= -1
                return True

        #elif because the top triggers the left and right collision

        # If ball hits left or right
        elif self.rect.right > ball.rect.left > self.rect.left or self.rect.left < ball.rect.right < self.rect.right:
            if self.rect.top < ball.rect.top < self.rect.bottom or self.rect.top < ball.rect.bottom < self.rect.bottom:
                ball.dy *= -1
                ball.dx *= -1
        
        return False
    def blitme(self):
        self.screen.blit(self.image, self.rect)