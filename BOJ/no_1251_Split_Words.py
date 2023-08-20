import sys
input = sys.stdin.readline

word = input().rstrip()

total_new_words = []

for i in range(1, len(word)-2):
    split_word_1st = word[:i][::-1]
    
    for j in range(i+1, len(word)):
        new_word = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        total_new_words.append(new_word)
    
print(min(total_new_words))