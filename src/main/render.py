import constants
import pygame

def make_scale(point):
    return {"x": point["x"] * constants.SCALING_FACTOR, "y": point["y"] * constants.SCALING_FACTOR}

def make_offset(point):
    return {"x": point["x"] + constants.OFFSET_X, "y": point["y"] + constants.OFFSET_Y}

def make_point(x, y):
    return {"x": x, "y": y}

def draw_icon(img):
    pygame.display.set_icon(img)

def draw_polygon(ws, color, plist):
    pygame.draw.polygon(ws, color, plist)

def draw_circle(ws, color, poffset, radius, width=0):
    pygame.draw.circle(ws, color, poffset, radius, width)

def draw_controls(ws):
    draw_shape(constants.GX,constants.GY,ws,constants.SHAPE_PLAY)

def draw_art(ws):
    ws.fill(constants.LIGHT_BLUE)
    draw_circle(ws, constants.LIGHT_GREY, (int(constants.WSWIDTH / 2), int(constants.WSHEIGHT / 2)), 100)
    draw_circle(ws, constants.PURPLE, (int(constants.WSWIDTH/2), int(constants.WSHEIGHT/2)), 90)

def global_offset(plist):
    output = list(map(lambda x, y: (x + constants.GX, y + constants.GY), plist))
    return output

def add_points(pa,pb):
    return {"x":pa["x"] + pb["x"], "y":pa["y"]+pb["y"]}

def make_global_point(gx, gy, vertex):
    gpoint = make_point(gx, gy)
    lpoint = make_point(vertex[0], vertex[1])
    scale = make_scale(lpoint)
    offset = make_offset(scale)
    return add_points(gpoint, offset)

def draw_points(gx, gy, vertices):
    result = []
    for vertex in vertices:
        p = make_global_point(gx, gy, vertex)
        result.append((vertex[0],vertex[1]))
    return result

def draw_shape(gx, gy, ws, shape):
    color = shape["color"]
    for vertices in shape["shape"]:

        plist = draw_points(gx, gy, vertices)
        draw_polygon(ws, color, plist)


