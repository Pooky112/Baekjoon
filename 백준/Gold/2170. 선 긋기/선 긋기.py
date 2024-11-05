import sys

n = int(sys.stdin.readline())
dots = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    dots.append((a, b))

dots.sort()
result = 0
base_x = dots[0][0]
base_y = dots[0][1]
for i in range(1, n):
    x = dots[i][0]
    y = dots[i][1]
    if base_y > x:
        if base_y < y:
            base_y = y
    else:
        result += base_y - base_x
        base_x = x
        base_y = y

result += base_y - base_x
print(result)