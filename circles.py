from platform import mac_ver
import numpy as np
import math as m

Cw = 100
Ch = 100
Vw = 100
Vh = 100
d = 100

O = (0,0,0)
class values:
    viewport_size = 1
    projection_plane_d = 1    
class scene_objects:
    sphere1 =[
        center = (0,-1,3),
        radius = 1,
        color = (255,0,0)
        ]

    center = (2,0,4)
    radius = 1
    color = (0,0,255)

    center(-2,0,4)
    radius = 1
    color (0,255,0)


def CanvasToViewport(x,y):
    return(x*Vw/Cw, y*Vh/Ch, d)

def IntersectRaySphere(O,D,sphere):
    r = sphere.radius
    CO = O - sphere.center

    a = np.dot(D,D)
    b = 2*np.dot(CO,D)
    c = np.dot(CO,CO) - r*r

    discrim = b*b - 4*a*c
    if discrim < 0:
        return np.Infinity,np.Infinity
    
    t1 = (-b + m.sqrt(discrim))/(2*a)
    t2 = (-b - m.sqrt(discrim))/(2*a)
    
    return t1, t2

def TraceRay(O,D,t_min,t_max):
    closest_t = np.Infinity
    closest_sphere = 0

    for sphere in scene.spheres:
        t1, t2 = IntersectRaySphere(O,D,sphere)

        if t1 in range(t_min, t_max) and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere

        if t2 in range(t_min, t_max) and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere

        if closest_sphere == 0:
            return values.BACKGROUND_COLOR

        return closest_sphere.color


for x in range(-Cw/2,Cw/2):
    for y in range(-Ch/2,Ch/2):
        D = CanvasToViewport(x,y)
        color = TraceRay(0,D,1,np.Infinity)
        canvas.Putpixel(x,y,color) ##Write this to hook into OpenCV

