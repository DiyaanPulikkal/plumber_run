from lib.player import Player
import lib.defaults as defaults
import random

class Consumable():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.asset = defaults.CONSUMABLE_ASSETS[type]
        self.spawned = False
        self.on_screen = False
        self.speed = defaults.CONSUMABLE_SPEED


    def take_effect_on_player(self, player: Player):
        self.on_screen = False
        if self.type == 0:
            player.heal(defaults.HEALTHORB_HEAL)
            return
        
        player.increase_score(defaults.GOLDCOIN_SCORE)
    
    def random_spawn(self):
        self.spawned = random.randint(0, 1) == 0
        if not self.spawned:
            return
        self.on_screen = True
        self.spawned = False

    def set_type(self, type):
        self.type = type
        self.asset = defaults.CONSUMABLE_ASSETS[type]

    def is_on_screen(self):
        return self.on_screen

    def get_width(self):
        return self.asset.get_width()
    
    def get_height(self):
        return self.asset.get_height()
        
