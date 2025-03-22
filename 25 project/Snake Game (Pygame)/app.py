import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

snake = [(100, 100)]
direction = (10, 0)
food = (random.randint(0, WIDTH//10)*10, random.randint(0, HEIGHT//10)*10)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: direction = (0, -10)
    if keys[pygame.K_DOWN]: direction = (0, 10)
    if keys[pygame.K_LEFT]: direction = (-10, 0)
    if keys[pygame.K_RIGHT]: direction = (10, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head == food:
        food = (random.randint(0, WIDTH//10)*10, random.randint(0, HEIGHT//10)*10)
    else:
        snake.pop()

    snake.insert(0, new_head)
    win.fill((0, 0, 0))
    for part in snake:
        pygame.draw.rect(win, (0, 255, 0), (part[0], part[1], 10, 10))
    pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], 10, 10))

    pygame.display.update()

pygame.quit()
