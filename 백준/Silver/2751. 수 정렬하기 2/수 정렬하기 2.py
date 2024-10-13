import sys

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

for num in sorted(num_list):
    print(num)