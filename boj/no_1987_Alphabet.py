import sys
input = sys.stdin.readline

def solution(r: int, c: int) -> int:
    board = [list(input().strip()) for _ in range(r)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_count = 0
    visited_alphabets = set()

    def dfs(x: int, y: int, count: int):
        nonlocal max_count
        max_count = max(max_count, count)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (0 <= nx < r) and (0 <= ny < c):
                if board[nx][ny] not in visited_alphabets:
                    visited_alphabets.add(board[nx][ny])
                    dfs(nx, ny, count + 1)
                    visited_alphabets.remove(board[nx][ny])

    visited_alphabets.add(board[0][0])
    dfs(0, 0, 1)

    answer = max_count
    return answer

if __name__ == "__main__":
    r, c = map(int, input().split())
    print(solution(r, c))