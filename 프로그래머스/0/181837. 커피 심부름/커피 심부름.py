def solution(order):
    answer = 0
    for item in order:
        answer += 4500 if "americano" in item or "anything" in item else 5000
    return answer