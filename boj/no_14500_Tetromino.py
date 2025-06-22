import sys
from typing import List, Tuple
input = sys.stdin.readline

n, m = map(int, input().split())

def get_tetromino_shapes() -> List[List[Tuple[int]]]:
    
    def normalize_shape(shape: List[Tuple[int]]) -> Tuple[Tuple[int]]:
        min_r = min(p[0] for p in shape)
        min_c = min(p[1] for p in shape)
        normalized = sorted([(p[0] - min_r, p[1] - min_c) for p in shape])
        return tuple(normalized)
        
    def rotate_90(shape: List[Tuple[int]]) -> Tuple[Tuple[int]]:
        rotated = []
        for r, c in shape:
            rotated.append((-c, r))
        return normalize_shape(rotated)
        
    def flip_horizontal(shape: List[Tuple[int]]) -> Tuple[Tuple[int]]:
        flipped = []
        for r, c in shape:
            flipped.append((r, -c))
        return normalize_shape(flipped)
        
    block_I = normalize_shape([(0,0), (0,1), (0,2), (0,3)])
    block_O = normalize_shape([(0,0), (0,1), (1,0), (1,1)])
    block_L = normalize_shape([(0,0), (1,0), (2,0), (2,1)])
    block_S = normalize_shape([(0,0), (1,0), (1,1), (2,1)])
    block_T = normalize_shape([(0,0), (0,1), (0,2), (1,1)])
    
    all_unique_shapes = set()
    
    current_shape = block_I
    for _ in range(2):
        all_unique_shapes.add(current_shape)
        all_unique_shapes.add(flip_horizontal(current_shape))
        current_shape = rotate_90(current_shape)
    
    all_unique_shapes.add(block_O)
    
    current_shape = block_L
    for _ in range(4):
        all_unique_shapes.add(current_shape)
        all_unique_shapes.add(flip_horizontal(current_shape))
        current_shape = rotate_90(current_shape)
        
    current_shape = block_S
    for _ in range(2):
        all_unique_shapes.add(current_shape)
        all_unique_shapes.add(flip_horizontal(current_shape))
        current_shape = rotate_90(current_shape)
        
    current_shape = block_T
    for _ in range(4):
        all_unique_shapes.add(current_shape)
        all_unique_shapes.add(flip_horizontal(current_shape))
        current_shape = rotate_90(current_shape)
        
    return [list(shape) for shape in all_unique_shapes]


def solution(n: int, m: int) -> int:
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    all_tetromino_shapes = get_tetromino_shapes()
    
    max_sum = 0
    
    for r in range(n):
        for c in range(m):
            for shape in all_tetromino_shapes:
                current_sum = 0
                is_valid = True
                
                for dr, dc in shape:
                    nr, nc = r + dr, c + dc
                    
                    if not ((0 <= nr < n) and (0 <= nc < m)):
                        is_valid = False
                        break
                    current_sum += board[nr][nc]
                
                if is_valid:
                    max_sum = max(max_sum, current_sum)
    
    answer = max_sum
    return answer
        
print(solution(n, m))