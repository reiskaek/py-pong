import pygame

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 1280, 768
BALL_SPEED_X = 4
BALL_SPEED_Y = 4
PADDLE_SPEED = 6

# Colors
WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle setup
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player1 = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 35, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
BALL_SIZE = 15
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 50)
about_font = pygame.font.Font(None, 25)

# Game loop
running = True
while running:
    pygame.time.delay(16)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.y < HEIGHT - PADDLE_HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.y > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.y < HEIGHT - PADDLE_HEIGHT:
        player2.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx *= -1

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dx = BALL_SPEED_X
        ball_dy = BALL_SPEED_Y

    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dx = -BALL_SPEED_X
        ball_dy = -BALL_SPEED_Y

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player1)
    pygame.draw.rect(screen, RED, player2)
    pygame.draw.ellipse(screen, GREEN, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    score_text = font.render(f"{score1}  {score2}", True, YELLOW)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))

    about_text1 = about_font.render(f"reis", True, WHITE)
    screen.blit(about_text1, (1203,750))

    about_text2 = about_font.render(f"kaek", True, YELLOW)
    screen.blit(about_text2, (1235,750))

    game_text = about_font.render(f"py-pong", True, WHITE)
    screen.blit(game_text, (5,750))

    pygame.display.flip()

pygame.quit()
