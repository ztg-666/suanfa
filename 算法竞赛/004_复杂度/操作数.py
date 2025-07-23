import time



start = time.time()
ans = 0
n = 100_000_000
for i in range(n):
    ans += 1

end = time.time()
print(f"耗时: {end - start:.4f}秒")

start = time.time()
ans = 0
ans2 = 0
n = 100_000_000
for i in range(n):
    ans += 1
    ans2 += 1

end = time.time()
print(f"耗时: {end - start:.4f}秒")


start = time.time()
ans = 0
ans2 = 0
n = 100_000_000
for i in range(n):
    if n % 2 == 0:
        ans += 1
        ans2 += 1
    if n % 2 == 1:
        ans += 1
end = time.time()
print(f"耗时: {end - start:.4f}秒")
