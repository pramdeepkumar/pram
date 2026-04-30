# Realistic Ludo Game (Python + Pygame)
# Install pygame first:
# pip install pygame

import pygame
import random
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real Ludo Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 255)
YELLOW = (240, 220, 50)
GRAY = (200, 200, 200)

font = pygame.font.SysFont("Arial", 28)

# Token positions
players = {
    "red": [(100, 100)],
    "green": [(700, 100)],
    "yellow": [(100, 700)],
    "blue": [(700, 700)]
}

turns = ["red", "green", "yellow", "blue"]
turn_index = 0
dice_value = 1

# Path positions (simple demo path)
path = [
    (400, 700), (400, 650), (400, 600), (400, 550),
    (400, 500), (450, 500), (500, 500), (550, 500),
    (600, 500), (650, 500), (700, 500),
    (700, 450), (700, 400), (650, 400), (600, 400),
    (550, 400), (500, 400), (450, 400), (400, 400),
]

player_steps = {
    "red": 0,
    "green": 0,
    "yellow": 0,
    "blue": 0
}


def draw_board():
    screen.fill(WHITE)

    # Home Areas
    pygame.draw.rect(screen, RED, (0, 0, 300, 300))
    pygame.draw.rect(screen, GREEN, (500, 0, 300, 300))
    pygame.draw.rect(screen, YELLOW, (0, 500, 300, 300))
    pygame.draw.rect(screen, BLUE, (500, 500, 300, 300))

    # Center
    pygame.draw.rect(screen, GRAY, (300, 300, 200, 200))

    # Grid lines
    for i in range(0, 801, 50):
        pygame.draw.line(screen, BLACK, (i, 0), (i, 800), 1)
        pygame.draw.line(screen, BLACK, (0, i), (800, i), 1)


def draw_tokens():
    color_map = {
        "red": RED,
        "green": GREEN,
        "yellow": YELLOW,
        "blue": BLUE
    }

    for player, positions in players.items():
        for pos in positions:
            pygame.draw.circle(screen, color_map[player], pos, 20)


def move_player(player, steps):
    current = player_steps[player]
    current += steps

    if current >= len(path):
        current = len(path) - 1

    player_steps[player] = current
    players[player][0] = path[current]


def draw_ui():
    current_player = turns[turn_index]

    text = font.render(
        f"Turn: {current_player.upper()} | Dice: {dice_value}",
        True,
        BLACK
    )
    screen.blit(text, (220, 760))

    button = pygame.draw.rect(screen, BLACK, (320, 710, 160, 40))
    btn_text = font.render("ROLL DICE", True, WHITE)
    screen.blit(btn_text, (340, 715))

    return button


clock = pygame.time.Clock()

while True:
    clock.tick(60)

    button = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if button and button.collidepoint(mouse):
                dice_value = random.randint(1, 6)

                current_player = turns[turn_index]
                move_player(current_player, dice_value)

                turn_index = (turn_index + 1) % 4

    draw_board()
    draw_tokens()
    button = draw_ui()

    pygame.display.update()