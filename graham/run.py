from graham import graham
from point import readPoints

points = readPoints('../data/points.csv')
for point in graham(points):
    print(point.x, point.y)
