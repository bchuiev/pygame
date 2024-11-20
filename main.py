import pygame
from random import uniform as func
from time import sleep

WIDTH, HEIGHT = 800, 600
BOUND = 10
RADIUS = 10
VELOCITY = 8
PADDLE_HEIGHT = 10
PADDLE_WIDTH = 80
PADDLE_SPEED = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

x, y = WIDTH // 2, HEIGHT // 2
vx = VELOCITY * func(-1, 1)
vy = VELOCITY * func(-1, 1)

xp = (WIDTH - PADDLE_WIDTH) // 2
yp = HEIGHT - PADDLE_HEIGHT - BOUND

border_l = BOUND + RADIUS
border_r = WIDTH - BOUND - RADIUS
border_u = BOUND + RADIUS
border_d = HEIGHT - BOUND - RADIUS

score = 0

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

def draw_window():
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (BOUND, BOUND, WIDTH - 2 * BOUND, HEIGHT - 2 * BOUND), 2)
    pygame.draw.circle(win, GREEN, (int(x), int(y)), RADIUS)
    pygame.draw.rect(win, WHITE, (xp, yp, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()

def draw_score():
    win.fill(BLACK)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = f"Your score: {score}"
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 100, HEIGHT // 3))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and xp > border_l:
        xp -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and xp < border_r - PADDLE_WIDTH:
        xp += PADDLE_SPEED

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy
    if y + vy > yp - RADIUS:
        if xp <= x + vx <= xp + PADDLE_WIDTH:
            vy = -vy
            score += 1
            vx *= 1.5
            vy *= 1.5
        else:
            draw_score()
            sleep(3)
            run = False

    x += vx
    y += vy

    draw_window()

pygame.quit()
