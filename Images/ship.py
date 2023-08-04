import pygame

class Ship:
    
    #Initialize the ship and set its starting position."""
    def inIt(self, aiGame):
        self.screen = aiGame.screen
        self. screenRect = aiGame.screen.get_rect()
        
        # Load the ship image and get its rect.
        