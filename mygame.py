import pygame
from sys import exit
from random import randint

def remove_background(image, bg_color=(255, 255, 255)):
    """Remove a single background color and make it transparent."""
    image = image.convert_alpha()
    width, height = image.get_size()

    for x in range(width):
        for y in range(height):
            r, g, b, a = image.get_at((x, y))
            if (r, g, b) == bg_color:
                image.set_at((x, y), (255, 255, 255, 0))
    return image

def display_score(score_val):
    score_surf = test_font.render(f"Score: {score_val}", False, (0,0,0))
    score_rect_local = score_surf.get_rect(center=(275, 50))
    screen.blit(score_surf, score_rect_local)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for ghost in obstacle_list:
            ghost["rect"].x -= ghost["speed"]
            screen.blit(ghost["surf"], ghost["rect"])
        obstacle_list = [g for g in obstacle_list if g["rect"].right > -50]
    return obstacle_list

def collisions(player_hitbox, obstacle_list):
    for ghost in obstacle_list:
        ghost_hitbox = ghost["rect"].inflate(-30, -20)
        if player_hitbox.colliderect(ghost_hitbox):
            return False
    return True

pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("04B_30__.TTF", 50)
message_font = pygame.font.Font("04B_30__.TTF", 25)

game_active = False
score = 0

Forest_surface = pygame.image.load("graphics/forest.jpg").convert()
Ground_surface = pygame.image.load("graphics/ground.jpg").convert()

GHOST_WIDTH = 80
GHOST_HEIGHT = 80

raw_ghost = pygame.image.load("graphics/ghost.png").convert_alpha()
ghost_no_bg = remove_background(raw_ghost, bg_color=(255, 255, 255))
ghost_surf = pygame.transform.smoothscale(ghost_no_bg, (GHOST_WIDTH, GHOST_HEIGHT))

obstacle_list = []
passed_obstacles = set()
next_ghost_id = 0

PLAYER_WIDTH = 120
PLAYER_HEIGHT = 200

raw_player = pygame.image.load("graphics/spiderman.png").convert_alpha()
player_surf = pygame.transform.smoothscale(raw_player, (PLAYER_WIDTH, PLAYER_HEIGHT))

player_rect = player_surf.get_rect(midbottom=(80, 300))
player_hitbox = player_rect.inflate(-40, -20)
player_gravity = 0

PLAYER_STAND_WIDTH = 150
PLAYER_STAND_HEIGHT = 180

raw_player_stand = pygame.image.load("graphics/spiderman_logo.png").convert_alpha()
player_stand_small = pygame.transform.smoothscale(raw_player_stand, (PLAYER_STAND_WIDTH, PLAYER_STAND_HEIGHT))

player_stand_rect = player_stand_small.get_rect(center=(350, 200))

game_name = test_font.render("DUDE", False, (132,133,35))
game_name_rect = game_name.get_rect(center=(350, 100))

game_message = message_font.render("Press SPACE to run", False, (165,45,23))
game_message_rect = game_message.get_rect(center=(350, 300))

# Faster spawn timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_hitbox.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -25

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -25

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_list.clear()
                passed_obstacles.clear()
                score = 0
                player_rect.midbottom = (80, 300)
                player_gravity = 0

        # FIXED — Ghost spawning guaranteed
        if event.type == obstacle_timer and game_active:
            if not obstacle_list:
                can_spawn = True
            else:
                last_rect = obstacle_list[-1]["rect"]
                required_gap = 300
                can_spawn = last_rect.x < 700 - required_gap

            if can_spawn:
                new_rect = ghost_surf.get_rect(bottomright=(randint(900, 1100), 300))

                next_ghost_id += 1
                ghost_data = {
                    "id": next_ghost_id,
                    "rect": new_rect,
                    "speed": randint(7, 8),
                    "surf": ghost_surf
                }
                obstacle_list.append(ghost_data)

    if game_active:

        screen.blit(Forest_surface, (0, 0))
        screen.blit(Ground_surface, (0, 300))

        display_score(score)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300

        player_hitbox.midbottom = player_rect.midbottom
        screen.blit(player_surf, player_rect)

        obstacle_list = obstacle_movement(obstacle_list)

        for ghost in obstacle_list:
            if ghost["rect"].right < player_rect.left:
                if ghost["id"] not in passed_obstacles:
                    passed_obstacles.add(ghost["id"])
                    score += 1

        if not collisions(player_hitbox, obstacle_list):
            game_active = False

    else:
        screen.fill((102,43,64))
        screen.blit(player_stand_small, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            final_score = test_font.render(f"Your score: {score}", False, (0,0,0))
            final_score_rect = final_score.get_rect(center=(350, 300))
            screen.blit(final_score, final_score_rect)

    pygame.display.update()
    clock.tick(70)

