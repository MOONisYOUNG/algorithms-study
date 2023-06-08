# Tag : 스택, 그리디

# 0. number는 2자리 이상, 10^6자리 이하 숫자이므로, 시간 효율성을 고려해야 한다.
# 1. answer 스택을 정의한다. 
# 2. i를 매개로 number 리스트 속 원소를 for 반복문으로 순회한다.
    # 2-1. 만약 k 횟수가 남았고, answer 스택에 내용물 존재하고, answer 스택 끝 부분이 i보다 작을 경우를 발견한다면...?
        # 2-1-2. answer 스택에서 pop을 연산하고, k -= 1을 통해 횟수를 차감한다.
    # 2-2. answer 스택에 i를 추가한다.
# 3. answer 스택에서 k횟수만큼 끝 부분을 제외해 준다.
# 3. ''.join(answer)를 return 연산한다.

def solution(number, k):
    answer = []
    
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    answer = answer[:len(answer)-k]
    return ''.join(answer)