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

#initial running status
running = True

# initialize snake
snake_x = 100
snake_y = 100

# Main Function
while running:

    # keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_y -= 5
    if keys[pygame.K_DOWN]:
        snake_y += 5
    if keys[pygame.K_LEFT]:
        snake_x -= 5
    if keys[pygame.K_RIGHT]:
        snake_x += 5

    square = pygame.Rect(snake_x, snake_y, 5, 5)

    if snake_x > window_x or snake_y > window_y:
        running = False

    # Refresh game screen
    pygame.display.flip()
