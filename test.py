import pygame
from pygame.locals import *
from sys import exit
import constants

ws = pygame.display.set_mode((constants.WSWIDTH, constants.WSHEIGHT))

def draw_stuff(x, y, width, height, ws, color):
    points = []
    points.append((x, y - ((2 / 3.0) * height)))  # top of 1st story, upper left
    points.append((x, y))  # lower left corner
    points.append((x + width, y))  # lower right corner

    lineThickness = 2
    pygame.draw.lines(ws, color, False, points, lineThickness)

def init():
    pygame.init()

def render():
    ws.fill(constants.WHITE)
    draw_stuff(100, 200, 120, 150, ws, constants.RED)

def check_events():
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

def run():
    init()
    render()
    check_events()

run()
