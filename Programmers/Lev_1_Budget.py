# Tag : 브루트 포스, 정렬

# 1. 신청 금액 리스트 d를 오름차순으로 정렬한 후, sorted_d 리스트로 반환한다.
# 2. sorted_d 리스트를 k개씩 잘라서 합산한 값이 budget보다 작은 경우만 money_k_list에 넣는다. 
# 3. mone_k_list가 비었으면 0을 반환하고, money_k_list 안 비었으면 끝 원소의 인덱스 1 값을 반환한다.

def solution(d, budget):
    sort_d = sorted(d)
    money_k_li = [(sum(sort_d[:(idx+1)]), idx+1) for idx in range(len(sort_d)) if sum(sort_d[:(idx+1)]) <= budget]
    
    return 0 if not money_k_li else money_k_li[-1][1]