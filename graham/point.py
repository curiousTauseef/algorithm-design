from math import sqrt, hypot, atan2
import csv

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = atan2(self.y, self.x)
    def __lt__(self, other):
        return self.theta < other.theta
    def __eq__(self, other):
        return self.theta == other.theta
    def translate(self, origin):
        self.x -= origin.x
        self.y -= origin.y
        self.theta = atan2(self.y, self.x)
        
def turn (pointA, pointB, pointC):
    return (pointB.x - pointA.x)*(pointC.y - pointA.y) - (pointB.y - pointA.y)*(pointC.x - pointA.x)

def readPoints(fileName):
    with open(fileName) as file:
        return [Point(float(row[0]), float(row[1])) for row in csv.reader(file)]
