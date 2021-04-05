class Settings():
    """A class to store all settings for Alien invasion"""

    def __init__(self):
        """initialize the games settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        #self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 0)

        #Ship settings
        self.ship_speed_factor = 1.5

        #Bullets settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 85, 255, 33
        self.bullets_allowed = 3