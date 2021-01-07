import pygame, sys, time, random
import pathfinders

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#YELLOW = 
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
GRID_SIZE = 10
START = (0, 0)
END = (59,59)


def main():
    global SCREEN, CLOCK 
    pygame.init()
    pygame.display.set_caption('Path Finder Visualization')
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(BLACK)
    
    grid_array = initialize_grid()
    draw_grid()
    while True:
        for event in pygame.event.get():
            if (pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEMOTION) or (event.type == pygame.mouse.get_pressed()[0]):
                pos = pygame.mouse.get_pos()
                x = pos[0] // GRID_SIZE; y = pos[1] // GRID_SIZE
                rect = pygame.Rect(x*GRID_SIZE + 1, y*GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)
                pygame.draw.rect(SCREEN, RED, rect)
                grid_array[y][x] = 1
            if (pygame.mouse.get_pressed()[2] and event.type == pygame.MOUSEMOTION) or (event.type == pygame.mouse.get_pressed()[2]):
                pos = pygame.mouse.get_pos()
                x = pos[0] // GRID_SIZE; y = pos[1] // GRID_SIZE
                rect = pygame.Rect(x*GRID_SIZE + 1, y*GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)
                pygame.draw.rect(SCREEN, BLACK, rect)
                grid_array[y][x] = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    path, closed_set = pathfinders.A_Star(START, END, grid_array, distance_metric=pathfinders.euclidean_distance)
                    draw_path(closed_set)
                    draw_path(path, color=BLUE)
                if event.key == pygame.K_BACKSPACE:
                    grid_array = initialize_grid()
                    SCREEN.fill(BLACK)
                    draw_grid()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def draw_path(path, color=GREEN):
    if path is None:
        return
    for node in path:
        x = node[1]; y = node[0]
        rect = pygame.Rect(x*GRID_SIZE + 1, y*GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(SCREEN, color, rect)
        pygame.display.update()

def draw_grid(color=WHITE, edge=1):
    block_size = GRID_SIZE
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(SCREEN, color, rect, edge)

def initialize_grid():
    return [[0 for _ in range(WINDOW_HEIGHT // GRID_SIZE)] for _ in range(WINDOW_HEIGHT // GRID_SIZE)]

if __name__=="__main__":
    main()
