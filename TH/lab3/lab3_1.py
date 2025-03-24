# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

import re

# A. Đọc file txt, và xây dựng btcq để tìm và in:
with open('./data.txt', 'r') as file:
    lines = file.readlines()

def A1(text):
    # 1) Các dòng bắt đầu bằng ‘t’ hoặc ‘h’, và có chứa ‘re’ (sử dụng phương thức re.match())
    for line in lines:
        line = line.strip() 
        if re.match(r'^[th].*re', line, re.IGNORECASE):
            print(line)

def A2(text):
    for line in lines:
        line = line.strip()
        if len(line) > 20:
            print(line)

def A3(text):
    # 3) Các dòng kết thúc bởi cặp dấu ‘?!’
    for line in lines:
        line = line.strip()
        if re.match(r'.*[?!]$', line):
            print(line)

def A4(text):
    # 4) Các dòng chứa những ký tự: a, r, s, m, l (không cần liên tục)
    for line in lines:
        line = line.strip()
        if re.match(r'.*a.*r.*s*.m.*l.*', line):
            print(line)

def A5(text):
    # 5) Nội dung file ko chứa các dấu ‘,’ và ‘.’
    for line in lines:
        line = line.strip()
        if re.match(r'^[^,]*[^.]*$', line):
            print(line)

def A6(text):
    # 6) Các dòng có chứa chữ “mouse”
    for line in lines:
        line = line.strip()
        if re.match(r'.*mouse*$', line):
            print(line)

def A7(text):
    # 7) Các từ có số chữ ‘a’ bất kỳ và theo sau bởi ‘b’
    for line in lines:
        line = line.strip()
        if re.findall(r'.*a.*b.*', line):
            print(re.findall(r'.*a.*b.*', line))

def A8(text):
    # 8) Domain địa chỉ mail (ví dụ: abc@gmail.com, in gmail.com )
    for line in lines:
        line = line.strip()
        if re.match(r'.*gmail.com$', line):
            print(line)


def A9(text):
    # 9) Nội dung giữa cặp tag <head> </head> (gợi ý: sử dụng open và read để mở và đọc file)
    for line in lines:
        line = line.strip()
        if re.match(r'^<head>.*</head>$', line):
            print(re.sub(r'<head>', '', re.sub(r'</head>', '', line)))

if __name__ == "__main__":
    A1(lines)
    A2(lines)
    A3(lines)
    A4(lines)
    A5(lines)
    A6(lines)
    A7(lines)
    A8(lines)
    A9(lines)
