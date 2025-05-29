import sys
input = sys.stdin.readline

str_li = [input()[:-1] for _ in range(3)]
int_li = [int(i) for i in str_li]

def solution_step_1(a: int, b: int, c: int) -> int:
    answer = a + b - c
    return answer
    
def solution_step_2(a: str, b: str, c: str) -> str:
    answer = str(int(a + b) - int(c))
    return answer
    
print(solution_step_1(*int_li))
print(solution_step_2(*str_li))