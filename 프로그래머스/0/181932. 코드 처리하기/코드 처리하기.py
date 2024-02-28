def solution(code):
    mode = 0
    ret = ""
    
    for idx, x in enumerate(code):
        if x != "1":
            if (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 == 1):
                ret += x
        else:
            mode = 1 - mode
    return ret if ret else "EMPTY"

"""
    def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
        """