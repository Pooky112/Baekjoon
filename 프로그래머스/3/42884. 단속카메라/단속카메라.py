def solution(routes):
    #처음에 하나는 설치 이후 겹치는 부분을 고려
    answer = 1

    #진출 지점을 기준으로 정렬하여 빠져나가는 순서대로 처리
    routes.sort(key=lambda x:x[1])
    camera = routes[0][1]
    
    for route in routes:
        if camera < route[0]:#시작지점보다 작을 경우 카메라 한 대 추가 및 카메라 위치 변경
            answer += 1
            camera = route[1]
            
    return answer