# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

import re

# B. Viết chương trình kiểm tra một câu có đúng cú pháp hay không?
with open('D:\Study\CT121_THLT\TH\lab3\data.txt', 'r') as file:
    lines = file.readlines()

def B1(line):
    # 1) Câu được bắt đầu bằng ký tự in hoa, theo sau bởi ký tự thường
    return re.match(r'^[A-Z][a-z].*', line);

def B2(line):
    # 2) Kết thúc bằng dấu chấm hoặc sau một ký tự in hoa
    if re.match(r'.*[.]$', line):
        return re.match(r'^[A-Z][^A-Z].*', line);
    else:
        return False

def B3(line):
    # 3) Các từ cách nhau bằng một khoảng trắng, không chấp nhận nhiều hơn 1 khoảng trắng liên tiếp
    return re.match(r'^[^' ']' '', line);

def B(line):
    for line in lines:
        line = line.strip()
        if B1(line) and B2(line):
            if B3(line):
                print(line)
            else:
                print("Sai cú pháp")
        else:
            print("Sai cú pháp")

if __name__ == "__main__":
    B(lines)

