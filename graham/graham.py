from point import Point, turn

def graham(points):
    n = len(points)
    m = 1
    points = sorted(points)
    for i in range(2, n):
        while(turn(points[m-1], points[m], points[i])) <= 0:
            if m > 1:
                m-=1
            elif i == n:
                break
            else:
                i += 1
        m += 1
        points[m], points[i] = points[i], points[m]
    return points[:m+1]
