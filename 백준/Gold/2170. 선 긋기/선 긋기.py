import sys

def calcaluate_total_length(dots):
    dots.sort()

    total_length = 0

    base_x = dots[0][0]
    base_y = dots[0][1]

    for i in range(1, len(dots)):
        x, y = dots[i]
        if base_y > x:
            base_y = max(base_y, y)
        else:
            total_length += base_y - base_x
            base_x = x
            base_y = y

    total_length += base_y - base_x

    return total_length


n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(calcaluate_total_length(dots))