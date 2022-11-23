# Pygame collaboration with functions
# From the menu Click to open level one
# IN level one click to get points
# In level one escape returns to the menu


import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


def menu(game_state):
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[RUNNING] = False
        elif event.type == QUIT:
            game_state[RUNNING] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("GO to level one!")
            game_state[CURRENT_LEVEL] = "level_one"

    # DRAWING
    screen.fill((0, 0, 0))  # always the first drawing command
    pygame.draw.circle(screen, (200, 0, 255), (circle_x, circle_y), 30)
    title_text = title_font.render('Menu', False, (200, 200, 200))
    text_width = title_text.get_width()
    screen.blit(title_text, (WIDTH//2 - text_width//2, HEIGHT * 0.33))

    score_text = title_font.render("Score: " + str(game_state[SCORE]), False, (0, 128, 0))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT * 0.66))


def level_one(game_state):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[CURRENT_LEVEL] = "menu"
        elif event.type == QUIT:
            game_state[RUNNING] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_state[SCORE] += 1
            print(game_state[SCORE])
    
    # DRAWING
    screen.fill((100, 100, 100))


pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
title_font = pygame.font.SysFont('Arial', 50)

game_state = [
    True,       # 0 - running
    "menu",     # 1 - current_screen
    0,          # 2 - player score
]

RUNNING = 0
CURRENT_LEVEL = 1
SCORE = 2

# ---------------------------
pygame.event.clear()

while game_state[RUNNING]:
    
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    if game_state[CURRENT_LEVEL] == "menu":
        menu(game_state)
    elif game_state[CURRENT_LEVEL] == "level_one":
        level_one(game_state)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------