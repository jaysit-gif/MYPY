import math

class shape:
    def __init__(self,length=0,breadth=0,a=0,b=0,c=0):
        self.length = length
        self.breadth = breadth
        self.a = a
        self.b = b
        self.c = c

    def rectangle(self):
        area = self.length*self.breadth
        perimeter = (self.length+self.breadth)*2
        return area,perimeter
    
    def circle(self):
        area = self.length*self.length*math.pi
        circumference = self.length*math.pi*2
        return area,circumference
    
    def ellipse(self):
        area = self.length*self.breadth*math.pi
        return area
    
    def triangle(self):
        perimeter = self.a + self.b + self.c
        s = perimeter/2
        area = math.sqrt(s*(s-self.a)*(s - self.b)*(s - self.c))
        return area, perimeter
        
        