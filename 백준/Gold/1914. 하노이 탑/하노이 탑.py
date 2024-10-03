import sys

N = int(sys.stdin.readline().strip())

def hanoi_tower(N, move_from, move_to, move_through):
    if N == 1:
        print(move_from, move_to)
        return
    hanoi_tower(N - 1, move_from, move_through, move_to)
    print(move_from, move_to)
    hanoi_tower(N - 1, move_through, move_to, move_from)

print(2**N - 1)

if N <= 20:
    hanoi_tower(N, 1, 3, 2)
