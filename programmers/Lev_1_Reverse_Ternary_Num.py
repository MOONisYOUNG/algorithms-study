# Tag : 수학
def solution(n):
    # 1. 10진법 --> 앞뒤 반전 3진법 (문자열 + 연산자 특성 이용하기)
    # 2. 앞뒤 반전 3진법 --> 10진법 (int 함수 사용해서 n진수를 10진수로 변환하기)
    
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    
    # 10진법으로 표현
    return int(rev_base, 3)            