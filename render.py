def make_scale(point):
    return {"x": point["x"] * SCALING_FACTOR, "y": point["y"] * SCALING_FACTOR}

def make_offset(point):
    return {"x": point["x"] + OFFSET_X, "y": point["y"] + OFFSET_Y}

def make_point(x, y):
    return {"x": x, "y": y}

def draw_icon(img):
    pygame.display.set_icon(img)

    #clock.tick(1000)
def draw_polygon(ws, color, plist):
    pygame.draw.polygon(ws, color, plist)

def draw_controls(params=None):
    #while pygame.mixer.music.get_busy():
    #ws.fill(LIGHT_BLUE)
    pygame.draw.circle(ws, LIGHT_GREY, (125, 125), 100, 0)
    pygame.draw.circle(ws, PURPLE, (125, 125), 90, 0)

def global_offset(plist):
    output = lambda x, y: (x + GX, y + GY), plist
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