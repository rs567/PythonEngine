
import cv2
import numpy as np
import math as m

#### FUNCTION PILE ####
def CanvasToViewport(x,y):
    return(x*canvas.Vw/canvas.Cw, y*canvas.Vh/canvas.Ch, canvas.d)

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

    for sphere in scene_objects:
        t1, t2 = IntersectRaySphere(config.O,config.D,sphere)

        if t1 in range(t_min, t_max) and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere

        if t2 in range(t_min, t_max) and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere

        if closest_sphere == 0:
            return config.BACKGROUND_COLOR

        return closest_sphere.color

#### CONFIG PILE ####

class config:
    O = (0,0,0) #Camera Origin
    viewport_size = 1,1 #x:y
    projection_plane_d = 1 #distance from camera
    BACKGROUND_COLOR = [128,128,128]

class canvas: #do calcs here for 
    #config.viewport

    Cw = config.viewport_size[0] #sus
    Ch = config.viewport_size[1] #sus
    Vw = config.viewport_size[0]
    Vh = config.viewport_size[1]
    d  = config.projection_plane_d

    def __init__(self):
        self.img = np.zeros([self.Vw,self.Vh,3]) #init image array with 3 color channels RGB
        
    def putPixel(self,x,y,color):
        self.img[x,y] = color

class sphere:
    center = 0
    radius = 0
    color = 0

    def __init__(self,center,radius,color):
        self.center = center
        self.radius = radius
        self.color = color

    
class scene_objects:
    objectList = []

    def insertObjectList(center,radius,color):
        sphere1 = sphere(center,radius,color)
    
        
#    def sphere_1():
#        center = (0,-1,3)
#        radius = 1
#        color = (255,0,0) 
#    def sphere_2():
#        center = (2,0,4)
#        radius = 1
#        color = (0,0,255)
#    def sphere_3():
#        center = (-2,0,4)
#        radius = 1
#        color (0,255,0)


#### Calling code to render image ###

for obj in scene_objects:
    #handle the different objects in scene o
    for x in range(-canvas.Cw/2,canvas.Cw/2):
        for y in range(-canvas.Ch/2,canvas.Ch/2):
            D = CanvasToViewport(x,y)
            color = TraceRay(config.O,config.D,1,np.Infinity)
            canvas.putPixel(x,y,color) ##Write this to hook into OpenCV


            #i forgor


