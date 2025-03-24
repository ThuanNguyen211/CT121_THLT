# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

import itertools

A1 = ['0011', '11', '1101']
B1 = ['110110', '00', '110']
A2 = ['100', '0', '1']
B2 = ['1', '100', '0']

# L1 = ['110','0011','0110']
# L2 = ['110110','00','110']
def check(L1, L2):
    L1_temp=list(itertools.permutations(L1, len(L1))) # tạo các hoán vị
    S1 = set() # tạo tập hợp rỗng
    for i in L1_temp:
        str1 = "".join(list(i)) #mỗi hoán vị kết nối thành chuỗi
        S1.add(str1)
    # print(S1)

    L2_temp=list(itertools.permutations(L2, len(L2)))
    S2 = set()
    for i in L2_temp:
        str2 = "".join(list(i))
        S2.add(str2)
    # print(S2)

    S3=S1.intersection(S2)
    if (len(S3) != 0):
        print("YES")
    else:
        print("NO")

print('A = ' + str(A1))
print('B = ' + str(B1))
check(A1, B1)

print('A = ' + str(A2))
print('B = ' + str(B2))
check(A2, B2)