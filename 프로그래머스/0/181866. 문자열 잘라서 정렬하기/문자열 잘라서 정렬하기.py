def solution(myString):
    split = [s for s in myString.split("x") if s]
    split.sort()
    return split