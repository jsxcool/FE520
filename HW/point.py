import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

p = Point(1.0,2.0)
print("(1,2) distance is: ", p.distance())
