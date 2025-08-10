import pygame
import sys

# Init pygame
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Physics
y_pos = 0  # Starting vertical position
velocity = 0
initial_v = 5
gravity = -9.8
BLUE = (0, 0, 255)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Physics update
    velocity += initial_v+gravity * 0.1  # scaled by frame time
    y_pos += velocity * 0.1

    # Clear screen and draw object
    screen.fill((0, 0, 0))  # black background
    pygame.draw.circle(screen, BLUE, (250, int(y_pos)), 20)  # red ball

    pygame.display.flip()
    clock.tick(60)  # 60 FPS   

   