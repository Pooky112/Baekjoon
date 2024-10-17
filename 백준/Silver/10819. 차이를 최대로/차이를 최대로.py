import itertools
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

max_value = 0
for perm in itertools.permutations(array):
    sum_value = 0
    for i in range(len(array) - 1):
        sum_value += abs(perm[i] - perm[i + 1])
    max_value = max(max_value, sum_value)

print(max_value)