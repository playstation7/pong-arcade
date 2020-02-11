import pygame
import sys

from settings import *


class Restart():
    """Class for creating restart button in menu"""
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('reset.png')
        self.rect = self.image.get_rect()
        
        self.rect.x  = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
    
    def blit(self):
        self.screen.blit(self.image,self.rect)
    
    
    def reset(self):
        """Check cursor position,that user can press reset button"""
        if pygame.mouse.get_pos()[0] > self.rect.x and pygame.mouse.get_pos()[0] < self.rect.x + self.rect.width:
            if pygame.mouse.get_pos()[1] > self.rect.y and pygame.mouse.get_pos()[1] < self.rect.y + self.rect.height:
                self.image = pygame.image.load('images/reset2.png')
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            return True
                    
                            
                          
                            
                            
                    
            else:
                self.image = pygame.image.load('images/reset.png')
        else:
                self.image = pygame.image.load('images/reset.png')
class Continue():
    """Class for creating continue button in menu"""
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/continue.png')
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.centerx - 60
        self.rect.y = self.screen_rect.centery 
    
    def blit(self):
        self.screen.blit(self.image,self.rect)
    
    def continue_press(self):
        if pygame.mouse.get_pos()[0] > self.rect.x and pygame.mouse.get_pos()[0] < self.rect.x + self.rect.width:
            if pygame.mouse.get_pos()[1] > self.rect.y and pygame.mouse.get_pos()[1] < self.rect.y + self.rect.height:
                self.image = pygame.image.load('images/continue2.png')
                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            return True
                    
            else:
                self.image = pygame.image.load('images/continue.png')
                
        else:
                self.image = pygame.image.load('images/continue.png')
                

class Volume_button():
    """Класс для создания кнопки выход"""
    def __init__(self,screen,volume):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.volume = volume
        if self.volume.volume_status:
            self.image = pygame.image.load('images/volumueon.png')#pygame.transform.rotate(pygame.image.load('images/volumueon.png'),25)
            
        else:
            self.image = pygame.image.load('images/volumueoff.png')
        
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.centerx + 60
        self.rect.y = self.screen_rect.centery 
        
        
    
    def blit(self):
        self.screen.blit(self.image,self.rect)
        
    def continue_press(self):
        if pygame.mouse.get_pos()[0] > self.rect.x and pygame.mouse.get_pos()[0] < self.rect.x + self.rect.width:
            if pygame.mouse.get_pos()[1] > self.rect.y and pygame.mouse.get_pos()[1] < self.rect.y + self.rect.height:
                 
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.volume.volume_status:
                                self.image = pygame.image.load('images/volumueoff.png')
                                self.volume.volume_status = False
                            else:
                                self.image = pygame.image.load('images/volumueon.png')
                                self.volume.volume_status = True
                                
class Exit():
    """Класс для создания кнопки выхода"""
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/exit.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.width - 60
        self.rect.y = self.screen_rect.bottom - 60
        
        #Настройки для создания анимации
        self.color = (253,124,165)
        #self.pos_x = self.rect.x + round((self.rect.width / 2))
        #self.pos_x_2 = self.rect.x
        #self.pos = (self.pos_x,self.rect.y,self.pos_x_2,self.rect.y + self.rect.height)
        self.pos_x = self.rect.centerx
        self.pos_y = self.rect.centery
        
        #self.rect2 = self.image2.get_rect()
        self.indentation = 0 #indentation необходим для того,чтобы анимация не исчезала после удаления курсора с кнопки выхода
        
        
        self.f1 = pygame.font.Font(None, 30)
        self.text1 = self.f1.render('exit', 1, (136,0,27))
        
    
    
    def blit(self):
        self.screen.blit(self.image,self.rect)
    
    def exit(self):
        if pygame.mouse.get_pos()[0] > self.rect.x - self.indentation and pygame.mouse.get_pos()[0] < self.rect.x + self.rect.width:
            if pygame.mouse.get_pos()[1] > self.rect.y and pygame.mouse.get_pos()[1] < self.rect.y + self.rect.height:
                self.indentation = 70
                pygame.draw.circle(self.screen,self.color,(self.pos_x,self.pos_y),24)
                self.pos_x -= 1
                self.screen.blit(self.text1,(self.pos_x-18,self.pos_y-10))
                if self.pos_x < self.rect.centerx - 70:
                    self.pos_x += 1
                    if pygame.mouse.get_pos()[0] > self.pos_x - 25 and pygame.mouse.get_pos()[0] < self.pos_x + 25:
                        if pygame.mouse.get_pos()[1] > self.pos_y - 25 and pygame.mouse.get_pos()[1] < self.pos_y + 25:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        pygame.quit()
            else:
                self.pos_x = self.rect.centerx
                self.pos_y = self.rect.centery
                self.indentation = 0
                
                  
                
                
                
                
            
                            
                            
                            
                            
        
                                
                            
                    
                            
    
    
    
                
    