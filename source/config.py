import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption("Arkanoid")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
GOLD = (255, 215, 0)
BACKGROUND_COLOR = (30, 30, 30)
OVERLAY_COLOR = (0, 0, 0, 128) 

PADDLE_WIDTH = 150
PADDLE_HEIGHT = 15
BALL_RADIUS = 12
BLOCK_WIDTH = SCREEN_WIDTH // 12
BLOCK_HEIGHT = 40
BONUS_BLOCK_COLOR = (255, 223, 0)

paddle_speed = 12
ball_speed = [7, -7]
lives = 3
score = 0
level = 1
game_over = False  

font = pygame.font.Font(None, 36)
instruction_font = pygame.font.Font(None, 28)
