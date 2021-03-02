import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screensize = (1200, 900)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
while not finished:
    clock.tick(FPS)
    myfont = pygame.font.SysFont(None, 40)
    scoretext = myfont.render("Score = " + str(score), True, (255, 0, 0))
    screen.blit(scoretext, (screensize[0]//2, 10))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click(event)
            x0, y0 = pygame.mouse.get_pos()
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
                score += 1

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()