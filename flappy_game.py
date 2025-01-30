import pygame
import random

# Initialize pygame
pygame.init()

# Set up game variables
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Game clock
clock = pygame.time.Clock()

# Load bird image
bird_width = 34
bird_height = 24
bird_img = pygame.Surface((bird_width, bird_height))
bird_img.fill(blue)

# Pipe settings
pipe_width = 50
pipe_height = random.randint(100, 300)
pipe_gap = 150
pipe_speed = 2  # Slow down pipe movement

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = screen_height // 2
        self.velocity = 0
        self.gravity = 0.25  # Reduced gravity
        self.lift = -6  # Increased lift

    def jump(self):
        self.velocity = self.lift

    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = screen_width
        self.height = random.randint(100, 300)
        self.top = self.height - screen_height
        self.bottom = self.height + pipe_gap

    def move(self):
        self.x -= pipe_speed

    def draw(self):
        pygame.draw.rect(screen, green, (self.x, self.top, pipe_width, screen_height + self.top))
        pygame.draw.rect(screen, green, (self.x, self.bottom, pipe_width, screen_height - self.bottom))

# Game function
def game_loop():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.move()

        # Add new pipes
        if pipes[-1].x < screen_width - 300:
            pipes.append(Pipe())

        # Move pipes and check if off-screen
        for pipe in pipes[:]:
            pipe.move()
            if pipe.x + pipe_width < 0:
                pipes.remove(pipe)
                score += 1

        # Collision detection
        for pipe in pipes:
            if bird.x + bird_width > pipe.x and bird.x < pipe.x + pipe_width:
                if bird.y < pipe.top + screen_height or bird.y + bird_height > pipe.bottom:
                    running = False

        # Game over condition if bird hits the ground or goes off-screen
        if bird.y >= screen_height or bird.y <= 0:
            running = False

        # Fill the screen with a color (white)
        screen.fill(white)

        # Draw bird and pipes
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        # Draw score
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()

        # Frame rate
        clock.tick(60)

    pygame.quit()

# Start the game loop
game_loop()
 