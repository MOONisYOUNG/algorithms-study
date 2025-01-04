import sys
input = sys.stdin.readline

t = int(input())

def solution(t):
    if t % 10 != 0:
        # 3개 버튼으로 T초를 맞출 수 없으므로 -1 반환
        return [-1]
        
    answer = []
    # 300, 60, 10은 서로 배수 및 약수 관계에 놓여 있으므로 그리디로 해결 가능
    button_li = [300, 60, 10]
    
    for button in button_li:
        answer.append(t // button)
        t %= button
    
    return answer
    
print(*solution(t), sep=' ')