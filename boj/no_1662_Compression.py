import sys
input = sys.stdin.readline

s = input()[:-1]
len_s = len(s)

# len_arr[cur_i]에 괄호 cur_i개 내부에 있는 숫자 개수를 기록
len_arr = [0] * len_s
# num_arr[cur_i]에 '(' 괄호 직전에 해당하는 숫자를 기록
num_arr = [0] * len_s
# cur_i는 현재 체크 중인 괄호의 개수를 의미; num은 임시로 숫자를 기록;
cur_i = 0; num = 0;

for i in range(len_s):
    if s[i] == '(':
        len_arr[cur_i] -= 1
        cur_i += 1
        num_arr[cur_i] = num
        
    elif s[i] == ')':
        temp = len_arr[cur_i] * num_arr[cur_i]
        len_arr[cur_i] = 0
        cur_i -= 1
        len_arr[cur_i] += temp
    
    else:
        len_arr[cur_i] += 1
        num = int(s[i])
        
answer = len_arr[0]
print(answer)