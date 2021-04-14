class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (55,57,60)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 2
        self.bullet_height = 12
        self.bullet_color = (248, 248, 255)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.2
        self.bullet_speed = 2.0
        self.alien_speed = 0.5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
