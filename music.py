import pygame
from pygame.locals import *


SCALING_FACTOR = 10
OFFSET_Y = 0
OFFSET_X = 0
BUFFER = 3072
GX = 25
GY = 10
LIGHT_BLUE = (80,255,255)
DARKBLUE = (0,0,255)
DARKGREY = (100,100,100)
LIGHT_GREY = (155,155,155)
PURPLE = (150,100,255)
RED = (255,0,0)
SHAPE_PLAY = {"color":PURPLE,"shape":[[(0,0),(8,5),(0,9)]]}
SHAPE_STOP = {"color":LIGHT_GREY,"shape":[[(0,0),(0,9),(9,9),(9,0)]]}
SHAPE_PAUSE = {"color":LIGHT_BLUE,"shape":[[(0,0),(0,3),(3,9),(3,0)],[(6,0),(6,3),(9,9),(9,0)]]}

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
Madness = ["C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Madness/Madness/12 Madness (Is All In The Mind).mp3",
           "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Madness/Madness/06 House Of Fun.mp3",
           "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Madness/Madness/03 It Must Be Love.mp3",
           "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Madness/Madness/01 Our House.mp3",
           "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Madness/Madness/09 Blue Skinned Beast.mp3"]
TheAnimals = []
TheMonkees = []
Alphaville = ["C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Alphaville/Forever Young/06 Forever Young.mp3",
              "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Alphaville/Forever Young/02 Summer In Berlin.mp3",
              "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Alphaville/Forever Young/08 Sounds Like A Melody.mp3",
              "C:/Users/Sugar Love/Music/iTunes/iTunes Media/Music/Alphaville/Forever Young/05 Fallen Angel.mp3"]
Queen = []
def makePlaylist(bands):
    pass
def make_scale(point):
    
    return {"x": point["x"] * SCALING_FACTOR, "y": point["y"] * SCALING_FACTOR }
def make_offset(point):
    
    return {"x":point["x"]+OFFSET_X,"y":point["y"]+OFFSET_Y}


def make_point(x,y):
    return {"x":x,"y":y}

def draw_polygon(ws,color,plist):
    pygame.draw.polygon(ws, color, plist)
def global_offset(plist):
    output = lambda x,y: (x+GX, y+GY),plist
    return output

def add_points(pa,pb):
    return {"x":pa["x"]+pb["x"],"y":pa["y"]+pb["y"]}
def make_global_point(gx,gy,points):
    gpoint = make_point(gx,gy)
    lpoint = make_point(points[0],points[1])
    scale = make_scale(lpoint)
    offset = make_offset(scale)
    return add_points(gpoint,offset)

def draw_points(gx,gy,points):
    result = []
    for point in points:
        p = make_global_point(gx,gy,point)
        result.append(p)
    return result
def draw_shape(gx,gy,ws,shape):
    color = shape["color"]
    for points in shape["shape"]:
        draw_polygon(ws, color, draw_points(gx, gy, points))   

    

clock = pygame.time.Clock()

def pmusic(playlist):
    img = pygame.image.load("C:/Users/Sugar Love/Pictures/music.jpg")
    draw_icon(img)

    play_music(playlist)

    while True:
        check_events()
        draw_controls()
        pause_music(ws)
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
    #ws.fill(LIGHT_BLUE)
    pygame.draw.circle(ws, LIGHT_GREY, (125, 125), 100, 0)
    pygame.draw.circle(ws, PURPLE, (125, 125), 90, 0)

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
    pmusic(TheZombies)
except Exception:
    print("error")