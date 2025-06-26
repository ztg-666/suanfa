import time

start = time.time()
a = pow(2, 100_000_000)
end = time.time()
print(f"耗时: {end - start:.4f}秒")

start = time.time()
b = (1 << 100000000)
end = time.time()
print(f"耗时: {end - start:.4f}秒")