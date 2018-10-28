from pygame.locals import *
import pygame
SCALING_FACTOR = 10
OFFSET_Y = 0
OFFSET_X = 0
GX = 25
GY = 10
DARKBLUE = (0,0,255)
LIGHTBLUE = (80,255,255)
DARKGREY = (100,100,100)
LIGHTGREY = (155,155,155)
PURPLE = (150,100,255)
stopped = False
pygame.init()
ws = pygame.display.set_mode((250,250),0,32)


stop = False
TheZombies = ["C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Zombies/The Collection/19 Just Out Of Reach.mp3",
               "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Zombies/The Collection/07 Summertime.mp3",
               "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Zombies/The Collection/18 Whenever You're Ready.mp3",
               "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Zombies/The Collection/13 You Make Me Feel Good.mp3",
               "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Zombies/The Collection/23 Time Of The Season.mp3"]

TheDoors = ["C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/Strange Days/07 People Are Strange.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/The Doors/10 Take It As It Comes.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/The Doors/07 Back Door Man.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/The Doors/03 The Crystal Ship.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/The Doors/02 Soul Kitchen.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/The Doors/01 Break On Through (To The Other Si.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/Strange Days/10 When The Music's Over.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/Strange Days/01 Strange Days.mp3",
            "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Doors/Strange Days/03 Love Me Two Times.mp3"]
TheBeatles = []
TheWho = []
TheSonics = ["C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Sonics/Here Are The Sonics!!!/06 Have Love Will Travel.mp3",
             "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Sonics/Here Are The Sonics!!!/08 Money.mp3",
             "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/The Sonics/Here Are The Sonics!!!/09 Walkin' The Dog.mp3"]
TheMusicMachine = []
blondie = []
Madness = []
TheAnimals =  []
TheMonkees = []
Alphaville = []
Queen = []
def makePlaylist(bands):
    pass
def scale(point):
    
    return { "x": point["x"] * SCALING_FACTOR, "y": point["y"] * SCALING_FACTOR }
def offset(point):
    
    return {"x":point["x"]+OFFSET_X,"y":point["y"]+OFFSET_Y}

def draw_pause(x,y,ws):
    pygame.draw.rect(ws, PURPLE, (x+25,y+10,x+55,y+70))
    pygame.draw.rect(ws, DARKBLUE, (x+25, y+10, x -10, y + 70))
    pygame.draw.rect(ws, DARKBLUE, (x+85, y+10, x -10, y + 70))
def make_point(x,y):
    return {"x":x,"y":y}

def draw_polygon(ws,color,list):
    pygame.draw.polygon(ws, color, list)
def global_offset(list):
    output = list(map(lambda x,y: (x+GX, y+GY)))
    return output
def draw_play(gx,gy,ws):
    p0 = offset(scale(make_point(0,0)))
    p1 = offset(scale(make_point(8,5)))
    p2 = offset(scale(make_point(0,9)))

    draw_polygon(ws,LIGHTBLUE,global_offset((p0,p1,p2)))

clock = pygame.time.Clock()

def pmusic(playlist):
    img = pygame.image.load("C:/Users/Sugar Love/Pictures/music.jpg")
    draw_icon(img)

    #play_music(playlist)

    while True:
        check_events()
        draw_controls()
        draw_play(25, 10, ws)
        pygame.display.flip()






def draw_icon(img):
    pygame.display.set_icon(img)
    #clock.tick(1000)



def play_music(playlist):
    pygame.mixer.init()
    for i in playlist:
        pygame.mixer.music.load(i)
        pygame.mixer.music.play()

def draw_controls(params=None):
    #while pygame.mixer.music.get_busy():
    ws.fill(LIGHTBLUE)
    pygame.draw.circle(ws, LIGHTGREY, (125, 125), 100, 0)
    pygame.draw.circle(ws, PURPLE, (125, 125), 90, 0)

def check_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            if 30 < mousex < 210 and 30 < mousey < 210:
                stopmusic(ws)







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


def stopmusic(ws):
    global stopped
    if not stopped:
        pygame.mixer.music.pause()
        draw_pause(50, 50, ws)

    else:
        pygame.mixer.music.unpause()
        draw_play(50, 50, ws)

    stopped = not stopped


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

try:
    initMixer()
    pmusic(TheZombies)
except Exception:
    print("error")

