isbn_str = input()

def solution(isbn_str: str) -> int:
    for i in range(10):
        isbn_temp = isbn_str.replace('*', str(i))
        
        val = 0
        for j in range(13):
            if j % 2 == 0:
                val += int(isbn_temp[j])
            else:
                val += (int(isbn_temp[j]) * 3)
        
        if val % 10 == 0:
            answer = i
            return answer
            
print(solution(isbn_str))