import sys
import heapq


def solution(N, T, P, K):
    answer = 0
    sum_tasks = 0
    pq = []

    for i in range(N):
        tasks = K[i]
        sum_tasks += tasks

        heapq.heappush(pq, -tasks)

        while sum_tasks > T - i * P:
            if not pq:
                break
            sum_tasks += heapq.heappop(pq)

        answer = max(answer, len(pq))

    return answer


N, T, P = map(int, sys.stdin.readline().split())
K = list(map(int, sys.stdin.readline().split()))

print(solution(N, T, P, K))
