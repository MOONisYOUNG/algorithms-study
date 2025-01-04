import sys
input = sys.stdin.readline

def solution(*positions):
    a, b, c = positions
    # 사실상 첫 회에서 판가름 나기 때문에, 반복문으로 단계를 하나하나 따질 필요 X
    answer = max(b-a-1, c-b-1)
    return answer
    
while True:
    try:
        a, b, c = map(int, input().split())
        print(solution(a, b, c))
        
    except:
        break