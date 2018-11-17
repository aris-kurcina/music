import pygame

import songs
import constants
import render

stopped = False
clock = pygame.time.Clock()

def makePlaylist(bands):
    pass

def preload(playlist):
    img = pygame.image.load("C:/Users/Sugar Love/Pictures/music.jpg")
    render.draw_icon(img)
    play_music(playlist)

    # while True:
    #     render.draw_controls(ws)
    #     pygame.display.flip()

def play_music(playlist):
    pygame.mixer.init()

    for i in playlist:
        pygame.mixer.music.load(i)
        pygame.mixer.music.play()

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
        render.draw_shape(50, 50, ws, constants.SHAPE_PAUSE)

    else:
        pygame.mixer.music.unpause()
        render.draw_shape(50, 50, ws, constants.SHAPE_PLAY)

    stopped = not stopped

def init():
    freq, size, chan = pygame.mixer.get_init()
    pygame.mixer.init(freq, size, chan, constants.BUFFER)
    preload(songs.TheZombies)
