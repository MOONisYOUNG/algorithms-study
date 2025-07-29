from typing import List

def solution(n: int) -> List[str]:
    if n == 1:
        return ['*']
        
    stars = solution(n // 3)
    star_li = []

    for star in stars: 
        star_li.append(star * 3)
        
    for star in stars:
        star_li.append(star + (' '  * (n//3)) + star)
        
    for star in stars:
        star_li.append(star * 3)
        
    return star_li

if __name__ == "__main__":
    n = int(input())
    print(*solution(n), sep='\n')