def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    if start_time == 0 or start_time == 12 * 3600:
        answer += 1
    #초 단위 미만의 단위도 잘 고려해야 한다.
    while start_time < end_time:
        h_cur_angle = start_time / 120 % 360
        m_cur_angle = start_time / 10 % 360
        s_cur_angle = start_time * 6 % 360
        
        h_next_angle = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        m_next_angle = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        s_next_angle = 360 if (start_time +1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360
        
        if s_cur_angle < h_cur_angle and s_next_angle >= h_next_angle:
            answer += 1
        if s_cur_angle < m_cur_angle and s_next_angle >= m_next_angle:
            answer += 1
        if s_next_angle == m_next_angle and m_next_angle == h_next_angle:
            answer -= 1
        
        start_time += 1
        
    return answer