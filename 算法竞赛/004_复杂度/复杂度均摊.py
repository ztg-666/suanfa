import time
import random

times = 1000000


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start = time.time()
ans = 0
for i in range(times):
    for i in range(20):
        ans += a[i]

end = time.time()
print(f"1耗时: {end - start:.4f}秒")


start = time.time()


ans = 0
for i in range(times):
    for i in range(1):
        ans += a[i]

end = time.time()
print(f"耗时: {end - start:.4f}秒")

ans = 0
for i in range(times):
    aa = random.randint(1,20)
    for i in range(aa):
        ans += a[i]


end = time.time()
print(f"耗时: {end - start:.4f}秒")
