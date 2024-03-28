def solution(park, routes):
    directions = {'S':(1, 0), 'N':(-1, 0), 'W':(0, -1), 'E':(0, 1)}
    w = len(park[0])
    h = len(park)

    for i in range(len(park)):
        if 'S' in park[i]:
            x, y = i, park[i].index('S')
            break
    
    for route in routes:
        direction, distance = route.split()
        curr_x, curr_y = x, y
        for i in range(int(distance)):
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
            
            if 0 <= nx <= h-1 and 0 <=ny <= w-1 and (park[nx][ny] != "X"):
                x, y = nx, ny
            else:
                x, y = curr_x, curr_y
                break
    
    return [x, y]
            
    