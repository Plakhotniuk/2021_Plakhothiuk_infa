import pygame
from random import randint

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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    Создает кружок
    :return: возвращает кружок с его рандомными параметрами
    """
    ball_code = 1
    ball_radius = randint(30, 50)
    ball_color = COLORS[randint(0, 5)]
    ball_coord_x = randint(ball_radius, screensize[0] - ball_radius)
    ball_coord_y = randint(ball_radius, screensize[1] - ball_radius)
    ball_velocity_x = randint(-5, 5)
    ball_velocity_y = randint(-5, 5)
    ball_element = {"code": ball_code,"color": ball_color, "radius": ball_radius, "x": ball_coord_x,
                    "y": ball_coord_y, "velocity_x": ball_velocity_x, "velocity_y": ball_velocity_y}
    return ball_element


def new_square():
    """
    Создает квадратик
    :return: возвращает квадратик с его рандомными параметрами
    """
    square_code = 2
    square_side = randint(30, 50)
    square_color = COLORS[randint(0, 5)]
    square_coord_x = randint(square_side // 2, screensize[0] - square_side // 2)
    square_coord_y = randint(square_side // 2, screensize[1] - square_side // 2)
    square_velocity_x = randint(-5, 5)
    square_velocity_y = randint(-5, 5)
    square_element = {"code": square_code, "color": square_color, "radius": square_side, "x": square_coord_x,
                      "y": square_coord_y, "velocity_x": square_velocity_x, "velocity_y": square_velocity_y}
    return square_element


def draw_square(color, x, y, side):
    """
    Рисует квадратик
    :param color: цвет квадратика
    :param x: координата центра
    :param y: координата центра
    :param side: размер боковой стороны
    :return: квадратик
    """
    pygame.draw.rect(screen, color, (x - side//2, y - side//2, side, side))


def draw_ball(color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)


element_mass = []


def random_generate_elements(count):
    """
    :param count: количество фигурок
    :return: рандомное распределение количества фигурок и вызов функций,
    рисующих их
    """
    balls = randint(0, count)

    for j in range(count):
        if j >= balls:
            element_mass.append((new_square()))
        else:
            element_mass.append(new_ball())


random_generate_elements(5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = {'score': 0, 'color': COLORS[randint(0, 5)]}

while not finished:
    clock.tick(FPS)
    myfont = pygame.font.SysFont(None, 40)
    scoretext = myfont.render("Score = " + str(score['score']), True, score['color'])
    screen.blit(scoretext, (screensize[0] // 2, 30))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            def gotcha():
                """
                Прибавляет различное количество очков при попадании в кружок и квадратик
                """
                x0, y0 = pygame.mouse.get_pos()
                i = 0
                for elem in element_mass:
                    if elem['code'] == 1:
                        if (elem['x'] - x0) ** 2 + (elem['y'] - y0) ** 2 <= elem['radius'] ** 2:
                            if randint(1, 2) == 1:
                                element_mass[i] = new_ball()
                            else:
                                element_mass[i] = new_square()
                            score['score'] += 1
                            score['color'] = elem['color']
                    elif elem['code'] == 2:
                        if abs(elem['x'] - x0) <= elem['radius'] // 2 and abs(elem['y'] - y0) <= elem['radius'] // 2:
                            if randint(1, 2) == 1:
                                element_mass[i] = new_ball()
                            else:
                                element_mass[i] = new_square()
                            score['score'] += 3
                            score['color'] = elem['color']
                    i += 1

            gotcha()

    def move_element(mass):
        """
        Двигает фигурки
        :param mass: массив фигурок
        :return:
        """
        for elem in mass:
            if elem['code'] == 1:
                elem['x'] += elem['velocity_x']
                elem['y'] += elem['velocity_y']

                if elem['x'] >= screensize[0] - elem['radius']:
                    elem['velocity_x'] *= -1
                    elem['velocity_y'] = randint(-5, 5)
                if elem['x'] <= elem['radius']:
                    elem['velocity_x'] *= -1
                    elem['velocity_y'] = randint(-5, 5)
                if elem['y'] >= screensize[1] - elem['radius']:
                    elem['velocity_y'] *= -1
                    elem['velocity_x'] = randint(-5, 5)
                if elem['y'] <= elem['radius']:
                    elem['velocity_y'] *= -1
                    elem['velocity_x'] = randint(-5, 5)
                draw_ball(elem['color'], elem['x'], elem['y'], elem['radius'])
            elif elem['code'] == 2:
                elem['x'] += elem['velocity_x']
                elem['y'] += elem['velocity_y']
                if elem['x'] >= screensize[0] // 2 and elem['x'] <= screensize[0] // 2 + 10:
                    elem['velocity_y'] = randint(-5, 5)
                    elem['velocity_x'] = randint(-5, 5)
                if elem['y'] >= screensize[0] // 2 and elem['y'] <= screensize[1] // 2 + 10:
                    elem['velocity_y'] = randint(-5, 5)
                    elem['velocity_x'] = randint(-5, 5)
                if elem['x'] >= screensize[0] - elem['radius']//2:
                    elem['velocity_x'] *= -1
                    elem['velocity_y'] = randint(-5, 5)
                if elem['x'] <= elem['radius']//2:
                    elem['velocity_x'] *= -1
                    elem['velocity_y'] = randint(-5, 5)
                if elem['y'] >= screensize[1] - elem['radius']//2:
                    elem['velocity_y'] *= -1
                    elem['velocity_x'] = randint(-5, 5)
                if elem['y'] <= elem['radius']//2:
                    elem['velocity_y'] *= -1
                    elem['velocity_x'] = randint(-5, 5)
                draw_square(elem['color'], elem['x'], elem['y'], elem['radius'])


    move_element(element_mass)

    pygame.display.update()

    screen.fill(BLACK)

pygame.quit()
