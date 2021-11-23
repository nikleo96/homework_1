import math

class Point:

    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)


class Segment:

    def __init__(self, a:Point, b:Point) -> None:
        if isinstance(a, Point) and isinstance(b, Point):
            self.__a = a
            self.__b = b
        else:
            print("waiting for points you know...")

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    a = property(get_a, set_a)
    b = property(get_b, set_b)

class Vector:

    def __init__(self, point_start:Point, point_stop:Point) -> None:
        self.x = point_stop.x - point_start.x
        self.y = point_stop.y - point_start.y
    
    def __add__(self, other):
        return Vector(Point(0, 0), Point(self.x + other.x, self.y + other.y))

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"{self.x},{self.y}"


p1 = Point(3, 5)
p2 = Point(-1, 6)

p3 = Point(5, 7)
p4 = Point(-10, 9)

c = Vector(p1, p2)
d = Vector(p3, p4)
print(abs(d))
#print(c+d)