import sys


def generate_triangle(max_value):
    triangle_numbers = []
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        if triangle_number > max_value:
            break
        triangle_numbers.append(triangle_number)
        n += 1

    return triangle_numbers


def solution(triangle_numbers, K):
    for i in triangle_numbers:
        for j in triangle_numbers:
            for k in triangle_numbers:
                if i + j + k == K:
                    return 1

    return 0


def main():
    triangle_numbers = generate_triangle(1000)

    N = int(sys.stdin.readline())
    answer = []
    for _ in range(N):
        K = int(sys.stdin.readline())
        answer.append(solution(triangle_numbers, K))

    for a in answer:
        print(a)


#2 4 11
main()