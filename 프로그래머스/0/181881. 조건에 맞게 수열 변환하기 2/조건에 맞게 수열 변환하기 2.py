def solution(arr):
    x = 0
    next_arr = arr[:]
    while True:
        for i,n in enumerate(arr):
            if n>= 50 and n % 2 ==0:
                next_arr[i] = n // 2
            elif n < 50 and n %2 != 0:
                next_arr[i] = n * 2 + 1
            else:
                next_arr[i] = n
        if next_arr == arr:
            return x
        arr = next_arr[:]
        x+=1
  