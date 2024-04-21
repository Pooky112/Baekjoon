def solution(players):
    lists = sorted([key for key, value in players.items() if value >= 5])
    answer = ''.join(lists)
    return answer if answer else 'PREDAJA'

n = int(input())
players = {}

for i in range(n):
    name = input()
    if name[0] not in players:
        players[name[0]] = 1
    else:
        players[name[0]] += 1

print(solution(players))