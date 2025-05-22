import sys
input = sys.stdin.readline

def solution() -> int:
    answer = 0
    
    for row_num in range(8):
        
        # Assign white zone data at the starting point of the row
        if row_num % 2 == 0:
            white_flag = True
        else:
            white_flag = False
        
        row = input()[:-1]
        
        for i in row:
            if white_flag:
                if i == 'F':
                    answer += 1
                white_flag = False
            else:
                white_flag = True
    
    return answer
    
print(solution())