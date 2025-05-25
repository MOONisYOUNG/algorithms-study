import sys
from datetime import datetime
input = sys.stdin.readline

today = input()[:-1]

def solution(today: str) -> float:
    month_dd, yyyy_hh_mm = today.split(', ')
    
    month, dd = month_dd.split()
    yyyy, hh_mm = yyyy_hh_mm.split()
    hh, mm = hh_mm.split(':')
    
    month_dict = {
        'January':1, 'February':2, 'March':3, 'April':4, 'May':5,
        'June':6, 'July':7, 'August':8, 'September':9, 'October':10,
        'November':11, 'December':12
    }
    
    yyyy, dd, hh, mm = map(int, [yyyy, dd, hh, mm])
    
    today = datetime(yyyy, month_dict[month], dd, hh, mm)
    new_year_day = datetime(yyyy, 1, 1, 0, 0, 0)
    next_new_year_day = datetime(yyyy+1, 1, 1, 0, 0, 0)
    
    numer = (today - new_year_day).total_seconds()
    denom = (next_new_year_day - new_year_day).total_seconds()
    
    answer = (numer / denom) * 100
    return answer
    
print(solution(today))