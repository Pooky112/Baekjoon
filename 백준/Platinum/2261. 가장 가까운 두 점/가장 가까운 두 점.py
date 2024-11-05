import sys

def distance(dot1, dot2):
    return (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2

def closest_pair(dots):
    if len(dots) <= 3:
        min_dist = float('inf')
        for i in range(len(dots)):
            for j in range(i + 1, len(dots)):
                min_dist = min(min_dist, distance(dots[i], dots[j]))
        return min_dist

    mid = len(dots) // 2
    left_dots = dots[:mid]
    right_dots = dots[mid:]

    min_dist = min(closest_pair(left_dots), closest_pair(right_dots))

    mid_x = dots[mid][0]
    strip = [dot for dot in dots if abs(dot[0] - mid_x) ** 2 < min_dist]
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))

    return min_dist



n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dots.sort()

print(closest_pair(dots))


