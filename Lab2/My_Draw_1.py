import pygame
import random

pygame.init()

FPS = 30
screen_size = (700, 800)
screen = pygame.display.set_mode(screen_size)

color_white = [255, 255, 255]

color_white_a = [255, 255, 255, 100]
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
pygame.draw.polygon(screen, color=color_sky, points=[(0, 0), (0, screen_size[1] / 2),
                                                     (screen_size[0], screen_size[1] / 2), (screen_size[0], 0)])
pygame.draw.polygon(screen, color=color_grass, points=[(0, screen_size[1] / 2),
                                                       (screen_size[0], screen_size[1] / 2), screen_size,
                                                       (0, screen_size[1])])


# Draw Moon
moon_coord = (400, 250)
moon_radius = 100
pygame.draw.circle(screen, color_white, moon_coord, moon_radius, 0)


# Draw Clouds

def clouds(number_of_clouds, color, size):
    '''
    :param number_of_clouds: no comments
    :param color: color of clouds
    :param size: (a, b)
    :return:
    '''
    for i in range(number_of_clouds):
        coord_cloud = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1] // 3))
        rect_cloud = (coord_cloud[0], coord_cloud[1], size[0], size[1])
        pygame.draw.ellipse(screen, color, rect_cloud, 0)
        i += 1


# Alien
def alien_body_ellipse(location, color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize, wid,
                       coef):
    '''
    :param location: position of alien
    :param color: color of body
    :param alien_bodypart_xcoord: x coordinate of body
    :param alien_bodypart_ycoord: y coordinate of body
    :param bodypart_angle: rotation of alien part
    :param asize: a size
    :param bsize: b size
    :param wid: width of line (0 to fill)
    :param coef: coefficient of size
    :return: draws a part of allien
    '''
    alien_surface = pygame.Surface([500, 500], pygame.SRCALPHA)
    pygame.draw.ellipse(alien_surface, color, (alien_bodypart_xcoord * coef, alien_bodypart_ycoord * coef,
                                               asize * coef, bsize * coef), wid)
    surface_rot = pygame.transform.rotate(alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)


def alien_body_arc(location, color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize,
                   startang, endang, wid, coef):
    '''
    :param location: position of alien
    :param color: color of alien
    :param alien_bodypart_xcoord: x coordinate
    :param alien_bodypart_ycoord: y coordinate
    :param bodypart_angle: rotation of alien part
    :param asize: a size
    :param bsize: b size
    :param startang: start angle to draw an apple branch
    :param endang: end angle to draw an apple branch
    :param wid: width of line (0 to fill)
    :param coef: coefficient of size
    :return: draw a branch of apple
    '''
    alien_surface = pygame.Surface([300, 300], pygame.SRCALPHA)
    pygame.draw.arc(alien_surface, color, (alien_bodypart_xcoord * coef, alien_bodypart_ycoord * coef,
                                           asize * coef, bsize * coef), startang, endang, wid)
    surface_rot = pygame.transform.rotate(alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)


def alien(alien_location, coef):
    '''
    :param alien_location: position of alien
    :param coef: coefficient of size
    :return: draw an alien
    '''
    alien_body_location = (alien_location[0] // 2, alien_location[1] // 2)
    # Main Body
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0], alien_body_location[1], 0, 65, 125, 0, coef)
    # Left arm
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 10, alien_body_location[1], 0, 35, 35, 0,
                       coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 45, alien_body_location[1], 0, 35, 35, 0,
                       coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 33, (alien_body_location[1] + 20), 0, 27,
                       17, 0, coef)
    # Right arm
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 45, (alien_body_location[1] + 35), 0, 15,
                       20, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 75, (alien_body_location[1] + 20), 0, 27,
                       20, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 95, alien_body_location[1] + 35, 0, 30, 17,
                       0, coef)
    # Left Leg
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 0, (alien_body_location[1] + 100), 0, 25,
                       40, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 10, (alien_body_location[1] + 130), 0, 20,
                       50, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 25, (alien_body_location[1] + 170), 0, 25,
                       25, 0, coef)
    # Right leg
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 50, (alien_body_location[1] + 100), 0, 25,
                       40, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 65, (alien_body_location[1] + 130), 0, 20,
                       50, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] + 75, (alien_body_location[1] + 170), 0, 25,
                       25, 0, coef)
    # Head
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] + 5), (alien_body_location[1] - 60), 0, 60,
                       60, 0, coef)
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] + 25), (alien_body_location[1] - 80), 0, 60,
                       60, 0, coef)
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] - 20), (alien_body_location[1] - 80), 0, 60,
                       60, 0, coef)
    alien_body_ellipse(alien_location, color_alien, alien_body_location[0] - 10, alien_body_location[1] - 85, 0, 85, 35,
                       0, coef)
    # Eyes
    # Left
    alien_body_ellipse(alien_location, color_black, alien_body_location[0], (alien_body_location[1] - 65), 0, 25, 25, 0,
                       coef)
    alien_body_ellipse(alien_location, color_white, (alien_body_location[0] + 13), (alien_body_location[1] - 54), 0, 8,
                       8, 0, coef)
    # Right
    alien_body_ellipse(alien_location, color_black, (alien_body_location[0] + 40), (alien_body_location[1] - 64), 0, 22,
                       22, 0, coef)
    alien_body_ellipse(alien_location, color_white, (alien_body_location[0] + 50), (alien_body_location[1] - 55), 0, 8,
                       8, 0, coef)
    # Ears
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] - 20), (alien_body_location[1] - 105), 0,
                       15, 35, 0, coef)
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] - 30), (alien_body_location[1] - 120), 0,
                       25, 25, 0, coef)

    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] + 60), (alien_body_location[1] - 105), 0,
                       15, 35, 0, coef)
    alien_body_ellipse(alien_location, color_alien, (alien_body_location[0] + 60), (alien_body_location[1] - 120), 0,
                       25, 25, 0, coef)
    # Apple
    alien_body_ellipse(alien_location, color_apple, (alien_body_location[0] + 110), alien_body_location[1], 0, 45, 45,
                       0, coef)
    pi = 3.14
    alien_body_arc(alien_location, color_black, alien_body_location[0] + 130, alien_body_location[1] - 20, 0, 40, 50,
                   pi / 2, pi, 2, coef)
    alien_body_ellipse(alien_location, (0, 200, 0), alien_body_location[0] + 118, alien_body_location[1] - 20, 0, 20,
                       10, 0, coef)
    alien_body_ellipse(alien_location, color_black, alien_body_location[0] + 118, alien_body_location[1] - 20, 0, 20,
                       10, 1, coef)


# SPACESHIPS (Location, similarity coef)
def spaceship(location, coef):
    '''
    :param location: location of a spaceship
    :param coef: coefficient of size
    :return: draw a spaceship
    '''
    # Spaceshiplight
    spaceship_location = [0, 0]
    spaceship_location[0] = location[0] / coef
    spaceship_location[1] = location[1] / coef
    spaceship_surface = pygame.surface.Surface(screen.get_size(), pygame.SRCALPHA)
    pygame.draw.polygon(spaceship_surface, color_white_a,
                        [((spaceship_location[0] - 100) * coef, (spaceship_location[1] + 300) * coef),
                         (spaceship_location[0] * coef, spaceship_location[1] * coef),
                         ((spaceship_location[0] + 100) * coef, (spaceship_location[1] + 300) * coef)])
    screen.blit(spaceship_surface, (0, 0))

    # Draw Spaceship Board and Cabin
    spaceship_board_coord_and_size = (
        (spaceship_location[0] - 145) * coef, (spaceship_location[1] - 10) * coef, 300 * coef, 90 * coef)
    pygame.draw.ellipse(screen, color_spaceship2, spaceship_board_coord_and_size, 0)

    spaceship_cabin_coord_and_size = (
        (spaceship_location[0] - 100) * coef, (spaceship_location[1] - 20) * coef, 200 * coef, 70 * coef)
    pygame.draw.ellipse(screen, color_spaceship1, spaceship_cabin_coord_and_size, 0)

    # SpaceshipWindows
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] - 130) * coef, (spaceship_location[1] + 30) * coef, 35 * coef, 12 * coef), 0)
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] - 90) * coef, (spaceship_location[1] + 50) * coef, 35 * coef, 12 * coef), 0)
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] - 40) * coef, (spaceship_location[1] + 60) * coef, 35 * coef, 12 * coef), 0)
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] + 95) * coef, (spaceship_location[1] + 30) * coef, 35 * coef, 12 * coef), 0)
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] + 65) * coef, (spaceship_location[1] + 50) * coef, 35 * coef, 12 * coef), 0)
    pygame.draw.ellipse(screen, color_white,
                 ((spaceship_location[0] + 20) * coef, (spaceship_location[1] + 60) * coef, 35 * coef, 12 * coef), 0)


spaceships = [[550, 300], [150, 250], [370, 320]]
clouds(3, color_dark_gray_cloud, (400, 70))
clouds(5, color_light_grey_cloud, (500, 90))

alien((150, 350), 0.3)

spaceship(spaceships[0], 0.5)
spaceship(spaceships[1], 1)
spaceship(spaceships[2], 0.3)

alien((300, 350), 1)
alien((100, 450), 0.8)
alien((70, 420), 0.3)
alien((200, 420), 0.4)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
