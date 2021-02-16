import pygame, sys

screen = pygame.display.set_mode((1024, 640))

running = True

#let's create a surface to hold our ellipse:
surface = pygame.Surface((320, 240))

red = (180, 50, 50)
size = (0, 0, 300, 200)

#drawing an ellipse onto the
ellipse = pygame.draw.ellipse(surface, red, size)

#new surface variable for clarity (could use our existing though)
#we use the pygame.transform module to rotate the original surface by 45°
surface2 = pygame.transform.rotate(surface, 45)

while running:
    screen.fill((255, 250, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(surface2, (100, 100))
    pygame.display.update()