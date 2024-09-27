import sys

n = int(sys.stdin.readline())
test_cases = []

for i in range(n):
    test_cases.append(sys.stdin.readline().strip())

for test_case in test_cases:
    score = 0
    test_case = test_case.split("X")
    for i in test_case:
        j = 1
        while j <= len(i):
            score += j
            j += 1

    print(score)



