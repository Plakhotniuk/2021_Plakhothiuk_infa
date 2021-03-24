import pygame
from random import randint
import math

pygame.init()

FPS = 70
screensize = (1200, 800)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)

pygame.display.update()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

element_mass = {'massive': [], 'remove ind': -1}

targets_mass = {'massive': [], 'remove ind': -1}


class Player:

    def __init__(self, username='', score=0, shots=0):
        """
        Some information about player (Score, Username, number of shots)
        :param username:
        :param score:
        :param shots:
        """
        self.score = score
        self.username = username
        self.shots = shots


class Ball:
    """
    Class of balls (Shells)
    """
    def __init__(self):
        """
        Generates random parameters of Ball (color, coord, velocity)
        Default parameters: gravitation, health, is_alive
        """
        self.color = COLORS[randint(0, 5)]
        self.radius = randint(30, 50)
        self.coord_x = randint(self.radius, screensize[0] - self.radius)
        self.coord_y = randint(self.radius, screensize[1] - self.radius)
        self.velocity_x = int(randint(-5, 5))
        self.velocity_y = int(randint(-5, 5))
        self.gravitation = 0.2
        self.health = 30
        self.is_alive = True
        self.time_of_live = 300

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

    def move_target(self):
        """
        Moves targets
        """
        self.coord_x += self.velocity_x
        self.coord_y += self.velocity_y
        if self.coord_x >= screensize[0] - self.radius or self.coord_x <= self.radius:
            self.velocity_x *= -1
            self.velocity_y = randint(-5, 5)
        if self.coord_y >= screensize[1] - self.radius or self.coord_y <= self.radius:
            self.velocity_y *= -1
            self.velocity_x = randint(-5, 5)
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


class Gun:
    """
    Class of Cannon
    """
    def __init__(self, x=400, y=500, color=BLACK, length=70, angle=0, shooting_mode=False, power=0):
        """
        :param x: coordinate x
        :param y: coordinate y
        :param color: color
        :param length: gun barrel length
        :param angle: angle with the horizon
        :param shooting_mode:
        :param power:
        """
        self.x = x
        self.y = y
        self.velocity_x = 2
        self.velocity_y = 2
        self.color = color
        self.body_color = BLACK
        self.length = length
        self.angle = angle
        self.shooting_mode = shooting_mode
        self.power = power
        self.maxlength = length*1.5

    def fire2_start(self):
        """
        Starts shooting mode
        """
        self.shooting_mode = True

    def fire2_end(self):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball()
        new_ball.radius = 15

        x0, y0 = pygame.mouse.get_pos()

        if x0 == self.x:
            pass
        else:
           self.angle = -math.atan((y0 - self.y) / (x0 - self.x))
        new_ball.velocity_x = self.power * math.cos(self.angle) * 0.5
        new_ball.velocity_y = self.power * math.sin(self.angle) * 0.5
        new_ball.coord_x = self.x + self.length * math.cos(self.angle)
        new_ball.coord_y = self.y - self.length * math.sin(self.angle)
        if self.x > x0:
            new_ball.velocity_y *= -1
            new_ball.velocity_x *= -1
            new_ball.coord_x = self.x - self.length * math.cos(self.angle)
            new_ball.coord_y = self.y + self.length * math.sin(self.angle)

        element_mass['massive'].append(new_ball)
        self.power = 0
        self.length = 70
        self.color = BLACK
        self.shooting_mode = False

    def draw_gun(self):
        """
        Draws Gun
        """
        x0, y0 = pygame.mouse.get_pos()
        if x0 < self.x:
            pygame.draw.line(screen, self.color, (self.x, self.y),
                             (self.x - self.length * math.cos(self.angle),
                              self.y + self.length * math.sin(self.angle)), width=7)
        else:
            pygame.draw.line(screen, self.color, (self.x, self.y),
                             (self.x + self.length * math.cos(self.angle),
                              self.y - self.length * math.sin(self.angle)), width=7)
        pygame.draw.rect(screen, self.body_color, (self.x - 45, self.y + 10, 90, 40))
        pygame.draw.circle(screen, self.body_color, (self.x, self.y), 20)


    def targeting(self):
        """
        Process of targeting (depends on mouse position)
        """
        x0, y0 = pygame.mouse.get_pos()
        if x0 == self.x:
            pass
        else:
            self.angle = -math.atan((y0 - self.y) / (x0 - self.x))
        if self.shooting_mode:
            self.color = RED
            if self.length >= self.maxlength:
                pass
            else:
                self.length += 1
        else:
            self.color = BLACK

        self.draw_gun()

    def power_up(self):
        """
        Gains power of shot
        """
        if self.shooting_mode:
            if self.power < 100:
                self.power += 0.5
            self.color = RED

        else:
            self.color = BLACK


def generate_targets(number_of_targets):
    """
    Generation of targets, put them in massive
    :param number_of_targets:set number of targets
    """
    for i in range(number_of_targets):
        targets_mass['massive'].append(BallTarget())


finished = False


def game():
    """
    Game session process
    """
    global finished
    generate_targets(2)
    counter = 0
    new_gun = Gun()
    finished_session = False
    see_results = False
    new_player = Player()
    element_mass['massive'].clear()

    while not finished_session:

        clock.tick(FPS)
        if not see_results:
            myfont = pygame.font.SysFont('Times New Roman', 30)
            scoretext = myfont.render((str(new_player.shots)), True, BLACK)
            screen.blit(scoretext, (screensize[0] // 8, 30))
        if see_results:
            myfont2 = pygame.font.SysFont('Times New Roman', 30)
            finish_session_text = myfont2.render(("Вы уничтожили все цели за: " + str(new_player.shots) + " выстрелов"),
                                                 True, BLACK)
            screen.blit(finish_session_text, (screensize[0] // 3.5, screensize[1] // 3))
            counter += 1
            if counter == 150:
                finished_session = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True
                finished_session = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_gun.fire2_start()
            elif event.type == pygame.MOUSEBUTTONUP:
                new_gun.fire2_end()
                if not see_results:
                    new_player.shots += 1

        new_gun.targeting()
        new_gun.power_up()

        targets_mass['remove ind'] = -1
        element_mass['remove ind'] = -1
        for i in range(len(targets_mass['massive'])):
            targets_mass['massive'][i].move_target()
        for j in range(len(element_mass['massive'])):
            element_mass['massive'][j].move_ball()
        for i in range(len(targets_mass['massive'])):
            for j in range(len(element_mass['massive'])):
                if not element_mass['massive'][j].is_alive:
                    element_mass['remove ind'] = j
                if not targets_mass['massive'][i].is_alive:
                    targets_mass['remove ind'] = i
                targets_mass['massive'][i].hit_enemy(element_mass['massive'][j], new_player)

        if targets_mass['remove ind'] == -1:
            pass
        else:
            targets_mass['massive'].remove(targets_mass['massive'][targets_mass['remove ind']])

        if element_mass['remove ind'] == -1:
            pass
        else:
            element_mass['massive'].remove(element_mass['massive'][element_mass['remove ind']])

        if not targets_mass['massive']:
            see_results = True

        pygame.display.update()
        screen.fill(WHITE)


while not finished:
    game()

pygame.quit()
