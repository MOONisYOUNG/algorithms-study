import sys
from datetime import date
input = sys.stdin.readline

def solution() -> str:
    today = tuple(map(int, input().split()))
    d_day = tuple(map(int, input().split()))
    
    if (today[0] + 1000) < d_day[0]:
        answer = 'gg'
        return answer
    
    elif (today[0] + 1000 == d_day[0]) and ((today[1], today[2]) <= (d_day[1], d_day[2])):
        answer = 'gg'
        return answer
            
    else:
        today = date(*today)
        d_day = date(*d_day)
        
        # A way to calculate neatly, including leap years
        answer = f'D-{(d_day.toordinal() - today.toordinal())}'
        return answer
 
print(solution())