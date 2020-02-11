import pygame

class Settings():
    """Class for storing game settings"""
    def __init__(self):
        self.volume_status = True
        self.sound_hit = pygame.mixer.Sound("hit.ogg")
        
        
        self.score = 0
        self.level = 1
        
        
        self.screen_width = 1200
        self.screen_height = 400
    def play(self):
        if self.volume_status:
            self.sound_hit.play()
    
    