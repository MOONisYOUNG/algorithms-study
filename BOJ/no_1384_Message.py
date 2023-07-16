# 0. 시간 제한 1초, 메모리 제한 128 MB이므로 전형적인 구현 문제라고 판단 가능함.
# 1. 1차원 배열 name_li에 name을 넣어서 관리한다.
  # 1-1. 음수 인덱스를 다룰 때에는 리스트로 사용하는 것이 좋기 때문임.
# 2. 2차원 배월 message_li에 message P/N 정보를 넣어서 관리한다.

import sys
input = sys.stdin.readline

def solution(people_cnt, name_li, message_li):
    neg_cnt = 0
    for k in range(people_cnt):
        messages = message_li[k]
        for i in range(people_cnt-1):
            if messages[i] == 'N':
                neg_cnt += 1
                
                to_name = name_li[k]
                from_name = name_li[k - (i+1)]
                print(f"{from_name} was nasty about {to_name}")
    
    if neg_cnt == 0:
        print("Nobody was nasty")
    

group_cnt = 0
while True:
    people_cnt = int(input())
    
    if people_cnt == 0:
        break
    
    group_cnt += 1
    if group_cnt != 1:
        print(f"\nGroup {group_cnt}")
    else:  
      print(f"Group {group_cnt}")

    name_li = []
    message_li = []
    for i in range(people_cnt):
        temp = input().split()
        name_li.append(temp[0])
        message_li.append(list(temp[1:]))
        
    solution(people_cnt, name_li, message_li)