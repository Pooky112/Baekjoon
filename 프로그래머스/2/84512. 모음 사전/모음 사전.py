def solution(word):
    answer = 0
    word_list = ["A", "E", "I", "O", "U"]
    num_list = [781, 156, 31, 6, 1]
    
    for i, letter in enumerate(word):
        index = word_list.index(letter)
        answer += num_list[i] * index + 1

    return answer