from random import randint
import pygame

pygame.init()

FPS = 70
screensize = (1200, 800)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)

pygame.display.update()
clock = pygame.time.Clock()

screensize = (1200, 800)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

element_mass = {'massive': [], 'remove ind': -1}

targets_mass = {'massive': [], 'remove ind': -1}

bombs_massive = {'massive': [], 'remove ind': -1}


class Ball:
    """
    Class of balls (Shells)
    """
    def __init__(self, radius=randint(30, 50), coord_x=0, coord_y=0,
                 velocity_x=int(randint(0, 10)), velocity_y=int(randint(0, 10)),
                 time_of_live=300, color=COLORS[randint(0, 5)]):
        """
        Generates random parameters of Ball (color, coord, velocity)
        Default parameters: gravitation, health, is_alive
        """
        self.color = COLORS[randint(0, 5)]
        self.radius = radius
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.gravitation = 0.2
        self.health = 30
        self.is_alive = True
        self.time_of_live = time_of_live

    def draw_ball(self):
        """
        Draws ball
        """
        pygame.draw.circle(screen, self.color, (self.coord_x, self.coord_y), self.radius)
        self.time_of_live -= 1

    def move_ball(self):
        """
        Moves ball
        """

        self.coord_x += self.velocity_x
        self.coord_y -= self.velocity_y
        self.velocity_y -= self.gravitation

        if self.coord_x > screensize[0] - self.radius or self.coord_x < self.radius:
            self.velocity_x *= -0.95
        if self.coord_y > screensize[1] - 50:
            self.velocity_y *= -0.95
        if abs(self.velocity_y) < 0.001:
            self.velocity_y = 0
        if self.time_of_live == 0:
            self.is_alive = False
        self.draw_ball()
        pygame.draw.circle(screen, BLACK, (self.coord_x, self.coord_y), self.radius, width=2)


class BallTarget(Ball):
    """
    Class of Targets, inheritance from Balls
    """
    def __init__(self, health=30, is_alive=True):
        """
        Generates new Target
        :param health: health points
        :param is_alive: Default (True)
        """
        super().__init__()
        self.health = health
        self.is_alive = is_alive
        self.time_attack = randint(1, 1000)
        self.attack = False
        self.coord_x = randint(100, screensize[0] - 100)
        self.coord_y = randint(50, screensize[1] - 50)

    def move_target(self):
        """
        Moves targets
        """
        self.coord_x += self.velocity_x
        if self.coord_x >= screensize[0] - self.radius or self.coord_x <= self.radius:
            self.velocity_x *= -1

        if self.coord_y >= screensize[1] - self.radius or self.coord_y <= self.radius:
            self.velocity_y *= -1
        if self.time_attack == 0:
            self.attack = True
            self.time_attack = 300
        self.time_attack -= 1
        self.draw_ball()

    def hit_enemy(self, obj, player):
        """
        Updates health points of target and adds points of player, if he hits
        :param player: Player
        :param obj: Aim
        """
        if (self.coord_x - obj.coord_x) ** 2 + (self.coord_y - obj.coord_y) ** 2 <= (self.radius + obj.radius) ** 2:
            self.health -= 100
            player.score += 1
            if self.health <= 0:
                self.is_alive = False