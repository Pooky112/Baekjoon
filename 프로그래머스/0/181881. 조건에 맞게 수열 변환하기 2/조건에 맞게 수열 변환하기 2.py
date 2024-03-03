def solution(arr):
    x = 0
    
    while True:
        next_arr = [n // 2 if n >= 50 and n % 2 == 0 else n * 2 + 1 if n < 50 and n % 2 != 0 else n for n in arr]
                
        if next_arr == arr:
            return x
        arr = next_arr
        x+=1
  