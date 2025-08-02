import sys
from typing import List

def solution(n: int) -> List[str]:
    canvas = [[' ' for _ in range(2*n - 1)] for _ in range(n)]

    def draw_pattern(row: int, col: int, size: int):
        if size == 3:
            canvas[row][col] = '*'
            canvas[row + 1][col - 1] = canvas[row + 1][col + 1] = '*'
            
            for i in range(-2, 3):
                canvas[row + 2][col + i] = '*'
            return
        new_size = size // 2
        draw_pattern(row, col, new_size)
        draw_pattern(row + new_size, col - new_size, new_size)
        draw_pattern(row + new_size, col + new_size, new_size)


    draw_pattern(0, n - 1, n)

    answer = []
    for row_data in canvas:
        answer.append("".join(row_data))
    return answer

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(*solution(n), sep='\n')