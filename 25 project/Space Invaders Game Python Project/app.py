import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 🚀👾")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Player settings
player_x, player_y = WIDTH // 2, HEIGHT - 80
player_speed = 5

# Enemy settings
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = 50
enemy_speed = 2

# Bullet settings
bullet_x, bullet_y = 0, 0
bullet_speed = 7
bullet_state = "ready"  # "ready" means not visible

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE] and bullet_state == "ready":
        bullet_x, bullet_y = player_x + 20, player_y
        bullet_state = "fire"

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x = random.randint(50, WIDTH - 50)
        enemy_y = 50

    # Bullet movement
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    # Collision detection
    if bullet_y < enemy_y + 40 and bullet_x in range(enemy_x, enemy_x + 40):
        enemy_x, enemy_y = random.randint(50, WIDTH - 50), 50
        bullet_state = "ready"

    # Draw player, enemy, bullet
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    if bullet_state == "fire":
        screen.blit(bullet_img, (bullet_x, bullet_y))

    pygame.display.update()

pygame.quit()
