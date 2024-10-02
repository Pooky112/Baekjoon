import sys

N = int(sys.stdin.readline().strip())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n

result = factorial(N)

print(result)
