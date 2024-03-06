def solution(phone_book):
    """
    phone_book.sort()
    for i in range(len(phone_book) -1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
            
    return True

"""
    p_table = set(phone_book)
    for num in phone_book:
        temp = ''
        for pnum in num:
            temp += pnum
            if temp in p_table and temp != num:
                return False
    return True
        
        