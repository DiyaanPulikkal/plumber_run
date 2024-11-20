import pygame


# General
WIDTH = 800
HEIGHT = 400
GROUND_HEIGHT = 15
FPS = 60
SCORE_MULTIPLIER = 1
GRAVITY = 1
HITBOX_SIZE = 20  # INCREASE THIS VALUE TO MAKE THE HITBOX SMALLER
BG_ASSET = pygame.image.load("assets/bg.jpg")


# Colors
WHITE = (255, 255, 255)
RED = (188, 24, 35)  # Player 1
BLUE = (0, 74, 173)  # Player 2


# Player
PLAYER1_ASSET = pygame.image.load("assets/redman.png")
PLAYER2_ASSET = pygame.image.load("assets/greenman.png")
PLAYER_SPEED = 5
PLAYER_HEALTH = 10
JUMP_HEIGHT = 20


# Obstacle
BARRIER_ASSET = pygame.image.load("assets/barrier.png")
SPIKETRAP_ASSET = pygame.image.load("assets/spiketrap.png")
THORN_ASSET = pygame.image.load("assets/thorn.png")
OBSTACLE_ASSETS = [BARRIER_ASSET, THORN_ASSET, SPIKETRAP_ASSET]
OBSTACLE_SPEED = 3


# Consumable
HEALTHORB_ASSET = pygame.image.load("assets/health_orb.png")
HEALTHORB_HEAL = 1
GOLDCOIN_ASSET = pygame.image.load("assets/coin.png")
GOLDCOIN_SCORE = 350
CONSUMABLE_ASSETS = [HEALTHORB_ASSET, GOLDCOIN_ASSET]
CONSUMABLE_SPEED = 3
CONSUMABLE_SPAWN_RATE = 300  # every X frames
