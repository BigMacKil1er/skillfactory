from math import pi
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.height * self.width

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return pi * self.r**2