import sys

arith_expression = sys.stdin.readline().rstrip()

def lost_parentheses(arith_expression):
    sub_expression = arith_expression.split('-')
    num_li = []
    for group_expression in sub_expression:
        sum_val = 0
        plus_li = group_expression.split('+')
        for num in plus_li:
            sum_val += int(num)
        num_li.append(sum_val)
    result = num_li[0]
    for i in range(1, len(num_li)):
        result -= num_li[i]
    
    return result
    
    
print(lost_parentheses(arith_expression))