def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    return ab if ab >= ba else ba

    #return int(max(f"{a}{b}", f"{b}{a}"))