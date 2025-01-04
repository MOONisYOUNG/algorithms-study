import sys

input = sys.stdin.readline

def is_palindrome(string):
    return string[::1] == string[::-1]

while True:
    num_string = input().rstrip()
    
    if num_string == '0':
        break 
    
    if is_palindrome(num_string):
        print("yes")
    else:
        print("no")
