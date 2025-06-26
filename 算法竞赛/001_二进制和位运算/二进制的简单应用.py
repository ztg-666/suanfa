
def print_bin(n):
    bits = ""
    while n > 0:
        if n & 1 == 1:
            bits = "1" + bits
        else:
            bits = "0" + bits
        n >>= 1
    return "0b" + bits
a = 0b1010
print(print_bin(a))