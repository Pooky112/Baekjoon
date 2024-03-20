def solution(arr):
    # 숫자만 추출하여 정수 리스트로 변환
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    # 연산자 리스트
    operators = arr[1:len(arr):2]

    # n은 숫자의 개수
    n = len(numbers)
    # dp 테이블 초기화: dp[i][j]는 numbers[i]부터 numbers[j]까지의 서브 배열에 대한 (최소값, 최대값)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
    
    # 초기 조건: 단일 숫자에 대한 최소값과 최대값은 그 숫자 자체
    for i in range(n):
        dp[i][i] = (numbers[i], numbers[i])

    # 서브 배열의 길이 l (2부터 시작)
    for l in range(2, n+1):
        # 서브 배열의 시작점 i
        for i in range(n-l+1):
            # 서브 배열의 끝점 j
            j = i+l-1
            # 초기 최소값과 최대값 설정
            min_val = float('inf')
            max_val = float('-inf')
            # 구간 내의 모든 가능한 분할 지점 k를 기준으로 계산
            for k in range(i, j):
                # 현재 연산자
                op = operators[k]
                # 분할된 구간의 결과값 계산
                left = dp[i][k]
                right = dp[k+1][j]
                # 연산자에 따라 결과값 계산
                if op == '+':
                    min_val = min(min_val, left[0] + right[0])
                    max_val = max(max_val, left[1] + right[1])
                elif op == '-':
                    min_val = min(min_val, left[0] - right[1])
                    max_val = max(max_val, left[1] - right[0])
            # 계산된 최소값과 최대값을 dp 테이블에 저장
            dp[i][j] = (min_val, max_val)

    # 전체 배열에 대한 최대 결과값 반환
    return dp[0][n-1][1]
