import time


n = int(input())
start = time.time()
ans = 0
for i in range(n):
    ans +=1
end = time.time()
print(f"1耗时: {end - start:.4f}秒")

ans = 0
start = time.time()
for i in range(n ** 2):
     continue
end = time.time()
print(f"2耗时: {end - start:.4f}秒")

# start = time.time()
# ans = 0
# for i in range(n ** 3):
#      ans+=1
#
# end = time.time()
# print(f"3耗时: {end - start:.4f}秒")


start = time.time()
ans = 0
for i in range(n ** 2):
     ans +=1
ans = 0

for i in range(n * 10000):
     ans +=1

end = time.time()
print(f"4耗时: {end - start:.4f}秒")



start = time.time()

for i in range(n ** 2):
     continue


for i in range(n * 10):
     continue

for i in range(100):
    continue
end = time.time()
print(f"5耗时: {end - start:.4f}秒")