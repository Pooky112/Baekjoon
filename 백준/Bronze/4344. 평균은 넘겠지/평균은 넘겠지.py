import sys

C = int(sys.stdin.readline())
test_cases = []
for i in range(C):
    test_cases.append(list(map(int, sys.stdin.readline().split())))

for test_case in test_cases:
    n = test_case[0]
    test_case = test_case[1:]

    avg = sum(test_case) / n
    above_avg_count = 0

    for score in test_case:
        if score > avg:
            above_avg_count += 1

    result = (above_avg_count / n) * 100

    print("{:.3f}%".format(result))

