import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for num in arr:
    if num < x:
        print(num, end=" ")
