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

m = 0b1101
# 降序遍历 m 的非空子集
s = m
print(print_bin(s))
while s > 0:
  # s 是 m 的一个非空子集
  s = (s - 1) & m
  print(print_bin(s))
