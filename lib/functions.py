from lib.player import Player
from lib.obstacle import Obstacle
import lib.defaults as defaults
from lib.consumable import Consumable
import pygame


def handle_jump(player: Player):
    if player.is_jumping:
        player.y -= player.jump_velocity
        player.jump_velocity -= defaults.GRAVITY
        if player.jump_velocity < -defaults.JUMP_HEIGHT:
            player.is_jumping = False
            player.jump_velocity = defaults.JUMP_HEIGHT
        return
    
    if player.y < defaults.HEIGHT - defaults.GROUND_HEIGHT - player.get_height():
        player.y += player.jump_velocity
        player.jump_velocity += 1
        return
    
    player.y = defaults.HEIGHT - defaults.GROUND_HEIGHT - player.get_height()

def handle_off_screen_obs(obstacle: Obstacle):
    if obstacle.x < -obstacle.get_width():
        obstacle.x = defaults.WIDTH
        obstacle.speed += 0.5
        obstacle.y = defaults.HEIGHT - defaults.GROUND_HEIGHT - obstacle.get_height()
        obstacle.on_screen = False

def handle_off_screen_cons(consumable: Consumable):
    if consumable.x < -consumable.get_width():
        consumable.x = defaults.WIDTH
        consumable.y = defaults.HEIGHT - defaults.GROUND_HEIGHT - consumable.get_height()
        consumable.on_screen = False

def generate_hitbox(obj):
    return pygame.Rect(obj.x + defaults.HITBOX_SIZE,
                       obj.y + defaults.HITBOX_SIZE,
                       obj.get_width() - defaults.HITBOX_SIZE,
                       obj.get_height() - defaults.HITBOX_SIZE
                       )