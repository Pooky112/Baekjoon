import sys

def max_sum(n, arr):
    arr.sort()
    i = 0
    j = n - 1
    sum = 0
    
    while i < n - 1 and arr[i] < 0 and arr[i + 1] <= 0:
        sum += arr[i] * arr[i + 1]
        i += 2

    while j > 0 and arr[j] > 1 and arr[j - 1] > 1:
        sum += arr[j] * arr[j - 1]
        j -= 2
    
    while i <= j:
        sum += arr[i]
        i += 1

    return sum


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

print(max_sum(n, arr))