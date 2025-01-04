origin_string = input()

answer = 1 if origin_string[::-1] == origin_string else 0
print(answer)