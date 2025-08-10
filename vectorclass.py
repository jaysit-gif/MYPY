import math as m

class Vectors:
    def __init__(self, *args):
        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            # Case: magnitude and angle
            self.mag, self.arg = args
            rad = m.radians(self.arg)
            self.i = self.mag * m.cos(rad)
            self.j = self.mag * m.sin(rad)
            self.k = 0

        elif len(args) == 1 and isinstance(args[0], list) and len(args[0]) == 3:
            # Case: component list [i, j, k]
            self.i, self.j, self.k = args[0]
            self.mag = m.sqrt(self.i**2 + self.j**2 + self.k**2)
            self.arg = m.degrees(m.atan2(self.j, self.i)) if self.mag != 0 else None

        else:
            raise ValueError("Use either (mag, angle) or ([i, j, k])")

    def __str__(self):
        angle_str = f"{self.arg:.2f}°" if self.arg is not None else "undefined"
        return f"Vector: ⟨{self.i:.2f}, {self.j:.2f}, {self.k:.2f}⟩ | Magnitude: {self.mag:.2f} | Angle: {angle_str}"
    

v1 = Vectors(4,30)
print(v1)
v2 = Vectors([2,3,4])
print(v2)    