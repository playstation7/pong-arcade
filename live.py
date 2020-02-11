import pygame
from pygame.sprite import Sprite


class Live(Sprite):
    def __init__(self,screen):
        super(Live,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('heart.png')
        self.rect = self.image.get_rect()
        
        
        
        self.lives = 3
        
        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y
        
    def blit(self):
        #self.image = pygame.transform.rotate(self.image,1)
        self.screen.blit(self.image,self.rect)



    
    '''def rotate(self):
            self.rotate_sch += 1
            if self.rotate_sch <= 6:
                self.image_r = pygame.transform.rotate(self.image,-(self.rotate_sch * 60))
                time.sleep(0.1)'''
            
            
            