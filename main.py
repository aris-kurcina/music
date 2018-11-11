import pygame
from pygame.locals import *
from sys import exit
import constants

import music
import render
import traceback

ws = pygame.display.set_mode((constants.WSWIDTH, constants.WSHEIGHT),0,32)

def check_events():
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # if event.type == MOUSEBUTTONUP:
            #     mousex, mousey = pygame.mouse.get_pos()
            #     if 30 < mousex < 210 and 30 < mousey < 210:
        #         music.pause_music(ws)

def init():
    pygame.init()
    # music.init()

def run():
    try:
        init()
        render.draw_art(ws)
        render.draw_controls(ws)
        check_events()

    except Exception:
        traceback.print_exc()

run()