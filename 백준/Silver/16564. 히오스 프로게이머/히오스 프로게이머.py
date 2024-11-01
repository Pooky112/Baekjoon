import sys

n, k = map(int, sys.stdin.readline().split())
levels = []

for i in range(n):
    levels.append(int(sys.stdin.readline()))

levels.sort()

def can_up(levels, mid, k):
    sum = 0
    for i in range(n):
        if levels[i] < mid:
            sum += mid - levels[i]
    if sum <= k:
        return True
    return False


low = levels[0]
high = levels[-1] + k
result = 0
while low <= high:
    mid = (low + high) // 2
    if can_up(levels, mid, k):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)