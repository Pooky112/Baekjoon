import sys

def solution(N, M, graph):
    directions = [(1, -1), (1, 0), (1, 1)]
    min_fuel = float('inf')

    def find_min_fuel(i, j, cur_dir, min_fuel, fuel):
        if i == N-1:
            return min(min_fuel, fuel)
        for direction in directions:
            dx, dy = direction
            if cur_dir != dy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    min_fuel = find_min_fuel(nx, ny, dy, min_fuel, fuel+graph[nx][ny])
        return min_fuel

    for j in range(M):
        min_fuel = min(min_fuel, find_min_fuel(0, j, 2, min_fuel, graph[0][j]))

    return min_fuel


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(N, M, graph))
