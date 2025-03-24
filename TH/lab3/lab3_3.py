# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

import re

def cau1(text):
    # 1) Tìm các từ chứa ký tự thường 'a-z' và số từ '0-9'
    pattern = r'\b[a-z0-9]+\b'
    return re.findall(pattern, text)

def cau2(text):
    # 2) Tìm các từ chứa ký tự 'a' theo sau bởi b (b xuất hiện ít nhất 0 lần)
    pattern = r'\b\w*a\w*b\w*\b'
    return re.findall(pattern, text)

def cau3(text):
    # 3) Tìm các từ bắt đầu bằng 'a', theo sau là ký tự bất kỳ và kết thúc bằng 'b'
    pattern = r'\ba\w*b\b'
    return re.findall(pattern, text)

def cau4(text):
    # 4) Tìm các từ chỉ chứa ký tự thường 'a-z' và '_'
    pattern = r'\b[a-z_]+(?<!_)\b'
    return re.findall(pattern, text)

def cau5(text):
    # 5) Tìm các từ có chiều dài là 5
    pattern = r'\b\w{5}\b'
    return re.findall(pattern, text)

def cau6(text):
    # 6) Tìm các từ có chứa ký tự 'h'
    pattern = r'\b\w*h\w*\b'
    return re.findall(pattern, text)

def cau7(text):
    # 7) Tìm các từ bắt đầu là số từ '0-9'
    pattern = r'\b[0-9]\w*\b'
    return re.findall(pattern, text)

def cau8(text):
    # 8) Tìm các từ có chứa dấu '_' và thay bằng khoảng trắng
    pattern = r'\b\w+_\w+\b'
    return re.sub(pattern, lambda m: m.group().replace('_', ' '), text)

def cau9(text):
    # 9) Chuyển đổi định dạng mm-dd-yy thành dd-mm-yy
    pattern = r'(\d{2})-(\d{2})-(\d{2})'
    return re.sub(pattern, r'\2-\1-\3', text)

if __name__ == "__main__":
    text1 = "Hello123 world abc_123"
    print("1. Từ chứa ký tự thường và số:", cau1(text1))
    
    text2 = "ab abc abbb abcd"
    print("2. Từ chứa 'a' theo sau bởi 'b':", cau2(text2))
    
    text3 = "ab axb a123b"
    print("3. Từ bắt đầu 'a' và kết thúc 'b':", cau3(text3))
    
    text4 = "abc_123 abc_ def_"
    print("4. Từ chỉ chứa ký tự thường và '_':", cau4(text4))
    
    text5 = "hello world abcde"
    print("5. Từ có độ dài 5:", cau5(text5))
    
    text6 = "hello world hi"
    print("6. Từ chứa ký tự 'h':", cau6(text6))
    
    text7 = "123abc 1world 2test"
    print("7. Từ bắt đầu bằng số:", cau7(text7))
    
    text8 = "hello_world test_case"
    print("8. Thay '_' bằng khoảng trắng:", cau8(text8))
    
    text9 = "12-31-23 01-15-24"
    print("9. Chuyển đổi định dạng ngày:", cau9(text9))
