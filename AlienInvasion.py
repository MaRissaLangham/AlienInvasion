import sys
import pygame
from settings import Settings #Import the Settings class from Settings.py.

class AlienInvasion: #Overall class to manage game assets and behavior.
    
    def inIt(self):
       
        pygame.init() #Initialize the game, and create game resources.
        self.clock - pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode
        (
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.setCaption("Alien Invasion")
        self.bgColor = (230, 230, 230) #Set the background color.
        
    def run_game(self):
        
        while True:
            
            
            self.screen.fill(self.settings.bgColor)
            
            pygame.display.flip()
            self.clock.tick(60)
            