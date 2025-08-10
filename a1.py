from a import shape as s

def fout(shape,area=0,perimeter=0):
    if shape == "ellipse":
        print(f"area of the {shape} is {area}")
    else:
        print(f"area of the {shape} is {area},perimeter of the {shape} is {perimeter}")    

y = input("ENTER THE SHAPE: ").lower()
if y=="circle":
    x = float(input("RADIUS: "))
    a = s(x)
    area , perimeter = s.circle(a)
    fout("circle",area,perimeter)
elif y == "rectangle":
    x = float(input("LENGTH: "))
    y = float(input("BREADTH: "))
    a = s(x,y)
    area ,perimeter=s.rectangle(a)
    fout("rectangle",area,perimeter)       
elif y == "ellipse":
    x = float(input("MAJOR AXIS: "))
    y = float(input("MINOR AXIS: "))
    a = s(x,y)
    area =s.ellipse(a)
    fout("ellipse",area)
elif y == "triangle":
    x = float(input("side1: "))
    y = float(input("side2: "))
    z = float(input("side3: "))
    a = s(0,0,x,y,z)
    area , perimeter = s.triangle(a)
    fout("triangle",area,perimeter)
    


