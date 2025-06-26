import time

start = time.time()
ans = 0
for i in range(100_000_000):
    continue

end = time.time()
print(f"耗时: {end - start:.4f}秒")


start = time.time()
ans = 0
for i in range(100_000_000):
    ans += 1

end = time.time()
print(f"耗时: {end - start:.4f}秒")

start = time.time()
ans = 0
ans2 = 0
for i in range(100_000_000):
    ans += 1
    ans2 += 1

end = time.time()
print(f"耗时: {end - start:.4f}秒")
