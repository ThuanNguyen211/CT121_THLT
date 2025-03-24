# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

def read_grammar(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Khởi tạo các thành phần của văn phạm
        V = set()  # Tập biến
        T = set()  # Tập ký tự kết thúc
        P = []    # Tập luật sinh
        S = ''    # Ký tự bắt đầu
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('V='):
                V = set(line[2:].strip('{}').split(','))
            elif line.startswith('T='):
                T = set(line[2:].strip('{}').split(','))
            elif line.startswith('S='):
                S = line[2:].strip()
            elif line.startswith('P='):
                rules = line[2:].strip('[]').split(';')
                for rule in rules:
                    if rule:
                        left, right = rule.split('->')
                        P.append((left.strip(), right.strip()))
        
        return V, T, P, S
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_name}")
        return None, None, None, None

def check_left_linear(P):
    for left, right in P:
        # Kiểm tra vế phải có dạng αA hoặc α (A là biến, α là chuỗi ký tự kết thúc)
        if len(right) > 2:
            return False
        if len(right) == 2:
            # Kiểm tra ký tự đầu là chữ thường và ký tự cuối là chữ hoa
            if not (right[0].islower() and right[1].isupper()):
                return False
        elif len(right) == 1:
            # Nếu độ dài là 1, phải là chữ thường
            if not right[0].islower():
                return False
    return True

def check_right_linear(P):
    for left, right in P:
        # Kiểm tra vế phải có dạng Aα hoặc α (A là biến, α là chuỗi ký tự kết thúc)
        if len(right) > 2:
            return False
        if len(right) == 2:
            # Kiểm tra ký tự đầu là chữ hoa và ký tự cuối là chữ thường
            if not (right[0].isupper() and right[1].islower()):
                return False
        elif len(right) == 1:
            # Nếu độ dài là 1, phải là chữ thường
            if not right[0].islower():
                return False
    return True

def check_regular(P):
    """Kiểm tra văn phạm chính quy (tuyến tính phải hoặc tuyến tính trái)"""
    return check_right_linear(P) or check_left_linear(P)

def main(file_name):
    # Đọc văn phạm từ file
    V, T, P, S = read_grammar(file_name)
    if not V:
        return
    
    # Kiểm tra và in kết quả
    print(f"\nKiểm tra {file_name}:")
    print(f"Văn phạm tuyến tính trái: {'True' if check_left_linear(P) else 'False'}")
    print(f"Văn phạm tuyến tính phải: {'True' if check_right_linear(P) else 'False'}")
    print(f"Văn phạm chính quy: {'True' if check_regular(P) else 'False'}")

if __name__ == "__main__":
    main("van_pham_tuyen_tinh_phai.txt")
    main("van_pham_tuyen_tinh_trai.txt")
    main("van_pham_khong_tuyen_tinh.txt")
