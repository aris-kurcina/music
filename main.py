from pygame.locals import *
from constants import *
from songs import *
import pygame
import render

stopped = False
pygame.init()
stop = False
ws = pygame.display.set_mode((250,250),0,32)

clock = pygame.time.Clock()

def makePlaylist(bands):
    pass

def preload(playlist):
    img = pygame.image.load("C:/Users/Sugar Love/Pictures/music.jpg")
    draw_icon(img)
    play_music(playlist)

    while True:
        check_events()
        draw_controls()
        pause_music(ws)
        pygame.display.flip()

def play_music(playlist):
    pygame.mixer.init()

    for i in playlist:
        pygame.mixer.music.load(i)
        pygame.mixer.music.play()

def check_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            if 30 < mousex < 210 and 30 < mousey < 210:
                pause_music(ws)

def analyze_song(song):
    slist = song.split("/")
    sitem = slist[9]
    s = sitem.split(".")
    s2 = s[0]
    s3 = s2.split(" ")
    song_name = s3[1]

    del s
    del s2
    del s3
    del slist
    del sitem

    ###########################
    blist = song.split("/")
    band_name = blist[7]
    del blist
    ###########################

    print("playing %s by %s" % (song_name,band_name))

def pause_music(ws):
    global stopped
    if not stopped:
        pygame.mixer.music.pause()
        draw_shape(50, 50, ws,SHAPE_PAUSE)

    else:
        pygame.mixer.music.unpause()
        draw_shape(50, 50, ws,SHAPE_PLAY)

    stopped = not stopped

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    freq, size, chan = getmixerargs()
    pygame.mixer.init(freq, size, chan, BUFFER)

try:
    initMixer()
    preload(TheZombies)

except Exception:
    print("error")