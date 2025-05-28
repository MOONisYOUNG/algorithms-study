import sys
from typing import Union
input = sys.stdin.readline

def solution() -> Union[str, int]:
    num = 0
    for _ in range(3):
        word = input()[:-1]
        if word.isdigit():
           num = int(word)
        elif not word.isdigit() and num != 0:
            num += 1
    num += 1
    
    if (num % 3 == 0) and (num % 5 == 0):
        answer = "FizzBuzz"
    elif (num % 3 == 0) and (num % 5 != 0):
        answer = "Fizz"
    elif (num % 3 != 0) and (num % 5 == 0):
        answer = "Buzz"
    else:
        answer = num
        
    return answer
    
print(solution())