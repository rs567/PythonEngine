import numpy as np

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
      
if __name__ == '__main__':
    obj1 = scene_objects()
    obj1.insertObjectList(np.array([[0,-1,3],[1],[255,0,0]])) #OBJ 1
    obj1.insertObjectList(np.array([[2,0,4],[1],[0,0,255]])) #OBJ 2
    obj1.insertObjectList(np.array([[-2,0,4],[1],[0,255,0]])) #OBJ 3

    print(obj1)

    for i in obj1.getList():
        print()