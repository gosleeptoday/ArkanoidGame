import pygame
from config import *
from game_objects import create_blocks, reset_ball, draw_text, draw_blocks, show_game_over_overlay, show_instructions

def main():
    global lives, score, level, game_over
    
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 100, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
    blocks = create_blocks()
    running = True
    clock = pygame.time.Clock()

    reset_ball(ball, ball_speed)

    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        lives = 3
                        score = 0
                        level = 1
                        blocks = create_blocks()
                        reset_ball(ball, ball_speed)
                        game_over = False
                    if event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    if event.key == pygame.K_ESCAPE:
                        running = False  

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle.left > 0:
                paddle.x -= paddle_speed
            if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
                paddle.x += paddle_speed

            ball.x += ball_speed[0]
            ball.y += ball_speed[1]

            if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
                ball_speed[0] = -ball_speed[0]
            if ball.top <= 0:
                ball_speed[1] = -ball_speed[1]
            if ball.bottom >= SCREEN_HEIGHT:
                lives -= 1
                reset_ball(ball, ball_speed)

            if ball.colliderect(paddle):
                ball_speed[1] = -ball_speed[1]

            for block, color in blocks[:]:
                if ball.colliderect(block):
                    ball_speed[1] = -ball_speed[1]
                    blocks.remove((block, color))
                    score += 10
                    if color == BONUS_BLOCK_COLOR:
                        paddle.width += 50

            if lives == 0:
                game_over = True

            if len(blocks) == 0:
                level += 1
                blocks = create_blocks()
                reset_ball(ball, ball_speed)

        pygame.draw.rect(screen, LIGHT_BLUE, paddle, border_radius=10)
        pygame.draw.circle(screen, RED, (ball.x, ball.y), BALL_RADIUS)
        draw_blocks(screen, blocks)
        show_instructions(screen)

        draw_text(screen, f"Lives: {lives}", 10, SCREEN_HEIGHT - 120, color=WHITE)
        draw_text(screen, f"Score: {score}", 10, SCREEN_HEIGHT - 90, color=WHITE)
        draw_text(screen, f"Level: {level}", 10, SCREEN_HEIGHT - 60, color=WHITE)

        if game_over:
            show_game_over_overlay(screen, score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
