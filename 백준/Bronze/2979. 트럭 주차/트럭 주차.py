import sys

def solution(A, B, C, time):
    answer = 0
    fee = [A, B, C]
    start, end = 100, 0
    for i in range(3):
        start = min(start, time[i][0])
        end = max(end, time[i][1])

    while start <= end:
        cur_trucks = 0
        for i in range(3):
            if time[i][0] <= start < time[i][1]:
                cur_trucks += 1
        answer += cur_trucks * fee[cur_trucks - 1]
        start += 1

    return answer

A, B, C = map(int, sys.stdin.readline().split())
time = []
for _ in range(3):
    i, o = map(int, sys.stdin.readline().split())
    time.append((i, o))

print(solution(A, B, C, time))