import sys

input = sys.stdin.readline

N = int(input())

def movie(N):
    movie_name = 666
    while N:
        if "666" in str(movie_name):
            N -= 1
        movie_name += 1
        
    return movie_name - 1
    
    
print(movie(N))