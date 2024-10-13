import sys

N = int(sys.stdin.readline())
num_count = [0] * (10000 + 1)
for _ in range(N):
    num_count[int(sys.stdin.readline())] += 1

for i in range(len(num_count)):
    if num_count[i] != 0:
        for _ in range(num_count[i]):
            print(i)