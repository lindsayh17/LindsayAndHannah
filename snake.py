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
current_snake = [snake_x, snake_y]

# food dimensions
food_radius = 5


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

    prev_snake = current_snake
    current_snake = [snake_x, snake_y]

    snake = pygame.Rect(current_snake[0], current_snake[1], 5, 5)
    pygame.draw.rect(game_window, (255,0,0), snake)

    # gets rid of snake body by setting it to the background color
    previous_snake = pygame.Rect(prev_snake[0], prev_snake[1], 5, 5)
    pygame.draw.rect(game_window, (0,0,0), previous_snake)

    # TODO: get rid of snake body or let it get longer


    # set up bounds for walls
    if snake_y < 0 or snake_y > window_y or snake_x > window_x or snake_x < 0:
        running = False

    # TODO: set up bounds for snake itself

    # TODO: display score



    # TODO: increment score when eat the things
    #if


    for event in pygame.event.get():
        # Check if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Refresh game screen
    pygame.display.flip()
    clock.tick(30)

# TODO: end screen

pygame.quit()

# have 'food' randomly appear within the bounds of the walls
def spawn_food():
    points = [random.randint(0, window_x), random.randint(0, window_y)]
    crect = pygame.Rect(points[0] - food_radius, points[1] - food_radius,
                        food_radius * 2, food_radius * 2)
    pygame.draw.circle(game_window, (0, 255, 0), crect.center, food_radius)
