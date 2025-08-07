import sys
from typing import List
input = sys.stdin.readline

def multiply_matrices(mat1: List[List[int]], mat2: List[List[int]], n: int) -> List[List[int]]:
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(n):
                result[r][c] = (result[r][c] + (mat1[r][k] * mat2[k][c])) % 1000
    return result

def solution(matrix: List[List[int]], b: int, n: int):
    if b == 1:
        for r in range(n):
            for c in range(n):
                matrix[r][c] %= 1000
        return matrix
    
    temp = solution(matrix, b // 2, n)
    
    if b % 2 == 0:
        return multiply_matrices(temp, temp, n)
    else:
        return multiply_matrices(multiply_matrices(temp, temp, n), matrix, n)

if __name__ == "__main__":
    n, b = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))

    answer = solution(a, b, n)
    for i in range(n):
        print(*(answer[i]), sep=' ')