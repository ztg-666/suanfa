# 将读入的 N 个数从小到大排序后输出。

import random
# def Selection_Sort(a):
#
#     for i in range(len(a)):
#         min_index = i
#         for j in range(i+1,len(a)):
#             if a[j] < a[min_index]:
#                 min_index = j
#         a[i],a[min_index] = a[min_index],a[i]
#         # print(a)
#     return a

# def Bubble_Sort(a):
#     for i in range(len(a)):
#         for j in range(len(a)-1 - i):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#     return a

def Insertion_Sort(a):
    for i in range(1,len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            j -= 1
        # print(a)
    return a


def check(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True
length = 1000
a = [random.randint(0, 100) for _ in range(length)]
# a = Selection_Sort(a)
# a = Bubble_Sort(a)
a = Insertion_Sort(a)
print(check(a))