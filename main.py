import pygame
from lib import defaults, functions, io
from lib.obstacle import Obstacle
from lib.player import Player
from lib.consumable import Consumable
import random
import sys


# initialize pygame engine
pygame.init()


def main():
    # CREATE SCREEN
    screen = pygame.display.set_mode((defaults.WIDTH, defaults.HEIGHT))
    pygame.display.set_caption("Plumber Run")

    background_image = defaults.BG_ASSET

    # player instances
    player1 = Player(defaults.WIDTH // 2, defaults.HEIGHT - defaults.GROUND_HEIGHT -
                     defaults.PLAYER1_ASSET.get_height(), defaults.PLAYER1_ASSET)
    player2 = Player(defaults.WIDTH // 2, defaults.HEIGHT - defaults.GROUND_HEIGHT -
                     defaults.PLAYER2_ASSET.get_height(), defaults.PLAYER2_ASSET)

    # obstacle variables
    obstacle1 = Obstacle(defaults.WIDTH, defaults.HEIGHT - defaults.GROUND_HEIGHT -
                         defaults.BARRIER_ASSET.get_height(), 1, defaults.BARRIER_ASSET)
    obstacle2 = Obstacle(defaults.WIDTH, defaults.HEIGHT - defaults.GROUND_HEIGHT -
                         defaults.BARRIER_ASSET.get_height(), 1, defaults.BARRIER_ASSET)
    obstacle3 = Obstacle(defaults.WIDTH, defaults.HEIGHT - defaults.GROUND_HEIGHT -
                         defaults.BARRIER_ASSET.get_height(), 1, defaults.BARRIER_ASSET)
    obstacles = [obstacle1, obstacle2, obstacle3]

    winner = None

    # consumable variables
    consumable1 = Consumable(defaults.WIDTH, defaults.HEIGHT -
                             defaults.GROUND_HEIGHT - defaults.HEALTHORB_ASSET.get_height(), 1)
    # game loop
    running = True
    clock = pygame.time.Clock()
    accumulated_frames = 0
    while running:
        # check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # handle player input (0 is mario and 1 is luigi)
        if not io.is_walking_forward(0) and player1.x > 0:
            player1.x -= defaults.PLAYER_SPEED
        if io.is_walking_forward(0) and player1.x < defaults.WIDTH - player1.get_width():
            player1.x += defaults.PLAYER_SPEED
        if io.is_jumping(0) and not player1.is_jumping:
            player1.is_jumping = True

        if not io.is_walking_forward(1) and player2.x > 0:
            player2.x -= defaults.PLAYER_SPEED
        if io.is_walking_forward(1) and player2.x < defaults.WIDTH - player2.get_width():
            player2.x += defaults.PLAYER_SPEED
        if io.is_jumping(1) and not player2.is_jumping:
            player2.is_jumping = True

        functions.handle_jump(player1)
        functions.handle_jump(player2)

        # randomly spawn obstacles
        for i in range(len(obstacles)):
            if accumulated_frames % (i*30 + 90) == 0 and not obstacles[i].on_screen:
                obstacles[i].random_spawn()

        # randomly spawn consumables
        if accumulated_frames % defaults.CONSUMABLE_SPAWN_RATE == 0 and not consumable1.on_screen:
            consumable_type = random.randint(0, 1)
            consumable1.set_type(consumable_type)
            consumable1.random_spawn()

        # update each obstacle's position
        for obstacle in obstacles:
            if obstacle.is_on_screen():
                obstacle.x -= obstacle.speed

        # update consumable position
        if consumable1.is_on_screen():
            consumable1.x -= consumable1.speed

        # initialize hitboxes
        player1_rect = functions.generate_hitbox(player1)
        player2_rect = functions.generate_hitbox(player2)
        obstacle1_rect = functions.generate_hitbox(obstacle1)
        obstacle2_rect = functions.generate_hitbox(obstacle2)
        obstacle3_rect = functions.generate_hitbox(obstacle3)
        consumable1_rect = functions.generate_hitbox(consumable1)


        # check for collision
        for player in [(player1, player1_rect), (player2, player2_rect)]:
            for obstacle in [(obstacle1, obstacle1_rect), (obstacle2, obstacle2_rect), (obstacle3, obstacle3_rect)]:
                if player[1].colliderect(obstacle[1]):
                    player[0].take_damage(obstacle[0].damage)
                    obstacle[0].x = defaults.WIDTH
            if player[1].colliderect(consumable1_rect):
                consumable1.take_effect_on_player(player[0])
                consumable1.x = defaults.WIDTH

        # check if player is dead
        if player1.is_dead() or player2.is_dead():
            if player1.is_dead():
                winner = 1
            else:
                winner = 0
            running = False

        # update player score
        player1.increase_score(defaults.SCORE_MULTIPLIER)
        player2.increase_score(defaults.SCORE_MULTIPLIER)

        # draw everything
        screen.blit(background_image, (0, 0))
        screen.blit(player1.asset, (player1.x, player1.y))
        screen.blit(player2.asset, (player2.x, player2.y))
        for obstacle in obstacles:
            if obstacle.is_on_screen():
                screen.blit(obstacle.asset, (obstacle.x, obstacle.y))
        if consumable1.is_on_screen():
            screen.blit(consumable1.asset, (consumable1.x, consumable1.y))

        # display player score
        gameOverFont = pygame.font.Font(None, 36)
        player1_score_text = gameOverFont.render(f"Player 1 Score: {str(player1.score)}, Health: {str(player1.health)}", True, defaults.RED)
        player2_score_text = gameOverFont.render(f"Player 2 Score: {str(player2.score)}, Health: {str(player2.health)}", True, defaults.BLUE)
        screen.blit(player1_score_text, (10, 10))
        screen.blit(player2_score_text, (defaults.WIDTH - 390, 10))
        pygame.display.flip()

        # check if objects has gone off screen
        for obstacle in [obstacle1, obstacle2, obstacle3]:
            functions.handle_off_screen_obs(obstacle)
        functions.handle_off_screen_cons(consumable1)

        # count frames to decide when to spawn obstacles
        accumulated_frames += 1
        if accumulated_frames % 3000 == 0 and accumulated_frames != 0:
            accumulated_frames = 0
        clock.tick(defaults.FPS)

    # create game over screen
    gameOverFont = pygame.font.Font(None, 72)
    game_over_text = gameOverFont.render("Game Over!", True, (128, 0, 0))
    press_any_key_text = pygame.font.Font(None, 36)
    press_any_key_text = press_any_key_text.render(
        "Press button to restart", True, (0, 0, 0))
    screen.blit(game_over_text, (defaults.WIDTH //
                2 - 150, defaults.HEIGHT // 2 - 50))
    screen.blit(press_any_key_text, (defaults.WIDTH //
                2 - 150, defaults.HEIGHT // 2 + 50))

    pygame.display.flip()
    return winner

if __name__ == "__main__":
    while True:
        pygame.time.delay(10)
        winner = main()
        if winner == 0:
            io.turn_on_led(0)
        else:
            io.turn_on_led(1)
        waiting_for_keydown = True
        while waiting_for_keydown:
            if io.is_button_pressed():
                io.turn_off_led(0)
                io.turn_off_led(1)
                waiting_for_keydown = False
                pygame.time.delay(800)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    io.turn_off_led(0)
                    io.turn_off_led(1)
                    pygame.quit()
                    io.cleanup()
                    sys.exit()
                    break
