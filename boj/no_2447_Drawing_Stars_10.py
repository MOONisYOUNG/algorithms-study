# tag - 분할 정복, 재귀
def draw_stars(n):
    if n==1:
        return ['*']
        
    Stars=draw_stars(n//3)
    L=[]
    
    # 리스트에 담긴 내용물을 str 형태로 풀어주기 위해서 for 반복문 사용
    for star in Stars: 
        L.append(star*3)
        
    for star in Stars:
        L.append(star+' '*(n//3)+star)
        
    for star in Stars:
        L.append(star*3)
        
    return L


N=int(input())
print('\n'.join(draw_stars(N)))