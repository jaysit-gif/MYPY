import math as m
import matplotlib.pyplot as plt


class Vectors:
    def __init__(self, mag, arg):  # arg is in degrees
        self.mag = mag
        self.arg = arg
   
    def components(self):
        rad = m.radians(self.arg)
        x = self.mag * m.cos(rad)
        y = self.mag * m.sin(rad)
        return x, y


    def __add__(v1,v2):
        a1 = m.radians(v1.arg)
        a2 = m.radians(v2.arg)

        # how is this implementation
        r1 = v1.mag * m.sin(a1) + v2.mag * m.sin(a2)  
        r2 = v1.mag * m.cos(a1) + v2.mag * m.cos(a2)  
        angle = m.degrees(m.atan2(r1, r2))
        mag = m.sqrt(r1**2+r2**2)
        return Vectors(mag,angle)
    
    def __str__(self):
        return f"Vector(magnitude={self.mag:.2f}, angle={self.arg:.2f}°)"



def ifa(a):
    return f"{'magnitude' if a % 2 == 0 else 'argument'} of v{a//2 + 1}: " #how is this new implementation

v1 = Vectors(6, 30)
v2 = Vectors(3, 60)
z = v1+v2
print(z)

x1, y1 = v1.components()
x2, y2 = v2.components()
x3, y3 = z.components()

# Plotting
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.quiver(0, 0, x3, y3, angles='xy', scale_units='xy', scale=1, color='g', label='v1 + v2')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Vector Addition Visualization")
plt.show()
