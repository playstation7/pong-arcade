import pygame


class Platform():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('platform2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 5 
        
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 4
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 4
        
    def blit(self):
        self.screen.blit(self.image,self.rect)