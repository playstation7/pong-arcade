import pygame
import sys
import random
from pygame.sprite import Sprite
from pygame.sprite import Group
import time



from restart import *
from live import *
from functions import *
from ball import *
from platform import *
from block import *
from settings import *


                
               
def run():
    
    pygame.init()
    
    #settings
    settings = Settings()
    
    
    
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))#,pygame.FULLSCREEN
    #screen.fill((230,230,230))
    pygame.display.set_caption('2Dbox')
    
    
    counter = 'Start'
    
    #Group are storing blocks
    blocks = Group()
    create_blocks(screen,blocks,settings.screen_width,settings.screen_height,settings.level)
    len_blocks = len(blocks)
   
    #Backgroungs settings
    background = pygame.image.load('pattern.bmp')
    background_rect = background.get_rect()
    platform = Platform(screen)
    
    
    ball = Ball(platform,screen) #create ball
    
    
    start_window(background,background_rect,screen,platform,ball,blocks)
    
    
    while True:
        
        res = check_events(platform,screen,background,background_rect,settings.score,settings.level,settings.screen_width,settings.screen_height,settings)
        if res == True:  #if res True,that start new game
            run()
        
        
        screen.blit(background,background_rect)
        
        
          
        
        blocks.draw(screen)
        
        
        settings.score = check_collisions(ball,blocks,screen,len_blocks,settings.score,settings.level,settings)
        
        
        
        platform.update()
        platform.blit()
        
        
        
        
        
        
        if len(blocks) == 0:
            settings.level += 1
            create_blocks(screen,blocks,settings.screen_width,settings.screen_height,settings.level)
            ball.spawn()
            
        
        if settings.level > 5:
            print_counter(screen,'You win!',(500,270))
            ball.mov_x_f = 0 
            ball.mox_y_f = 0
        
        if len(ball.lives) < 1:
            
            print_counter(screen,'You lose',(500,270))
            ball.mov_x_f = 0 
            ball.mox_y_f = 0
        
        else:
            ball.update(blocks,background,background_rect,screen,settings)
            ball.blit()
            print_counter(screen,settings.score,(500,270))  #print number score
        pygame.display.flip()    
        
        
run()
