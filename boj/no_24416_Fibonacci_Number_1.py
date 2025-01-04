import sys

input = sys.stdin.readline

n = int(input())

fib_cnt = 1
fibonacci_cnt = 0

def fib(n):
    global fib_cnt
    if n <= 2:
        return 1
    else:
        fib_cnt += 1
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    global fibonacci_cnt
    d = [0] * (n+1)
    
    d[1] = 1
    d[2] = 1
    
    for i in range(3, n+1):
        fibonacci_cnt += 1
        d[i] = d[i-1] + d[i-2]


fib(n)
print(fib_cnt, end=' ')

fibonacci(n)
print(fibonacci_cnt)