import sys
input = sys.stdin.readline

N = int(input())
dna = list(input().rstrip())

dna_list = [['A', 'C', 'A', 'G'], 
            ['C', 'G', 'T', 'A'],
            ['A', 'T', 'C', 'G'],
            ['G', 'A', 'G', 'T']]
    
dna_dict = {'A':0, 'G':1, 'C':2, 'T':3}
            
while len(dna) > 1:
    row_dna_idx, col_dna_idx = dna_dict[dna[-2]], dna_dict[dna[-1]]
    del dna[-2], dna[-1]
    dna.append(dna_list[row_dna_idx][col_dna_idx])
    
print(dna[0])