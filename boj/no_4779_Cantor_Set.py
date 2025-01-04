def cantor_set(array, start_idx, total_len):
    section_len = total_len // 3
    
    if section_len == 0:
        return 
    
    for i in range(start_idx+section_len, start_idx+section_len*2):
        array[i] = ' '
        
    cantor_set(array, start_idx, section_len)
    cantor_set(array, start_idx+section_len*2, section_len)


while True:
    try:
        N = input()
        if N == '':
            break
        else:
            N = int(N)
            array = ['-' for i in range(3**N)]
            cantor_set(array, 0, 3**N)
            print(''.join(array))
            
    except EOFError:
        break
