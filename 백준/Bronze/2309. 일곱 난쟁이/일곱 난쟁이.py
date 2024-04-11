from itertools import combinations

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

dwarf_combi = list(combinations(dwarfs, 7))

for dwarf_comb in dwarf_combi:
    if sum(dwarf_comb) == 100:
        answer = list(dwarf_comb)
        break

answer.sort()

for i in range(7):
    print(answer[i])

