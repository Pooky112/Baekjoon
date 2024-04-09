import sys
from collections import deque


def solution(N, K):
    least_move = float('inf')
    visited = [0] * 100001

    queue = deque([(N, 0)])
    least_move, possible_moves = 100000, 0

    while queue:
        val, move = queue.popleft()
        visited[val] = 1

        if val == K and move <= least_move:
            least_move = min(least_move, move)
            possible_moves += 1
        if move > least_move:
            break

        for next_move in (val - 1, val + 1, val * 2):
            if next_move in range(100001) and not visited[next_move]:
                queue.append((next_move, move + 1))

    return least_move, possible_moves


N, K = map(int, sys.stdin.readline().split())
a, b = solution(N, K)
print(a)
print(b)