def solution(number, limit, power):
    iron_cnt_li = []

    for num in range(1, number+1):
        cnt = 0
        for j in range(1, int(num**(1/2))+1):            
            if num % j == 0:
                if j*j == num:
                    cnt += 1
                else:
                    cnt += 2
        if cnt > limit:
            cnt = power
        iron_cnt_li.append(cnt)
            
    return sum(iron_cnt_li)