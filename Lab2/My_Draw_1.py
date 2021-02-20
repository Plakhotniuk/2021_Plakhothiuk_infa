import pygame
import random
from pygame.draw import *

pygame.init()

FPS = 30
screen_size = (700, 800)
screen = pygame.display.set_mode(screen_size)

color_white = [255, 255, 255]
color_black = [0, 0, 0]
color_red = [255, 0, 0]
color_yellow = [255, 255, 0]
color_apple = [220, 20, 60]
color_grass = [0, 128, 0]
color_sky = [0, 0, 128]
color_light_grey_cloud = [150, 150, 150]
color_dark_gray_cloud = [70, 70, 70]
color_spaceship1 = [211, 211, 211]
color_spaceship2 = [170, 170, 170]
color_alien = [0, 255, 127]

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


def draw_ellipse(Surface, color, coord_rect, wid):
    pygame.draw.ellipse(surface=Surface, color=color, rect=coord_rect, width=wid)


# Draw Clouds

def Clouds(number_of_clouds, color, size):
    for i in range(number_of_clouds):
        coord_cloud = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]//3))
        rect_cloud = (coord_cloud[0], coord_cloud[1], size[0], size[1])
        draw_ellipse(screen, color, rect_cloud, 0)
        i += 1

Clouds(3, color_dark_gray_cloud, (400, 70))
Clouds(5 , color_light_grey_cloud, (500, 90))


# Alien
def alien_body_ellipse(location, Color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize, wid, coef):
    Alien_surface = pygame.Surface([500, 500], pygame.SRCALPHA)
    pygame.draw.ellipse(Alien_surface, Color, (alien_bodypart_xcoord*coef, alien_bodypart_ycoord*coef,
                                                     asize*coef, bsize*coef), wid)
    surface_rot = pygame.transform.rotate(Alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)
def alien_body_arc(location, Color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize, startang, endang, wid, coef):
    Alien_surface = pygame.Surface([300, 300], pygame.SRCALPHA)
    pygame.draw.arc(Alien_surface, Color, (alien_bodypart_xcoord*coef, alien_bodypart_ycoord*coef,
                                                     asize*coef, bsize*coef), startang, endang, wid)
    surface_rot = pygame.transform.rotate(Alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)
def Alien(Alien_location, coef):

    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)
    # Main Body
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0], Alien_body_location[1], 0, 65, 125, 0, coef)
    # Left arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, Alien_body_location[1], 0, 35, 35, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 45, Alien_body_location[1], 0, 35, 35, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 33, (Alien_body_location[1] + 20), 0, 27, 17, 0, coef)
    # Right arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 45, (Alien_body_location[1] + 35), 0, 15, 20, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 20), 0, 27, 20, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 95, Alien_body_location[1] + 35, 0, 30, 17, 0, coef)
    # Left Leg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 0, (Alien_body_location[1] + 100), 0, 25, 40, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, (Alien_body_location[1] + 130), 0, 20, 50, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 25, (Alien_body_location[1] + 170), 0, 25, 25, 0, coef)
    # Rightleg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 50, (Alien_body_location[1] + 100), 0, 25, 40, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 65, (Alien_body_location[1] + 130), 0, 20, 50, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 170), 0, 25, 25, 0, coef)
    # Head
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 5), (Alien_body_location[1] - 60), 0, 60, 60, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 25), (Alien_body_location[1] - 80), 0, 60, 60, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 20), (Alien_body_location[1] - 80), 0, 60, 60, 0, coef)
    # alien_body_ellipse((Alien_location[0] - 20, Alien_location[1] - 130), color_alien, Alien_body_location[0], Alien_body_location[1], 60, 85, 35)
    # alien_body_ellipse((Alien_location[0] - 70, Alien_location[1] - 160), color_alien, Alien_body_location[0], Alien_body_location[1], 120, 85, 35)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, Alien_body_location[1] - 85, 0, 85, 35, 0, coef)
    # Eyes
    # Left
    alien_body_ellipse(Alien_location, color_black, Alien_body_location[0], (Alien_body_location[1] - 65), 0, 25, 25, 0, coef)
    alien_body_ellipse(Alien_location, color_white, (Alien_body_location[0] + 13), (Alien_body_location[1] - 54), 0, 8, 8, 0, coef)
    # Right
    alien_body_ellipse(Alien_location, color_black, (Alien_body_location[0] + 40), (Alien_body_location[1] - 64), 0, 22, 22, 0, coef)
    alien_body_ellipse(Alien_location, color_white, (Alien_body_location[0] + 50), (Alien_body_location[1] - 55), 0, 8, 8, 0, coef)
    # Ears
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 20), (Alien_body_location[1] - 105), 0, 15, 35, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 30), (Alien_body_location[1] - 120), 0, 25, 25, 0, coef)

    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 60), (Alien_body_location[1] - 105), 0, 15, 35, 0, coef)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 60), (Alien_body_location[1] - 120), 0, 25, 25, 0, coef)
    # Apple
    alien_body_ellipse(Alien_location, color_apple, (Alien_body_location[0] + 110), Alien_body_location[1], 0, 45, 45, 0, coef)
    pi = 3.14
    alien_body_arc(Alien_location, color_black, Alien_body_location[0] + 130, Alien_body_location[1] - 20, 0, 40, 50, pi/2, pi, 2, coef)
    alien_body_ellipse(Alien_location, (0, 200, 0), Alien_body_location[0] + 118, Alien_body_location[1] - 20, 0, 20, 10, 0, coef)
    alien_body_ellipse(Alien_location, color_black, Alien_body_location[0] + 118, Alien_body_location[1] - 20, 0, 20, 10, 1, coef)


Alien((150, 350), 0.3)

# SPACESHIPS (Location, similarity coef)
def Spaceship(location, coef):
    # Spaceshiplight
    Spaceship_location = [0,0]
    Spaceship_location[0] = location[0]/coef
    Spaceship_location[1] = location[1] / coef
    Spaceship_surface = pygame.surface.Surface(screen.get_size())
    pygame.draw.polygon(Spaceship_surface, color_white, [((Spaceship_location[0] - 100)*coef, (Spaceship_location[1] + 300)*coef),
                                                         (Spaceship_location[0]*coef, Spaceship_location[1]*coef),
                                                         ((Spaceship_location[0] + 100)*coef, (Spaceship_location[1] + 300)*coef)])
    Spaceship_surface.set_alpha(150)
    screen.blit(Spaceship_surface, (0, 0))

    # Draw Spaceship Board and Cabin
    spaceship_board_coord_and_size = ((Spaceship_location[0] - 145)*coef, (Spaceship_location[1] - 10)*coef, 300*coef, 90*coef)
    draw_ellipse(screen, color_spaceship2, spaceship_board_coord_and_size, 0)

    spaceship_Cabin_coord_and_size = ((Spaceship_location[0] - 100)*coef, (Spaceship_location[1] - 20)*coef, 200*coef, 70*coef)
    draw_ellipse(screen, color_spaceship1, spaceship_Cabin_coord_and_size, 0)

    # SpaceshipWindows
    draw_ellipse(screen, color_white, ((Spaceship_location[0] - 130)*coef, (Spaceship_location[1] + 30)*coef, 35*coef, 12*coef), 0)
    draw_ellipse(screen, color_white, ((Spaceship_location[0] - 90)*coef, (Spaceship_location[1] + 50)*coef, 35*coef, 12*coef), 0)
    draw_ellipse(screen, color_white, ((Spaceship_location[0] - 40)*coef, (Spaceship_location[1] + 60)*coef, 35*coef, 12*coef), 0)
    draw_ellipse(screen, color_white, ((Spaceship_location[0] + 95)*coef, (Spaceship_location[1] + 30)*coef, 35*coef, 12*coef), 0)
    draw_ellipse(screen, color_white, ((Spaceship_location[0] + 65)*coef, (Spaceship_location[1] + 50)*coef, 35*coef, 12*coef), 0)
    draw_ellipse(screen, color_white, ((Spaceship_location[0] + 20)*coef, (Spaceship_location[1] + 60)*coef, 35*coef, 12*coef), 0)


Spaceship((550, 300), 0.5)
Spaceship((150, 250), 1)
Spaceship((370, 320), 0.3)



Alien((300, 350), 1)
Alien((100, 450), 0.8)
Alien((70, 420), 0.3)
Alien((200, 420), 0.4)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
