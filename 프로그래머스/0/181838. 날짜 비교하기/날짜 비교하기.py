from datetime import date

def solution(date1, date2):
    d1 = date(*date1)
    d2 = date(*date2)
    
    return 1 if d1 < d2 else 0
