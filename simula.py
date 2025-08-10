import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Spring parameters
rest_position = 200
position = 300.0
velocity = 0.0
k = 10
m = 2
dt = 0.05

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spring physics
    force = -k * (position - rest_position)
    acceleration = force / m
    velocity += acceleration * dt
    position += velocity * dt

    # Drawing
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (100, 100, 255), (200, int(position)), 20)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
