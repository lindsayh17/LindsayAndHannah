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

#font
font = pygame.font.Font(None, 36)

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
food_size = 10
food_available = False
food_position = [random.randrange(food_size, (window_x//10)) * 10,
                  random.randrange(food_size, (window_y//10)) * 10]

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
        snake_y -= 10
    if direction == "DOWN":
        snake_y += 10
    if direction == "LEFT":
        snake_x -= 10
    if direction == "RIGHT":
        snake_x += 10


    # let it get longer
    snake_position = [snake_x, snake_y]
    current_snake.insert(0, list(snake_position))

    pygame.draw.rect(game_window, (0, 255, 0), pygame.Rect(
        food_position[0], food_position[1], food_size, food_size))

    # increment score when eat the things
    if food_position[0] == current_snake[0][0] and food_position[1] == current_snake[0][1]:
        score += 1
        food_available = False
    else:
        current_snake.pop()

    if not food_available:
        food_position = [random.randrange(food_size, (window_x // 10)) * 10,
                         random.randrange(food_size, (window_y // 10)) * 10]
    food_available = True

    game_window.fill((0, 0, 0))

    # redraw snake
    for x in current_snake:
        snake = pygame.Rect(x[0], x[1], 10, 10)
        pygame.draw.rect(game_window, (255, 0, 0), snake)

    # new food
    pygame.draw.rect(game_window, (0, 255, 0), pygame.Rect(
        food_position[0], food_position[1], food_size, food_size))

    # set up bounds for walls
    if snake_y < 0 or snake_y > window_y - 10 or snake_x > window_x - 10 or snake_x < 0:
        running = False

    # set up bounds for snake itself
    for block in current_snake[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            running = False



    # display score
    scoreText = font.render(f"Score: {score}", True, (152, 108, 106))
    game_window.blit(scoreText, (10, 10))


    for event in pygame.event.get():
        # Check if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Refresh game screen
    pygame.display.update()
    clock.tick(15)

# end screen

game_window.fill((34, 46, 80))

endText = font.render("Game Over", True, (152, 108, 106))

game_window.blit(endText, (window_x // 2 - endText.get_width() // 2, window_y // 2 - 30))

finalScoreText = font.render(f"Score: {score}", True, (152, 108, 106))

game_window.blit(finalScoreText, (window_x // 2
                        - finalScoreText.get_width() // 2, window_y // 2 + 10))

pygame.display.flip()
time.sleep(10)
pygame.quit()

pygame.quit()
