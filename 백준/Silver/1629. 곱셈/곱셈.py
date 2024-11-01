import sys

a, b, c = map(int, sys.stdin.readline().split())

def solution(a, b, c):
    if b == 0:
        return 1
    half = solution(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    else:
        return (half * a) % c

print(solution(a, b, c))