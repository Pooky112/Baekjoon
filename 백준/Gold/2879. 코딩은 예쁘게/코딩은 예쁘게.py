import sys

N = int(sys.stdin.readline())
current_tab = list(map(int, sys.stdin.readline().split()))
correct_tab = list(map(int, sys.stdin.readline().split()))

def make_correct_indent(n, current_tab, correct_tab):
    diff = []
    for i in range(n):
        diff.append(correct_tab[i] - current_tab[i])

    temp = [0] * n
    temp[0] = abs(diff[0])

    i = 1
    while i < n:
        if diff[i] * diff[i - 1] > 0:
            temp[i] = temp[i - 1] + max(0, abs(diff[i]) - abs(diff[i - 1]))
        else:
            temp[i] = temp[i - 1] + abs(diff[i])
        i += 1
    return temp[-1]


print(make_correct_indent(N, current_tab, correct_tab))
