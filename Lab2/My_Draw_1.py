import pygame
import random
from pygame.draw import *

pygame.init()

FPS = 30
screen_size = (600, 800)
screen = pygame.display.set_mode(screen_size)

color_white = [255, 255, 255]
color_black = [0, 0, 0]
color_red = [255, 0, 0]
color_yellow = [255, 255, 0]
color_apple = [220, 20, 60]
color_grass = [0, 128, 0]
color_sky = [0, 0, 128]
color_light_grey_cloud = [150, 150, 150]
color_dark_grew_cloud = [70, 70, 70]
color_spaceship1 = [211, 211, 211]
color_spaceship2 = [170, 170, 170]
color_alien = [0, 255, 127]
# lines(screen, color=[255, 0, 0], closed=True, points=[(100, 100), (200, 200), (200, 100)], width=5)

# Draw Sky and Grass
pygame.draw.polygon(screen, color=color_sky, points=[(0, 0), (0, screen_size[1]/2),
                                                     (screen_size[0], screen_size[1]/2), (screen_size[0], 0)])
pygame.draw.polygon(screen, color=color_grass, points=[(0, screen_size[1]/2),
                                                     (screen_size[0], screen_size[1]/2), screen_size, (0, screen_size[1])])


def draw_circle(color, centr, rad, wid):
    pygame.draw.circle(screen, color, center=centr, radius=rad, width=(wid))

# Draw Moon
moon_coord = (400, 250)
moon_radius = (100)
draw_circle(color_white, moon_coord, moon_radius, 0)


def draw_ellipse(surface, color, coord_rect, wid):
    pygame.draw.ellipse(surface=surface, color=color, rect=coord_rect, width=wid)



# Draw Clouds
dark_cloud_size = (400, 70)
light_cloud_size = (500, 90)
number_of_dark_clouds = 3
number_of_light_clouds = 5

for i in range(number_of_light_clouds):
    coord_cloud = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]//3))
    rect_cloud = (coord_cloud[0], coord_cloud[1], light_cloud_size[0], light_cloud_size[1])
    print(rect_cloud)
    draw_ellipse(screen, color_light_grey_cloud, rect_cloud, 0)
    i += 1
for i in range(number_of_dark_clouds):
    coord_cloud = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]//3))
    rect_cloud = (coord_cloud[0], coord_cloud[1], dark_cloud_size[0], dark_cloud_size[1])
    print(rect_cloud)
    draw_ellipse(screen, color_dark_grew_cloud, rect_cloud, 0)
    i += 1

# SPACESHIP

# Spaceshiplight
Spaceship_position = (150, 300)
Spaceship_surface = pygame.surface.Surface(screen.get_size())
pygame.draw.polygon(Spaceship_surface, color_white, [(Spaceship_position[0] - 100, Spaceship_position[1] + 300),
                                                     Spaceship_position,
                                                     (Spaceship_position[0] + 100, Spaceship_position[1] + 300)])
Spaceship_surface.set_alpha(150)
screen.blit(Spaceship_surface, (0, 0))

# Draw Spaceship Board and Cabin
spaceship_board_coord_and_size = (Spaceship_position[0] - 145, Spaceship_position[1] - 10, 300, 90)
draw_ellipse(screen, color_spaceship2, spaceship_board_coord_and_size, 0)

spaceship_Cabin_coord_and_size = (Spaceship_position[0] - 100, Spaceship_position[1] - 20, 200, 70)
draw_ellipse(screen, color_spaceship1, spaceship_Cabin_coord_and_size, 0)

# SpaceshipWindows
draw_ellipse(screen, color_white, (Spaceship_position[0] - 130, Spaceship_position[1] + 30, 35, 12), 0)
draw_ellipse(screen, color_white, (Spaceship_position[0] - 90, Spaceship_position[1] + 50, 35, 12), 0)
draw_ellipse(screen, color_white, (Spaceship_position[0] - 40, Spaceship_position[1] + 60, 35, 12), 0)
draw_ellipse(screen, color_white, (Spaceship_position[0] + 95, Spaceship_position[1] + 30, 35, 12), 0)
draw_ellipse(screen, color_white, (Spaceship_position[0] + 65, Spaceship_position[1] + 50, 35, 12), 0)
draw_ellipse(screen, color_white, (Spaceship_position[0] + 20, Spaceship_position[1] + 60, 35, 12), 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
