import cv2
import numpy as np
import math as m

big_num = 999999 #fake infinity

#### FUNCTION PILE ####
def CanvasToViewport(x,y):
    return(x*canvas.Vw/canvas.Cw, y*canvas.Vh/canvas.Ch, canvas.d)

def IntersectRaySphere(O,D,sphere):
    r = np.array(sphere.radius)
    CO = np.array(O) - np.array(sphere.center)

    a = np.dot(D,D)
    b = 2*np.dot(CO,D)
    c = np.dot(CO,CO) - r*r

    discrim = b*b - 4*a*c
    if discrim < 0:
        return big_num,big_num
    
    t1 = (-b + m.sqrt(discrim))/(2*a)
    t2 = (-b - m.sqrt(discrim))/(2*a)
    
    return t1, t2

def TraceRay(O,D,t_min,t_max):

    closest_t = big_num
    closest_sphere = 0

    for sphere in objList.getList(): 
        t1, t2 = IntersectRaySphere(config.O,D,sphere)

        if t1 in range(t_min, t_max) and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere

        if t2 in range(t_min, t_max) and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere

        if closest_sphere == 0:
            return config.BACKGROUND_COLOR

        return closest_sphere.color
        
    
####################################################

#### CONFIG PILE ####
class config:
    O = np.array([0,0,0]) #Camera Origin
    viewport_size = 1,1 #x:y
    projection_plane_d = 1 #distance from camera
    BACKGROUND_COLOR = np.array([128,128,128])

class canvas: #do calcs here for 

    Cw = config.viewport_size[0] #sus
    Ch = config.viewport_size[1] #sus
    Vw = config.viewport_size[0]
    Vh = config.viewport_size[1]
    d  = config.projection_plane_d

    def __init__(self):
        self.img = np.zeros((100,100,3),dtype=np.uint8)
        
    def putPixel(self,x,y,color):
        self.img[int(x),int(y)] = color

class sphere:
    center = 0
    radius = 0
    color = 0

    def __init__(self,center,radius,color):
        self.center = center
        self.radius = radius
        self.color = color
    
    def __repr__(self):
        megaString = ""
        megaString += "["

        for i in self.center:
            megaString+=str(i)+","

        megaString += "],["
        for i in self.radius:
            megaString+=str(i)+","
            
        megaString += "],["
        for i in self.color:
            megaString+=str(i)+","
            
        megaString += "]"
        
        return megaString
 
class scene_objects:
    objectList = []

    def getList(self):
        return self.objectList

    def insertObjectList(self,center,radius,color):
        sphere1 = sphere(center,radius,color)
        self.objectList.append(sphere1)

    def __str__(self):
        megaString = ""
        for i in self.objectList:
            megaString+=str(i)+"\n"
        return megaString

#Load Objects
objList = scene_objects()
objList.insertObjectList([0,-1,3],[1],[255,0,0]) #OBJ 1
objList.insertObjectList([2,0,4],[1],[0,0,255]) #OBJ 2
objList.insertObjectList([-2,0,4],[1],[0,255,0]) #OBJ 3

canvas_ = canvas()

for i in objList.getList():
    for x in np.arange(-canvas_.Cw/2,canvas_.Cw/2):
        for y in np.arange(-canvas_.Ch/2,canvas_.Ch/2):
            
            D = CanvasToViewport(x,y)
            canvas_.color = TraceRay(config.O,D,1,big_num)
            canvas_.putPixel(x,y,canvas_.color) 

cv2.imwrite('color_img.jpg',canvas_.img)
cv2.imshow('Color image', canvas_.img)
cv2.waitKey(0)
cv2.destroyAllWindows()
