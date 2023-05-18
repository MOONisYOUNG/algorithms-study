from collections import Counter
def solution(want, number, discount):
    # 0. answer = 0 (가능한 날이 없으면 0이므로, 해당 값으로 디폴트 값 설정)
    # 1. want_dict 정의하기 (개수 대조하는 용도)
    # 2. temp_list = discount 리스트 인덱싱해서 자르기 (for 반복문 사용)
    # 3. temp_list에 Counter을 취해서 문제 속 조건을 만족하는지 확인하기
        # 3-1. 조건을 만족하면 answer += 1을 진행함
    
    answer = 0
    want_dict = {key:val for key, val in zip(want, number)}
    
    for i in range(len(discount)-10+1):
        temp_list = discount[i:i+10]
        if want_dict == dict(Counter(temp_list)):
            answer += 1
        
    return answer