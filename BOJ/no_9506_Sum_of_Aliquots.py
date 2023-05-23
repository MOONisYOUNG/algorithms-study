# 1. 1 ~ n-1까지 반복문을 돌려서, n이 특정 값으로 나눠지는 경우만 리스트에 추가한다.
# 2-1. 더한 값이 n과 같으면, 약수들의 합으로 나타내어 출력한다.
# 2-2. 더한 값이 n과 다르면 'n is Not Perfect.'를 출력한다.

import sys

input = sys.stdin.readline

def solution():
    aliquot_li = []
    for i in range(1, n):
        if n % i == 0:
            aliquot_li.append(i)
    
    if sum(aliquot_li) == n:
        # n = a + b + c 꼴로 출력
        print(f"{n} = ", end='')
        for aliquot in aliquot_li[:-1]:
            print(f"{aliquot} + ", end='')
        print(aliquot_li[-1])
        
    else:
        print(f"{n} is NOT perfect.")
    

while True:
    n = int(input())
    
    if n == -1:
        break
    
    solution()