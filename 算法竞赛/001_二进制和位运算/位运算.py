

a = 0b1010
b = 0b1110
# print(a,b)
# print(bin( a ))
# 1010
# 1110
# 1010
print(bin( a & b ))

# 1010
# 1110
# 1110
print(bin( a | b ))

# 1010
# 1110
# 0100
print(bin( a ^ b))

# 原码：00001010 -> 10
# 原码：10001010 -> -10
# 反码：11110101 -> -10
# 补码：11110110 -> -10
# 11110101
# 11110110
# 10001011 -> -11
# 11110100
# 11110101 -> -11
print(a)
print(~a)

# 1010
# 10100
#  1 0 1 0 0 -> 20
# 16 8 4 2 1
print(bin(a))
print(bin(a<<1))
print(a)
print(a<<2)

# 1010
# 101
#  0 0 1 0 1 -> 5
# 16 8 4 2 1
print(bin(a))
print(bin(a>>1))
print(bin(a>>2))
print(a)
print(a>>1)