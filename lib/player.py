import lib.defaults as defaults

class Player():
    def __init__(self, x, y, asset):
        self.x = x
        self.y = y
        self.asset = asset
        self.jump_velocity = defaults.JUMP_HEIGHT
        self.health = defaults.PLAYER_HEALTH
        self.score = 0
        self.is_jumping = False
    
    def heal(self, amount):
        self.health += amount

    def take_damage(self, damage):
        self.health -= damage
    
    def is_dead(self):
        return self.health <= 0

    def increase_score(self, multiplier):
        self.score += multiplier
    
    def get_width(self):
        return self.asset.get_width()
    
    def get_height(self):
        return self.asset.get_height()
