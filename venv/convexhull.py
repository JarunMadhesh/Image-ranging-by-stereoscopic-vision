
def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i][0] < points[minn][0]:
            minn = i
        elif points[i][0] == points[minn][0]:
            if points[i][1] > points[minn][1]:
                minn = i
    return minn

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convexHull(points, n):
    # There must be at least 3 points
    if n < 3:
        return
    # Find the leftmost point
    l = Left_index(points)
    hull = []
    p = l
    q = 0
    while(True):
        # Add current point to result
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if(orientation(points[p],
                           points[i], points[q]) == 2):
                q = i
        p = q

        # While we don't come to first point
        if(p == l):
            break

    pts = []
    for each in hull:
        pts.append(points[each])

    return pts