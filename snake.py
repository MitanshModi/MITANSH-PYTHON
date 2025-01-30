import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Define colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

# Set window dimensions
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(2)

# Snake settings
snake_size = 10
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Define fonts
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Function to display the score
def user_score(score):
    number = score_font.render("Score: " + str(score), True, red)
    window.blit(number, [0, 0])

# Function to draw the snake
def game_snake(snake_size, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])

# Function to display message when game is over
def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = win_width / 2
    y1 = win_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Snake length and body positions
    snake_length_list = []
    snake_length = 1

    # Spawn the first food
    foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(grey)
            message("You Lost! Press P to Play Again or Q to Quit.")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        # Check for boundaries and collisions
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)

        # Draw food
        pygame.draw.rect(window, yellow, [foodx, foody, snake_size, snake_size])

        # Update snake body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_length_list.append(snake_head)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        # Check if snake collides with itself
        for x in snake_length_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        game_snake(snake_size, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        # Set snake speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
