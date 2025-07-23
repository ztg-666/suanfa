import random
import time
def Bubble_Sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
def Bubble_Sort_optimize(a):

    for i in range(len(a)):
        flag = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                flag = True
        if not flag:
            break
    return a

length = 10000
a = [random.randint(0, 1000) for _ in range(length)]
b = a[:]
start = time.time()
a = Bubble_Sort(a)
end = time.time()
print(f"耗时: {end - start:.4f}秒")
start = time.time()
b = Bubble_Sort_optimize(b)
end = time.time()
print(f"耗时: {end - start:.4f}秒")
# a = Bubble_Sort(a)
# a = Insertion_Sort(a)
