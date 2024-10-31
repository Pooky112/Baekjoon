import sys

n, c = map(int, sys.stdin.readline().split())
house = []

for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

def can_place(house, distance, c):
    count = 1
    last_position = house[0]
    for i in range(1, len(house)):
        if house[i] - last_position >= distance:
            count += 1
            last_position = house[i]
            if count == c:
                return True
    return False

low = 1
high = house[-1] - house[0]
max_distance = 0
while low <= high:
    mid = (low + high) // 2
    if can_place(house, mid, c):
        max_distance = max(max_distance, mid)
        low = mid + 1
    else:
        high = mid - 1

print(max_distance)
