# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

def check_grammar(string):
    # Định nghĩa văn phạm
    # S -> aA | bB
    # A -> aA | bB | c
    # B -> bB | c
    # Chuỗi hợp lệ {ac, bc, aac, bbc, abac}

    def check_S(string, index):
        if index >= len(string):
            return False
        if string[index] == 'a':
            return check_A(string, index + 1)
        elif string[index] == 'b':
            return check_B(string, index + 1)
        return False
    
    def check_A(string, index):
        if index >= len(string):
            return False
        if string[index] == 'a':
            return check_A(string, index + 1)
        elif string[index] == 'b':
            return check_B(string, index + 1)
        elif string[index] == 'c':
            return index == len(string) - 1
        return False
    
    def check_B(string, index):
        if index >= len(string):
            return False
        if string[index] == 'b':
            return check_B(string, index + 1)
        elif string[index] == 'c':
            return index == len(string) - 1
        return False
    
    return check_S(string, 0)

def main():
    print("Nhập chuỗi cần kiểm tra (chỉ chứa các ký tự a, b, c):")
    string = input().strip()
    
    if check_grammar(string):
        print(f"Chuỗi '{string}' thuộc văn phạm đã cho.")
    else:
        print(f"Chuỗi '{string}' không thuộc văn phạm đã cho.")

if __name__ == "__main__":
    main()