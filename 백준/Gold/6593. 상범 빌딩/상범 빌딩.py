from collections import deque


def bfs(building, start, end, L, R, C):
    #동, 서, 남, 북, 위, 아래
    directions = [(0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]
    queue = deque([start])
    visited = set([start])
    minutes = 0

    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            if (x, y, z) == end:
                return minutes
            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and building[nz][nx][ny] != '#' and (nx, ny, nz) not in visited:
                    queue.append((nx, ny, nz))
                    visited.add((nx, ny, nz))
        minutes += 1
    return -1


def main():
    while True:
        L, R, C = map(int, input().split())

        if L == 0 and R == 0 and C == 0:
            break

        building = []
        start = end = None

        for l in range(L):
            floor = []
            for r in range(R):
                line = input()
                floor.append(line)
                if 'S' in line:
                    start = (r, line.index('S'), l)
                if 'E' in line:
                    end = (r, line.index('E'), l)

            building.append(floor)
            if l < L:
                input().strip()

        result = bfs(building, start, end, L, R, C)
        if result == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {result} minute(s).")


main()