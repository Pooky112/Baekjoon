def hanoi(n, answer, start, end, temp):
    if n == 1:
        answer.append([start, end])
    else:
        #위의 n-1개를 temp로 옮긴 후에
        hanoi(n-1, answer, start, temp, end)
        answer.append([start, end])
        #temp에 있는 걸 다시 옮김
        hanoi(n-1, answer, temp, end, start)
        

def solution(n):
    answer = []
    hanoi(n, answer, 1, 3, 2)

    return answer