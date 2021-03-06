import pygame

class Ship():

    def __init__(self, ai_setting, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_setting = ai_setting
        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)   

    def update(self):
        """Update the ships position based on the movement falg"""
        #Update the ships center value not the rect
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_setting.ship_speed_factor 
        elif self.moving_left and (self.rect.left > 0): #In the book this is not a elif is a if
            self.center -= self.ai_setting.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center     