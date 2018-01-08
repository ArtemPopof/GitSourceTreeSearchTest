"""Some util classes"""

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_dist_to_point(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def swap(self):
        temp = self.first
        self.first = self.second
        self.second = temp
