"""
Simulation known as "Conway's Game of Life", 
a cellular automaton devised by John Horton Conway in 1970. 
We are going to build it with Python using Pygame.

Rules:
    - A live cell with two or fewer live neighbors dies.
    - A live cell with three live neighbors lives.
    - A live cell with more than three live neighbors dies.
    - A dead cell with exactly three live neighbors becomes alive.

Dependencies:
    pip install pygame


    
adjust grid is  the most important its the place where 
rules are applied 
""" 

import pygame
import sys
import random

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (128, 58, 140)

# Define screen size and tile size
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 5
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# Define frames per second
FPS = 5  # Lower FPS to better observe the simulation
SLOW_FPS = 2
FAST_FPS = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)) for i in range(num)])

def draw_grid(positions):
    # Draw grid lines
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))
    
    # Draw live cells
    for pos in positions:
        pygame.draw.rect(screen, BLUE, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def get_neighbors(pos):
    x,y = pos
    neighbors = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT]

def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()
    
    # Count live neighbors for each cell
    live_counts = {}
    for pos in positions:
        neighbors = get_neighbors(pos)
        all_neighbors.update(neighbors)
        for neighbor in neighbors:
            live_counts[neighbor] = live_counts.get(neighbor, 0) + 1
    
    # Apply rules to determine new positions
    for pos in all_neighbors:
        live_neighbor_count = live_counts.get(pos, 0)
        if pos in positions:
            if live_neighbor_count == 2 or live_neighbor_count == 3:
                new_positions.add(pos)
        elif live_neighbor_count == 3:
            new_positions.add(pos)
    
    return new_positions


def main():
    positions = set()  # each cell is unique
    running = True
    paused = False
    slow_mode = False
    fast_mode = False
    
    while running:
       
        if fast_mode:
            clock.tick(FAST_FPS)
        else:
            if slow_mode:
                clock.tick(SLOW_FPS)
            else:
                clock.tick(FPS)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    positions = gen(random.randrange(7, 9) * GRID_WIDTH)
                elif event.key == pygame.K_c:
                    slow_mode = not slow_mode
                elif event.key == pygame.K_s:
                    slow_mode = not slow_mode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // TILE_SIZE, y // TILE_SIZE
                pos = (col, row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

        if not paused:
            positions = adjust_grid(positions)

        screen.fill(BLACK)
        draw_grid(positions)
        pygame.display.update()

if __name__ == "__main__":
    main()