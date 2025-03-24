# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

def cau1(a, b):
    kp = ""
    a1 = a[:2]
    b1 = b[:2]
    kp = b1 + a[2:] + " " + a1 + b[2:]
    print(kp)

def cau2(a):
    kp = ""
    for i in range(0, len(a)):
        if i % 2 == 1:
            kp += a[i]
    print(kp)

def cau3(a):
    kp = a
    temp = ""
    count = 0
    i = 0
    dict = {}
    while i != len(kp) - 1:
        for i in range(i, len(kp)):
            if kp[i] != " ":
                temp += kp[i]
            else:
                i += 1
                break
        if dict == {}:
            dict = {temp, kp.count(temp)}
        else:
            dict.update({temp: kp.count(temp)})
        temp = ""
    print(dict)

def cau4(input):
    # input "def", output "abc"
    a = ["d", "e", "f"]
    b = ["a", "b", "c"]
    output = ""
    for i in range(len(input)):
        for y in a:
            if y == input[i]:
                index = i
        output += b[i]
    print(output)

def cau5(a):
    S = ["0", "1", "2"]
    flag = 1
    for i in range(len(a)):
        if a[i] not in S:
            print(a + ": Chuỗi không hợp lệ")
            flag = 0
    if flag:
        print(a + ": Chuỗi hợp lệ")

def cau6(a):
    list = []
    temp = ""
    i = 0
    while i != len(a) - 1:
        for i in range(i, len(a)):
            if a[i] != " ":
                temp += a[i]
            else:
                i += 1
                break
        list.append(temp)
        temp = ""
    print(list)

def cau7(a):
    i = 0
    list = []
    for i in range(len(a)):
        list.append(a[i])
    print(list)
    for i in list:
        if list.count(i) == 1:
            print(i)
            break

def cau8(a):
    kp = ""
    for i in range(len(a)):
        if a[i] != " ":
            kp += a[i]
    print(kp)

def cau9(a):
    temp = ""
    i = 0
    list = []
    while i != len(a) - 1:
        for i in range(i, len(a)):
            if a[i] != " ":
                temp += a[i]
            else:
                i += 1
                break
        if temp not in list:
            list.append(temp)
        else:
            print(temp)
            break
        temp = ""

def cau10(a):
    max = 0
    x = a[0]
    len_x = 0
    for i in range(1, len(a)):
        if a[i] == x:
            len_x += 1
        else:
            x = a[i]
            if len_x >= max:
                max = len_x
            len_x = 1
    print(len_x)

if __name__ == "__main__":
    cau1("abc", "efg")
    cau2("python")
    cau3("no pain no gain")
    cau4("def")
    cau5("0012")
    cau5("12")
    cau5("123")
    cau6("This is a list")
    cau7("abcdef")
    cau7("abcabcdef")
    cau8("a b c")
    cau9("ab ca ba ca ab bc")
    cau9("ab ca bc ab")
    cau10("1110001110000")
