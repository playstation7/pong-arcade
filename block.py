from pygame.sprite import Sprite
import pygame

class Block(Sprite):
    """ Класс для создание блоков"""
    def __init__(self,screen,block_row=1):
        super(Block,self).__init__()
        self.screen = screen
        self.block_row = block_row
        
        image_name = 'block{}.png'.format(self.block_row)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blit(self):
        self.screen.blit(self.image,self.rect)