import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

prime_count = 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in numbers:
    if is_prime(num):
        prime_count += 1

print(prime_count)