import random
import lib.defaults as defaults

class Obstacle():
    def __init__(self, x, y, damage, asset):
        self.x = x
        self.y = y
        self.speed = defaults.OBSTACLE_SPEED
        self.damage = damage
        self.asset = asset
        self.spawned = False
        self.on_screen = False

    def random_spawn(self):
        self.spawned = random.randint(0, 1) == 0
        if not self.spawned:
            return
        rand_int = random.randint(0, 2)
        self.asset = defaults.OBSTACLE_ASSETS[rand_int]
        self.damage = rand_int + 1
        self.on_screen = True
        self.spawned = False
    
    def get_width(self):
        return self.asset.get_width()
    
    def get_height(self):
        return self.asset.get_height()
    
    def is_on_screen(self):
        return self.on_screen