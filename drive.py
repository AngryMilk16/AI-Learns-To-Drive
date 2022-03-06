import pygame
import random

pygame.init()

back_colour = (255, 255, 255)
wall_colour = (0, 0, 0)
start_colour = (0, 255, 0)
Win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Drive")
Win.fill(back_colour)
pygame.display.update()

def map():

    pygame.draw.line(Win, wall_colour, (75, 75), (175, 75), 4)
    pygame.draw.line(Win, wall_colour, (175, 75), (175, 550), 4)
    pygame.draw.line(Win, wall_colour, (75, 75), (75, 600), 4)
    pygame.draw.line(Win, wall_colour, (75, 600), (175, 700), 5)
    pygame.draw.line(Win, wall_colour, (175, 700), (300, 700), 4)
    pygame.draw.line(Win, wall_colour, (175, 550), (250, 625), 5)
    pygame.draw.line(Win, wall_colour, (250, 625), (275, 625), 4)
    pygame.draw.line(Win, wall_colour, (275, 625), (300, 600), 5)
    pygame.draw.line(Win, wall_colour, (300, 700), (400, 600), 5)
    pygame.draw.line(Win, wall_colour, (400, 600), (400, 400), 4)
    pygame.draw.line(Win, wall_colour, (400, 400), (450, 350), 5)
    pygame.draw.line(Win, wall_colour, (300, 600), (300, 350), 4)
    pygame.draw.line(Win, wall_colour, (300, 350), (400, 250), 5)
    pygame.draw.line(Win, wall_colour, (400, 250), (550, 250), 4)
    pygame.draw.line(Win, wall_colour, (450, 350), (500, 350), 4)
    pygame.draw.line(Win, wall_colour, (500, 350), (550, 400), 5)
    pygame.draw.line(Win, wall_colour, (550, 400), (550, 600), 4)
    pygame.draw.line(Win, wall_colour, (550, 250), (650, 350), 5)
    pygame.draw.line(Win, wall_colour, (650, 350), (650, 600), 4)
    pygame.draw.line(Win, wall_colour, (650, 600), (700, 650), 5)
    pygame.draw.line(Win, wall_colour, (550, 600), (675, 725), 5)
    pygame.draw.line(Win, wall_colour, (675, 725), (800, 725), 4)
    pygame.draw.line(Win, wall_colour, (800, 725), (900, 650), 5)
    pygame.draw.line(Win, wall_colour, (900, 650), (900, 200), 4)
    pygame.draw.line(Win, wall_colour, (900, 200), (800, 75), 5)
    pygame.draw.line(Win, wall_colour, (800, 75), (400, 75), 4)
    pygame.draw.line(Win, wall_colour, (700, 650), (750, 650), 4)
    pygame.draw.line(Win, wall_colour, (750, 650), (800, 615), 5)
    pygame.draw.line(Win, wall_colour, (800, 615), (800, 250), 4)
    pygame.draw.line(Win, wall_colour, (800, 250), (750, 175), 5)
    pygame.draw.line(Win, wall_colour, (750, 175), (400, 175), 4)

    pygame.display.update()


class Car:

    def cars():
        pass

def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        map()

    pygame.quit()
            
if __name__ == "__main__":
    main()
