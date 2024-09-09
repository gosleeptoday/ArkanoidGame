import pygame
import random
from config import *

def create_blocks():
    blocks = []
    block_padding = 5
    num_cols = 12
    num_rows = 6
    start_x = (SCREEN_WIDTH - (BLOCK_WIDTH + block_padding) * num_cols) // 2
    start_y = 50

    for row in range(num_rows):
        for col in range(num_cols):
            block = pygame.Rect(start_x + col * (BLOCK_WIDTH + block_padding),
                                start_y + row * (BLOCK_HEIGHT + block_padding),
                                BLOCK_WIDTH, BLOCK_HEIGHT)
            if random.random() < 0.1:
                blocks.append((block, BONUS_BLOCK_COLOR))
            else:
                blocks.append((block, (block.x % 255, block.y % 255, 200)))
    return blocks

def draw_blocks(screen, blocks):
    for block, color in blocks:
        pygame.draw.rect(screen, color, block)
        pygame.draw.rect(screen, BLACK, block, 2)

def reset_ball(ball, ball_speed):
    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2
    ball_speed[0] = random.choice([-7, 7])
    ball_speed[1] = -7

def draw_text(screen, text, x, y, color=WHITE, font=font, center=False):
    surface = font.render(text, True, color)
    if center:
        x = SCREEN_WIDTH // 2 - surface.get_width() // 2
    screen.blit(surface, (x, y))

def show_game_over_overlay(screen, score):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_COLOR)
    screen.blit(overlay, (0, 0))
    
    draw_text(screen, "Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, color=GOLD, center=True)
    draw_text(screen, f"Score: {score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, color=WHITE, center=True)
    draw_text(screen, "Press R to restart or Esc to quit", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, color=WHITE, center=True)

def show_instructions(screen):
    instructions_x = SCREEN_WIDTH - 350
    draw_text(screen, "Controls:", instructions_x, SCREEN_HEIGHT - 150, WHITE, font=instruction_font)
    draw_text(screen, "Right and left arrow to move", instructions_x, SCREEN_HEIGHT - 120, WHITE, font=instruction_font)
    draw_text(screen, "R to restart", instructions_x, SCREEN_HEIGHT - 90, WHITE, font=instruction_font)
    draw_text(screen, "Esc to quit", instructions_x, SCREEN_HEIGHT - 60, WHITE, font=instruction_font)
    draw_text(screen, "Golden blocks enlarge platform", instructions_x, SCREEN_HEIGHT - 30, WHITE, font=instruction_font)
