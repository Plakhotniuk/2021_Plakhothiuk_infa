import pygame

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

color_black = [0, 0, 0]
color_red = [255, 0, 0]
color_yellow = [255, 255, 0]
# здесь будут рисоваться фигуры1
# ...
def draw_circle(color, centr, rad, wid):
    pygame.draw.circle(screen, color, center=centr, radius=rad, width=(wid))


pygame.draw.polygon(screen, [100, 100, 100], [(0, 0), (0, screen_size[1]),screen_size, (screen_size[0], 0) ])


face_centr = (200, 200)
face_rad = 120
face_wid1 = 0
face_wid2 = 3


draw_circle(color_yellow, face_centr, face_rad, face_wid1)

draw_circle(color_black, face_centr, face_rad, face_wid2)


eye_centr1 = [150, 160]
eye_centr2 = [250, 160]
eye_rad1 = 20
eye_rad2 = 15
eye_rad3 = 7
eye_wid1 = 0
eye_wid2 = 2

draw_circle(color_red, eye_centr1, eye_rad1, eye_wid1)
draw_circle(color_black, eye_centr1, eye_rad1, eye_wid2)
draw_circle(color_red, eye_centr2, eye_rad2, eye_wid1)
draw_circle(color_black, eye_centr2, eye_rad2, eye_wid2)
draw_circle(color_black, eye_centr1, eye_rad3, eye_wid1)
draw_circle(color_black, eye_centr2, eye_rad3, eye_wid1)

h = 20
mouth_location = 250
brov1 = []

pygame.draw.polygon(screen, color_black, [(eye_centr1[0], mouth_location+h), (eye_centr2[0], mouth_location+h), (eye_centr2[0], mouth_location), (eye_centr1[0], mouth_location)])


pygame.draw.line(screen, color_black, [98, 110], [190, 150], 15)
pygame.draw.line(screen, color_black, [300, 110], [208, 160], 10)
# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

