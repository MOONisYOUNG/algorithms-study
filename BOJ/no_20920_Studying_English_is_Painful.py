# 0-1. 시간 제한 1초, 메모리 제한 1024 MB
# 0-2. 따라서 반복문 사용을 최소화시키고, 공간을 최대한 활용하는 풀이로 작성하는 게 좋다.
# 1. word_dict에 단어 길이가 M인 word만 추가한다.
    # 1-1. word_dict에 등록된 단어가 아니라면, word_dict[word] = 0를 저장한다.
    # 1-2. word_dict에 등록된 단어라면, word_dict[word] += 1을 연산한다.
# 2. word_dict.items()를 정렬한다. 정렬 기준은 (-횟수, -문자열 길이, 문자열 정보)를 사용한다.
# 3. 정렬한 word_li의 인덱스 0부분만 출력한다.


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = dict()
for _ in range(N):
    word = input().rstrip()
    
    if len(word) >= M:
        if not word in word_dict:
            word_dict[word] = 0
        else:
            word_dict[word] += 1

word_li = sorted(word_dict.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for word in word_li:
    print(word[0])