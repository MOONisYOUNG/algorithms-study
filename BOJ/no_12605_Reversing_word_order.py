import sys
input = sys.stdin.readline

n = int(input())

# Solution 1: The standard style using a stack structure
def stack_sol(sol_str: str, sol_int: int) -> str:
    stack = sol_str.split()
    pop_li = []
    while stack:
        pop_li.append(stack.pop())
    return f'Case #{sol_int}: {" ".join(pop_li)}'
    
# Solution 2: The pythonic style
def pythonic_sol(sol_str: str, sol_int: int) -> str:
    stack = sol_str.split()
    return f'Case #{sol_int}: {" ".join(stack[::-1])}'
    
for i in range(n):
    case_str = input()[:-1]
    # print(stack_sol(case_str, i+1))
    print(pythonic_sol(case_str, i+1))