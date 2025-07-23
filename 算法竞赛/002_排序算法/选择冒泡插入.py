# 将读入的 N 个数从小到大排序后输出。
# https://www.luogu.com.cn/problem/P1177

def Selection_Sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]
        # print(a)
    return a
# def Bubble_Sort(a):
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#     return a

# def Insertion_Sort(a):
#     for i in range(1,len(a)):
#         j = i
#         while j > 0 and a[j] < a[j-1]:
#             a[j],a[j-1] = a[j-1],a[j]
#             j -= 1
#         # print(a)
#     return a
def list_out(a):
    for i in a:
        print(i,end = ' ')

n = int(input())
a = list(map(int, input().split()))
# a = Selection_Sort(a)
# a = Bubble_Sort(a)
# a = Insertion_Sort(a)
# print(a)
list_out(a)