def solution(n, k, electronics):
    sockets = [0] * n
    next_uses = [0] * n
    answer = 0

    def update_next_use(i, plug_index):
        if electronics[i + 1:].count(electronics[i]) >= 1:
            idx = electronics.index(electronics[i], i + 1, k)
            next_uses[plug_index] = idx - i
        else:
            next_uses[plug_index] = k


    for i in range(k):
        for j in range(n):
            next_uses[j] -= 1

        if electronics[i] in sockets:
            update_next_use(i, sockets.index(electronics[i]))
            continue
        else:
            if 0 in sockets:
                empty_index = sockets.index(0)
                sockets[empty_index] = electronics[i]
                update_next_use(i, empty_index)
            else:
                unplug_index = next_uses.index(max(next_uses))
                sockets[unplug_index] = electronics[i]
                answer += 1
                update_next_use(i, unplug_index)

    print(answer)


n, k = map(int, input().split())
electronics = list(map(int, input().split()))

solution(n, k, electronics)