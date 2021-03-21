import pygame
from random import randint
import math
import time

pygame.init()

FPS = 60
screensize = (1200, 800)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x=randint(0, screensize[0]), y=randint(0, screensize[1]),
                 color=COLORS[randint(0, 5)], r=randint(1, 10), vx=randint(-10, 10), vy=randint(-10, 10)):
        """
        :param x: x coordinate
        :param y: y coordinate
        :param color: color
        :param r: radius
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = color



class BallTarget(Ball):
    def __init__(self, health=30):
        super().__init__()
        self.health = health


    def draw_ball(self):
        """
        Draws ball
        :return ball
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move_target(self):
        """
        Moves targets
        :return: motion
        """
        self.x += self.vx
        self.y += self.vy
        if self.x >= screensize[0] - self.r:
            self.vx *= -1
            self.vy = randint(-5, 5)
        if self.x <= self.r:
            self.vx *= -1
            self.vy = randint(-5, 5)
        if self.y >= screensize[1] - self.r:
            self.vy *= -1
            self.vx = randint(-5, 5)
        if self.y <= self.r:
            self.vy *= -1
            self.vx = randint(-5, 5)
        self.draw_ball()

    def hit_test(self, obj):





def game():
    """
    :return:Game
    """
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()
        screen.fill(WHITE)


game()

pygame.quit()
