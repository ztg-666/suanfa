
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
# a = 0b1010
a = 1
print(print_bin(a))
print(bin(a))