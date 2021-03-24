import pygame
from random import randint
import math
import time

pygame.init()

FPS = 60
screensize = (1200, 800)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)

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
    def __init__(self, username='', score=0, shoots=0):
        self.score = score
        self.username = username
        self.shoots = shoots

    def set_username(self, username):
        self.username = username

    def set_score(self, points):
        self.score += points

    def get_username(self):
        return self.username

    def get_score(self):
        return self.score

    def get_shoots(self):
        return self.shoots

    def set_shoots(self):
        self.shoots += 1


class Ball:
    def __init__(self):
        self.color = COLORS[randint(0, 5)]
        self.radius = randint(30, 50)
        self.coord_x = randint(self.radius, screensize[0] - self.radius)
        self.coord_y = randint(self.radius, screensize[1] - self.radius)
        self.velocity_x = int(randint(-5, 5))
        self.velocity_y = int(randint(-5, 5))
        self.gravitation = 0.1
        self.health = 30
        self.is_alive = True

    def draw_ball(self):
        """
        :return: Draws ball
        """
        pygame.draw.circle(screen, self.color, (self.coord_x, self.coord_y), self.radius)

    def move_ball(self):
        """
        :return: Moves ball
        """
        self.coord_x += self.velocity_x
        self.coord_y -= self.velocity_y
        self.velocity_y -= self.gravitation
        if self.coord_x >= screensize[0] - self.radius or self.coord_x <= self.radius:
            self.velocity_x *= -0.9
            self.health -= 2
        if self.coord_y >= screensize[1] - 50:
            self.velocity_y *= -0.9
            self.health -= 2
        if abs(self.velocity_x) < 0.05:
            self.velocity_x = 0
        if abs(self.velocity_y) < 0.05:
            self.velocity_y = 0
        self.draw_ball()
        if self.health <= 0:
            self.is_alive = False


class BallTarget(Ball):
    def __init__(self, health=30, is_alive=True):
        super().__init__()
        self.health = health
        self.is_alive = is_alive

    def move_target(self):
        """
        Moves targets
        :return: motion
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
        :param obj:Aim
        :return: Result of hit test
        """
        if (self.coord_x - obj.coord_x) ** 2 + (self.coord_y - obj.coord_y) ** 2 <= (self.radius + obj.radius) ** 2:
            self.health -= 100

            player.shoots += 1
            player.score += 1
            if self.health <= 0:
                self.is_alive = False

        # return self.is_alive


class Gun:
    def __init__(self, x=40, y=500, color=BLACK, length=70, angle=0, shoot_mode=False, power=0):
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.shoot_mode = shoot_mode
        self.power = power
        self.maxlength = length*1.5

    def fire2_start(self):
        self.shoot_mode = True

    def fire2_end(self):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball()
        new_ball.radius = 10

        x0, y0 = pygame.mouse.get_pos()
        print(x0, y0)
        if x0 == self.x:
            pass
        else:
            self.angle = -math.atan((y0 - self.y) / (x0 - self.x))
        new_ball.velocity_x = self.power * math.cos(self.angle)
        new_ball.velocity_y = self.power * math.sin(self.angle)

        new_ball.coord_x = self.x + self.length * math.cos(self.angle)
        new_ball.coord_y = self.y - self.length * math.sin(self.angle)
        element_mass['massive'].append(new_ball)
        self.power = 0
        self.length /= 1.5
        self.color = BLACK
        self.shoot_mode = False
        self.draw_gan()

    def draw_gan(self):
        pygame.draw.line(screen, self.color, (self.x, self.y),
                         (self.x + self.length * math.cos(self.angle), self.y - self.length * math.sin(self.angle)), width=7)

    def targeting(self):
        x0, y0 = pygame.mouse.get_pos()
        print(x0, y0)
        if x0 == self.x:
            pass
        else:
            self.angle = -math.atan((y0 - self.y) / (x0 - self.x))
        if self.shoot_mode:
            self.color = RED
            if self.length >= self.maxlength:
                pass
            else:
                self.length += 1
        else:
            self.color = BLACK

        self.draw_gan()

    def power_up(self):
        if self.shoot_mode:
            if self.power < 100:
                self.power += 0.5
            self.color = RED
            self.draw_gan()
        else:
            self.color = BLACK
        self.draw_gan()


pygame.display.update()
clock = pygame.time.Clock()



def game():
    """
    :return:Game
    """
    def new_massive(mass, ind):
        new_mass = []
        for i in range(len(mass) - 1):
            if i < ind:
                new_mass[i] = mass[i]
            if i > ind:
                new_mass[i - 1] = mass[i]
        return new_mass

    def generate_targets(number_of_targets):
        for i in range(number_of_targets):
            targets_mass['massive'].append(BallTarget())

    generate_targets(5)
    counter = 10

    new_gun = Gun()
    finished = False
    finished_session = False
    while not finished:
        new_player = Player()
        clock.tick(FPS)
        myfont = pygame.font.SysFont('Times New Roman', 30)
        scoretext = myfont.render((str(new_player.score)), True, BLACK)
        screen.blit(scoretext, (screensize[0] // 8, 30))
        if finished_session:
            myfont2 = pygame.font.SysFont('Times New Roman', 30)
            finish_session_text = myfont2.render(("Вы уничтожили все цели за:" + str(new_player.get_shoots())),
                                                 True, BLACK)
            screen.blit(finish_session_text, (screensize[0] // 2, screensize[1] // 2))
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter < -2:
                        finished_session = False
                if event.type == pygame.QUIT:
                    finished = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_gun.fire2_start()
            elif event.type == pygame.MOUSEBUTTONUP:
                new_gun.fire2_end()
                new_player.set_shoots()
        new_gun.targeting()
        new_gun.power_up()

        targets_mass['remove ind'] = -1
        element_mass['remove ind'] = -1

        for i in range(len(targets_mass['massive'])):
            targets_mass['massive'][i].move_target()
            for j in range(len(element_mass['massive'])):
                element_mass['massive'][j].move_ball()
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
            finished_session = True

        pygame.display.update()
        screen.fill(WHITE)


game()

pygame.quit()
