def solution(myStr):
    
    changed = [s for s in (myStr.replace("b", "a").replace("c", "a")).split("a") if s]
    return changed if changed else ["EMPTY"]