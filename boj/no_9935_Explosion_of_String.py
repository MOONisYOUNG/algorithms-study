import sys
input = sys.stdin.readline

def solution(original_str: str, explosion_str: str) -> str:
    stack = []
    bomb_len = len(explosion_str)

    for char in original_str:
        stack.append(char)
        if ''.join(stack[-bomb_len:]) == explosion_str:
            for _ in range(bomb_len):
                stack.pop()

    answer = ''
    if not stack:
        answer = "FRULA"
    else:
        answer = ''.join(stack)

    return answer

if __name__ == "__main__":
    original_str = input().strip()
    explosion_str = input().strip()
    print(solution(original_str, explosion_str))