import time

start = time.time()
# a = pow(2, 100_000_000)
a = 2 ** 100000000
end = time.time()
print(f"耗时: {end - start:.4f}秒")

start = time.time()
# 1   -> 1
# 10  -> 2
# 100 -> 4
b = (1 << 100000000)
end = time.time()
print(f"耗时: {end - start:.4f}秒")