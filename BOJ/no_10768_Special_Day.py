import sys
input = sys.stdin.readline

month = int(input())
day = int(input())

def solution():
    if month < 2:
        return "Before"
        
    elif month == 2:
        if day < 18:
            return "Before"
        
        elif day == 18:
            return "Special"
          
        else:
            return "After"
            
    else:
        return "After"
        
print(solution())