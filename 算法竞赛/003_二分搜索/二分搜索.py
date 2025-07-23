
# 第一个和第二个一起讲
# 终止条件
# def binary_search1(l, r, key,a):
#     ans = -1
#     while l <= r:
#         # mid = (l + r) // 2
#         mid = (l + r) >> 1
#         if a[mid] == key :
#             ans = mid
#             break
#         elif a[mid] < key:
#             l = mid + 1  # 目标在右半部分
#         else:
#             r = mid - 1  # 目标在左半部分
#     return ans

# a = [3,4,5,6,7]
# #    0 1 2 3 4
# # mid = 2
# # l = 0 r= 1
# print(binary_search1(0, len(a) - 1, 3, a))

# 当我们遇到了在一串数字中有很多相同数字的情况

# aa = [1,2,3,3,3,4,5]
# print(binary_search1(0, len(aa) - 1, 3 , aa))
#
# 有序数组中找>=num的最左位置
def binary_search3(l, r, key,a):
    ans = len(a)
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] >= key:
            ans = mid  # 目标在右半部分
            r = mid - 1
        else:
            l = mid + 1  # 目标在左半部分
    return ans
#
# aa = [1,2,3,3,3,4,5]
# aaa = [1,2,2,2,2]
# print(binary_search3(0, len(aa) - 1, 3 , aa))
# print(binary_search3(0, len(aaa) - 1, 3 , aaa))
# #
# def binary_search33(l, r, key,a):
#     while l <= r:
#         mid = (l + r) >> 1
#         if a[mid] >= key:
#             # 目标在右半部分
#             r = mid - 1
#         else:
#             l = mid + 1  # 目标在左半部分
#     return l
#
# aa = [1,2,3,3,3,4,5]
# aaa = [1,2,2,2,2]
# print(binary_search3(0, len(aa) - 1, 3 , aa))
# print(binary_search3(0, len(aaa) - 1, 3 , aaa))
#
# 有序数组中找<=num的最右位置
def binary_search4(l, r, key,a):
    ans = - 1
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] <= key:
            ans = mid  # 目标在右半部分
            l = mid + 1
        else:
            r = mid - 1  # 目标在左半部分
    return  ans
#
# aa = [1,2,2,3,3,4,5]
# print(binary_search4(0, len(a) - 1, 3 , aa))



