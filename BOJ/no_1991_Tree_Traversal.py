# 0. 시간 제한 2초, 메모리 제한 128 MB이므로 재귀로 풀어도 무방함.
# 1. 딕셔너리를 사용해서 tree를 구성한다.

# 2. 전위 순회하기 위한 재귀함수 preorder(current)를 정의한다. 
    # 2-1. '현재 노드 --> left 노드 --> right 노드' 순으로 재귀 탐색한다.

# 3. 중위 순화하기 위한 재귀함수 inorder(current)를 정의한다.
    # 3-1. 'left 노드 --> 현재 노드 --> right 노드' 순으로 재귀 탐색한다.
    
# 4. 후위 순회하기 위한 재귀함수 postorder(current)를 정의한다.
    # 4-1. 'left 노드 --> right 노드 --> 현재 노드' 순으로 재귀 탐색한다.

import sys
input = sys.stdin.readline

N = int(input())
tree = dict()

for _ in range(N):
    root, right, left = input().split()
    tree[root] = [right, left]
    
def preorder(current):
    if current != '.':
        print(current, end='')
        preorder(tree[current][0])
        preorder(tree[current][1])
        
def inorder(current):
    if current != '.':
        inorder(tree[current][0])
        print(current, end='')
        inorder(tree[current][1])
        
def postorder(current):
    if current != '.':
        postorder(tree[current][0])
        postorder(tree[current][1])
        print(current, end='')
        
preorder('A')
print()
inorder('A')
print()
postorder('A')