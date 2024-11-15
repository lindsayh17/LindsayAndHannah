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
snake_position = [snake_x, snake_y]
# start snake at 100, 100
current_snake = [[100-28, 100],
                 [100-21, 100],
                 [100-14, 100],
                 [100-7, 100],
                 [100, 100]]

# food dimensions
food_radius = 5
food_position = [200, 200]
food_available = False

# have 'food' randomly appear within the bounds of the walls
def spawn_food():
    food_position = [random.randint(food_radius, window_x - food_radius), random.randint(food_radius, window_y - food_radius)]
    # crect = pygame.Rect(points[0], points[1],
    #                     food_radius * 2, food_radius * 2)
    pygame.draw.circle(game_window, (0, 255, 0), food_position, food_radius)
    # pygame.draw.circle(game_window, (0, 255, 0), crect.center, food_radius)
    # return crect


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
        snake_y -= 7
    if direction == "DOWN":
        snake_y += 7
    if direction == "LEFT":
        snake_x -= 7
    if direction == "RIGHT":
        snake_x += 7

    spawn_food()

    # let it get longer
    snake_position = [snake_x, snake_y]
    current_snake.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
    else:
        current_snake.pop()

    game_window.fill((0, 0, 0))

    # function
    # if not food_available:
    #     circle = spawn_food()
    #     pygame.draw.circle(game_window, (0, 255, 0), circle.center, food_radius)
    #     food_available = True

    for x in current_snake:
        snake = pygame.Rect(x[0], x[1], 7, 7)
        pygame.draw.rect(game_window, (255, 0, 0), snake)


    # set up bounds for walls
    if snake_y < 0 or snake_y > window_y or snake_x > window_x or snake_x < 0:
        running = False

    # TODO: set up bounds for snake itself
    for block in current_snake[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            running = False

    # TODO: display score


    # TODO: increment score when eat the things
    if circle.center[0] == current_snake[0][0] and circle.center[1] == current_snake[0][1]:
        food_available = False



    for event in pygame.event.get():
        # Check if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Refresh game screen
    pygame.display.update()
    clock.tick(30)

# TODO: end screen

pygame.quit()
