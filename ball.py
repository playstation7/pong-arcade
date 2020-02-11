from pygame.sprite import Sprite



import random
import pygame
from functions import draw_lives,menu



class Ball(Sprite):
    def __init__(self,platform,screen):
        super(Ball,self).__init__()
        self.platform = platform
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = (240, 115, 217)
        
        
        
        
        
        
        
        
        #self.rect = pygame.draw.circle(screen,self.color,(self.platform.image_rect.centerx,self.platform.image_rect.top),40)
        self.image = pygame.image.load('ball3.png')
        self.rect = self.image.get_rect()
        
        #Group for store lives
        self.lives = []
        draw_lives(screen,self.lives)
        
    
        self.rect.centerx = self.platform.rect.centerx
        self.rect.bottom = self.platform.rect.top - 5 
        
        #ball speed settings 
        self.mov_y_f = -0.99   #(random.randrange(1,10) / 10)
        self.mov_x_f =  (random.randrange(1,10) - random.randrange(1,10)) / 10
        self.mov_y = self.rect.bottom
        self.mov_x = self.rect.centerx
    


    def spawn(self):
        self.rect.centerx = self.platform.rect.centerx
        self.rect.bottom = self.platform.rect.top - 5 
        
        #ball speed settings 
        self.mov_y_f = -0.99   #(random.randrange(1,10) / 10)
        self.mov_x_f =  (random.randrange(1,10) - random.randrange(1,10)) / 10
        self.mov_y = self.rect.bottom
        self.mov_x = self.rect.centerx
        
        
    def update(self,blocks,background,background_rect,screen,volume):#!!!!!!!!
        
        if self.rect.top == self.screen_rect.top:
            volume.play()
            self.mov_y_f = -self.mov_y_f
        if self.rect.bottom >= self.platform.rect.top:
            if self.rect.centerx >= self.platform.rect.left and self.rect.centerx <= self.platform.rect.right:
                volume.play()
                self.mov_y_f = -self.mov_y_f
                self.mov_y -= 2 
                if self.rect.centerx >= self.platform.rect.centerx:
                    self.mov_x_f = +((self.rect.centerx - self.platform.rect.centerx)  / 100) + 0.05
                if self.rect.centerx < self.platform.rect.centerx:
                    self.mov_x_f = -((self.platform.rect.centerx - self.rect.centerx)  / 100)
               
        
        
        
        if self.rect.top == self.screen_rect.bottom:
            self.lives.pop()
            
            self.rect.centerx = self.platform.rect.centerx
            self.rect.bottom = self.platform.rect.top - 5 
            
            #Настройка скорости мяча 
            self.mov_y_f = -0.99   #(random.randrange(1,10) / 10)
            self.mov_x_f =  (random.randrange(1,10) - random.randrange(1,10)) / 10
            self.mov_y = self.rect.bottom
            self.mov_x = self.rect.centerx
            
            
            
            
            
            
        if self.rect.right == self.screen_rect.right:
            volume.play()
            self.mov_x_f = -self.mov_x_f
        
        if self.rect.left == self.screen_rect.left:
            volume.play()
            
            self.mov_x_f = -self.mov_x_f
        self.mov_x += self.mov_x_f
        self.mov_y += self.mov_y_f
        
        self.rect.y = self.mov_y
        self.rect.x = self.mov_x
        for live in self.lives:
                live.blit()
        
    def blit(self):
        self.screen.blit(self.image,self.rect)