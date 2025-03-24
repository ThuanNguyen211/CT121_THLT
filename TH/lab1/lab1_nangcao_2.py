# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

import itertools
DNA = ['A', 'T', 'C', 'G']
DNA_start = 'ATG'
DNA_accept = ['TAA', 'TAG', 'TGA']

L_temp=list(itertools.permutations(DNA, 3))
codons = set()
for i in L_temp:
    str = "".join(list(i))
    codons.add(str)

def check_DNA(L):
    L_start = L[:3]
    L_end = L[-3:]
    L_middle = []
    i = 3
    for i in range(i, len(L) - 3):
        if i % 3 != 0:
            continue
        str = L[i:i+3]
        L_middle.append(str)

    if len(L) % 3 != 0:
        return 'NO'
    elif L_start != DNA_start:
        return 'NO'
    elif L_end not in DNA_accept:
        return 'NO'
    
    for i in L_middle:
        if i not in codons:
            return 'NO'
    return 'YES'

L1 = 'ATGCCCTAG' # Output: không hợp lệ
print(L1, check_DNA(L1))
L2 = 'ATGCGTTGA' # Output: hợp lệ
print(L2, check_DNA(L2))
