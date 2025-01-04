# Tag : 시뮬레이션
def solution(dirs):
    # 0-1. 경로의 디폴트 값은 0이므로, answer = 0으로 설정한다. 
    # 0-2. 기본 위치를 x, y = 0, 0으로 설정한다. 
    # 1. U, D, R, L에 대응하는 방향이동을 설정한다. (딕셔너리 사용)
    # 2. dirs를 하나씩 읽어서 이동시킨다. 이때 방문 정보(방문 방향 고려x)를 입력한다.
        # 2-1. 좌표 이탈한 경우라면, continue 적용
        # 2-2. 방문한 지역이라면, 자리 이동만 하고 continue 적용
        # 2-3. 좌표 이탈 x, 방문 x에 해당한다면 answer += 1 적용 (visited 처리도 필수)
        
    answer = 0
    x, y = 0, 0
    dir_dict = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visited = []
    
    for dir in dirs:
        dx, dy = dir_dict[dir]
        new_x, new_y = x + dx, y + dy
        
        if new_x < -5 or new_x > 5 or new_y < -5 or new_y > 5:
            continue
            
        elif ((x, y), (new_x, new_y)) in visited:
            x, y = new_x, new_y
            continue
            
        else:
            visited.append(((x, y), (new_x, new_y)))
            visited.append((((new_x, new_y)), (x,y)))
            x, y = new_x, new_y
            answer += 1
    
    return answer