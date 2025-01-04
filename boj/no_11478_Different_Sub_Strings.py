# 1. for i in range(1, len(S)+1)만큼 반복한다.
    # 1-1. for k in range(0, len(S)-i+1)만큼 반복한다. 
        # 1-2. S[k:k+i]를 sub_str_set에 넣는다.
# 2. answer = len(sub_str_set)를 연산해서 답을 구한다.

S = input()

sub_str_set = set()
for i in range(1, len(S)+1):
    for k in range(0, len(S)-i+1):
        sub_str_set.add(S[k:k+i])
        
answer = len(sub_str_set)
print(answer)