# def solution(money):
#     n = len(money)
#     #dp[i]를 집 i까지의 최대 금액
#     #점화식 - dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
#     dp = [0 for _ in range(n)]
#     dp2 = [0 for _ in range(n)]
    
#     #첫 번째 집을 터는 경우
#     dp[0] = money[0]
#     dp[1] = max(money[0], money[1])
#     for i in range(2, n-1):
#         dp[i] = max(dp[i-1], dp[i-2] + money[i]) 
    
                                               
#     #마지막 집을 터는 경우
#     m = money[-1:] + money[:n-1]
#     dp2[0] = m[0]
#     dp2[1] = max(m[0], m[1])
#     for i in range(2, n-1):
#         dp2[i] = max(dp2[i-1], dp2[i-2] + m[i])
    
#     max_val = max(max(dp), max(dp2))
    
#     return max_val
        
    
def rob(money):
    prev_max = 0
    curr_max = 0
    
    for m in money:
        prev_max, curr_max = curr_max, max(curr_max, prev_max + m)

    return curr_max

def solution(money):
    #첫 번째 집을 터는 경우
    max_first_house = rob(money[:-1])
    #마지막 집을 터는 경우
    max_last_house = rob(money[1:])    
    
    return max(max_first_house, max_last_house)
        
    