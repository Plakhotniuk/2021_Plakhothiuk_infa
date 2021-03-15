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

score = {'score': 0, 'color': COLORS[randint(0, 5)], 'Username': '', 'Complexity': ''}

complexity_coef = 1


def new_ball():
    """
    Создает кружок
    :return: возвращает кружок с его рандомными параметрами
    """
    ball_code = 1
    ball_radius = randint(30, 50) // complexity_coef
    ball_color = COLORS[randint(0, 5)]
    ball_coord_x = randint(ball_radius, screensize[0] - ball_radius)
    ball_coord_y = randint(ball_radius, screensize[1] - ball_radius)
    ball_velocity_x = int(randint(-5, 5) * complexity_coef)
    ball_velocity_y = int(randint(-5, 5) * complexity_coef)
    ball_element = {"code": ball_code, "color": ball_color, "radius": ball_radius, "x": ball_coord_x,
                    "y": ball_coord_y, "velocity_x": ball_velocity_x, "velocity_y": ball_velocity_y}
    return ball_element


def new_square():
    """
    Создает квадратик
    :return: возвращает квадратик с его рандомными параметрами
    """
    square_code = 2
    square_side = randint(30, 50) // complexity_coef
    square_color = COLORS[randint(0, 5)]
    square_coord_x = randint(square_side // 2, screensize[0] - square_side // 2)
    square_coord_y = randint(square_side // 2, screensize[1] - square_side // 2)
    square_velocity_x = (randint(-5, 5) * complexity_coef)
    square_velocity_y = (randint(-5, 5) * complexity_coef)
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


massive_of_gamers = []


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
enter_name = False
choose_complexity = False


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
            if screensize[0] // 2 <= elem['x'] <= screensize[0] // 2 + 3:
                elem['velocity_y'] = randint(-5, 5)
                elem['velocity_x'] = randint(-5, 5)
            if screensize[1] // 2 <= elem['y'] <= screensize[1] // 2 + 3:
                elem['velocity_y'] = randint(-5, 5)
                elem['velocity_x'] = randint(-5, 5)
            if elem['x'] >= screensize[0] - elem['radius'] // 2:
                elem['velocity_x'] *= -1
                elem['velocity_y'] = randint(-5, 5)
            if elem['x'] <= elem['radius'] // 2:
                elem['velocity_x'] *= -1
                elem['velocity_y'] = randint(-5, 5)
            if elem['y'] >= screensize[1] - elem['radius'] // 2:
                elem['velocity_y'] *= -1
                elem['velocity_x'] = randint(-5, 5)
            if elem['y'] <= elem['radius'] // 2:
                elem['velocity_y'] *= -1
                elem['velocity_x'] = randint(-5, 5)
            draw_square(elem['color'], elem['x'], elem['y'], elem['radius'])


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
            if abs(elem['x'] - x0) <= elem['radius'] // 2 and \
                    abs(elem['y'] - y0) <= elem['radius'] // 2:
                if randint(1, 2) == 1:
                    element_mass[i] = new_ball()
                else:
                    element_mass[i] = new_square()
                score['score'] += 3
                score['color'] = elem['color']
        i += 1


while not finished:
    clock.tick(FPS)
    if not enter_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score['Username'] = score['Username'].replace("\n", "")
                    enter_name = True
                if event.key == pygame.K_BACKSPACE:
                    score['Username'] = score['Username'][:-1]
                elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                    score['Username'] += event.unicode

        start_screen = pygame.font.SysFont('Times New Roman', 40)
        start_text = start_screen.render(("Write your name to start the game: " + score['Username']), True,
                                         score['color'])
        screen.blit(start_text, (screensize[0] // 5, screensize[1] // 4))
        pygame.display.flip()

    elif enter_name == True and choose_complexity == False:
        start_screen = pygame.font.SysFont('Times New Roman', 30)
        start_text = start_screen.render("Choose complexity: 1 - Normal 2 - Hard  3 - Impossible", True,
                                         score['color'])
        screen.blit(start_text, (screensize[0] // 8, screensize[1] // 4))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    complexity_coef += 1
                    score['Complexity'] = 'Normal'
                    choose_complexity = True
                elif event.key == pygame.K_2:
                    complexity_coef += 1.5
                    score['Complexity'] = 'Hard'
                    choose_complexity = True
                elif event.key == pygame.K_3:
                    complexity_coef += 3
                    score['Complexity'] = 'Impossible'
                    choose_complexity = True
        pygame.display.flip()

    elif enter_name == True and choose_complexity == True:
        myfont = pygame.font.SysFont('Times New Roman', 30)
        scoretext = myfont.render(("Chosen complexity: " + score['Complexity'] +
                                   "   |   " + score['Username'] + "'s score = " +
                                   str(score['score'])), True, score['color'])
        screen.blit(scoretext, (screensize[0] // 8, 30))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                gotcha()

        move_element(element_mass)

    pygame.display.update()

    screen.fill(BLACK)

pygame.quit()


def leaders():
    """
    :return: Добавление результатов игровой сессии в файл
    """

    print('Your result: ' + '\n' + score['Username'] + ' ' + score['Complexity'] + ' ' + str(score['score']))
    filename = 'Data'
    with open(filename, 'a+') as file:
        file.write(score['Username'] + ' ' + score['Complexity'] + ' ' + str(score['score']) + '\n')


leaders()
