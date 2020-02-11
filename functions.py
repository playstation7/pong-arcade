import pygame
from pygame.sprite import Group
from block import *


from restart import *

from live import *



def start_window(background,background_rect,screen,platform,ball,blocks):
    """Print message Press any to start at the beginning of the game"""
    while True:
        screen.blit(background,background_rect)
        platform.blit()
        ball.blit()
        blocks.draw(screen)
        print_counter(screen,'Press any to start',(100,270))
        pygame.display.flip() 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return True
                
        

def menu(background,background_rect,screen,volume):
    menu = True
    restart = Restart(screen)
    continue_b = Continue(screen)
    volume_b = Volume_button(screen,volume)
    exit = Exit(screen)
    
    while menu == True:
        screen.blit(background,background_rect)
        print_counter(screen,'Menu',(30,30),70,(161,40,48))
        restart.blit()
        continue_b.blit()
        volume_b.blit()
        exit.exit()
        exit.blit()
        if restart.reset() == True:
            return True
            
        if continue_b.continue_press() == True:
            break
        volume_b.continue_press()
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False 
                if event.key == pygame.K_q:
                    pygame.quit()

def check_events(platform,screen,background,background_rect,score,level,screen_width,screen_height,volume):
    """Input check """
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                platform.moving_right = True
            elif event.key == pygame.K_LEFT:
                platform.moving_left = True
            
            elif event.key == pygame.K_ESCAPE:
                
                if menu(background,background_rect,screen,volume) == True: #if True,main.py check_events return True too  and start new game
                    return True 
                    
    
                
                
                
           
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                platform.moving_right = False
            elif event.key == pygame.K_LEFT:
                platform.moving_left = False
        
        
def draw_lives(screen,lives):
    """Draw user lives"""
    indentation = 0
    for i in range(3):
        live = Live(screen)
        live.rect.x = (live.rect.width * i) + indentation + live.rect.width
        live.rect.y = live.rect.y + 10
        
        indentation += 10
        lives.append(live)
        
       

def create_blocks(screen,blocks,screen_width,screen_height,level):
    """Create blocks"""
    block = Block(screen)
    block_width = block.rect.width 
    block_height = block.rect.height
    number_blocks_x = 12  #number of blocks horizontally
    number_blocks_y = 6   #number of blocks vertically
    indentation = 0
    indentation_row = 0
    
    for block_row in range(number_blocks_y):
        for block_number in range(number_blocks_x):
            #Create a block and placing it in a row
            block = Block(screen,block_row+1)
            block.x = (block_width * block_number + indentation) 
            block.y = (block_height + block_height * block_row + indentation_row)
            block.rect.y = block.y
            block.rect.x = block.x 
            blocks.add(block)
            indentation += 1  #it allows add indentation between blocks
        indentation_row += 1
        indentation = 0
    difference_sides = ((screen_width - (block.rect.x + block_width)) / 2)
    for i in blocks:
        i.rect.x += difference_sides  #align blocks in the middle of the screen
        i.rect.y += 70
    
    for i in blocks:
        i.rect.y += (block_height * level)
        
    
def print_counter(screen,text,pos,size = 170,color = (250,218,221)):
    '''Blit number of points on screen'''
    f1 = pygame.font.Font(None, size)
    text1 = f1.render(str(text), 1, color)
    screen.blit(text1, pos)



    
def check_collisions(ball,blocks,screen,len_blocks,score,level,volume):
    '''Check collisions'''
    for bk in blocks:
            if ball.rect.left == bk.rect.right:
                if (ball.rect.top <= bk.rect.bottom and ball.rect.top >= bk.rect.top) or (ball.rect.bottom >= bk.rect.top and ball.rect.bottom <= bk.rect.bottom):
                    volume.play()
                    ball.mov_x_f = -ball.mov_x_f
                    blocks.remove(bk)
                    score += 1
                    return score
            elif ball.rect.right == bk.rect.left:
                if (ball.rect.top <= bk.rect.bottom and ball.rect.top >= bk.rect.top) or (ball.rect.bottom >= bk.rect.top and ball.rect.bottom <= bk.rect.bottom):
                    volume.play()
                    ball.mov_x_f = -ball.mov_x_f
                    blocks.remove(bk)
                    score += 1
                    return score 
            elif ball.rect.top == bk.rect.bottom:
                if (ball.rect.right >= bk.rect.left and ball.rect.right <= bk.rect.right) or (ball.rect.left <= bk.rect.right and ball.rect.left >= bk.rect.left):
                    volume.play()
                    ball.mov_y_f = -ball.mov_y_f
                    blocks.remove(bk)
                    score += 1
                    return score
            elif ball.rect.bottom == bk.rect.top:
                if (ball.rect.right >= bk.rect.left and ball.rect.right <= bk.rect.right) or (ball.rect.left <= bk.rect.right and ball.rect.left >= bk.rect.left):
                    volume.play()
                    ball.mov_y_f = -ball.mov_y_f
                    blocks.remove(bk)
                    score += 1
                    return score
    
        
        
            
    return score