import time


n = int(input())
start = time.time()
for i in range(n):
    continue
end = time.time()
print(f"1耗时: {end - start:.4f}秒")


start = time.time()
for i in range(n ** 2):
     continue
end = time.time()
print(f"2耗时: {end - start:.4f}秒")

start = time.time()

for i in range(n ** 3):
     continue

end = time.time()
print(f"3耗时: {end - start:.4f}秒")


start = time.time()

for i in range(n ** 2):
     continue

for i in range(n * 10000):
     continue

end = time.time()
print(f"4耗时: {end - start:.4f}秒")



start = time.time()

for i in range(n ** 2):
     continue


for i in range(n * 10000):
     continue

for i in range(1000000):
    continue
end = time.time()
print(f"5耗时: {end - start:.4f}秒")