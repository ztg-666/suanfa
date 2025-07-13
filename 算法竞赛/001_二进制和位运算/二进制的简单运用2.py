def print_bin(n):
    bits = ""
    while n > 0:
        # 0b1010
        # 0b0001
        # 0b0000

        #0b101
        #0b001
        if n & 1 == 1:
            bits = "1" + bits
        else:
            bits = "0" + bits
        # 0b101
        n >>= 1
    while len(bits) < 4:
        bits = "0" + bits
    return "0b" + bits


#假设一个房间有四盏灯，初始时全是关着的，即状态为0
a = 0b0000
print(print_bin(a))
while 1:
    # 每次输入一个数，操作一盏灯，就是开变成关，关变成开
    opt = int(input())
    # 9表示结束
    if opt == 9:
        break

    # 1 表示 0001 << (1 - 1) = 0001
    # 0b1101 0b1100
    # 0b0001

    a = a ^ (1 << (opt-1))



    print(print_bin(a))


