# importing modules
import pygame
import time
import random

# Window size
window_x = 720
window_y = 480

# Initializing pygame
pygame.init()

# Initialize game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# initial score
score = 0

#clock
clock = pygame.time.Clock()

#initial running status
running = True

# initialize snake
direction = "RIGHT"
snake_x = 100
snake_y = 100

# Main Function
while running:

    # keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = "UP"
    if keys[pygame.K_DOWN]:
        direction = "DOWN"
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"

    if direction == "UP":
        snake_y -= 5
    if direction == "DOWN":
        snake_y += 5
    if direction == "LEFT":
        snake_x -= 5
    if direction == "RIGHT":
        snake_x += 5

    snake = pygame.Rect(snake_x, snake_y, 5, 5)
    pygame.draw.rect(game_window, (255,0,0), snake)

    # TODO: get rid of snake body or let it get longer

    # TODO: display score

    # TODO: set up bounds for walls (and maybe snake itself - store in an array?)

    for event in pygame.event.get():
        # Check if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Refresh game screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
