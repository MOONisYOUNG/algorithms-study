from typing import List, Tuple

# Parsing numbers and operators
def num_op_parsing(input_str: str)-> Tuple[List[int], List[str]]:
    op_li = []
    temp_str_li = list(input_str)
    
    for i in range(len(input_str)):
        # Finding operators
        if not input_str[i].isdigit():
            temp_str_li[i] = ' '
            op_li.append(input_str[i])
            
    # Parsing numbers
    num_li = list(map(int, ''.join(temp_str_li).split()))
    return (num_li, op_li)

def solution(input_str: str) -> int:
    answer = 0
    num_li, op_li = num_op_parsing(input_str)
    
    answer += num_li[0]
    for i in range(1, len(num_li)):
        op = op_li[i-1]
        if op == '+':
            answer += num_li[i]
        elif op == '-':
            answer -= num_li[i]
        else:
            answer *= num_li[i]
    
    return answer

# input example : '3+2*5-10' (-> output: 15)
print(solution(input()))