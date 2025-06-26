def binary_search1(l, r, key,a):
    while l <= r:
        # mid = (l + r) // 2
        mid = (l + r) >> 1
        if a[mid] == key :
            return mid
        elif a[mid] < key:
            l = mid + 1  # 目标在右半部分
        else:
            r = mid - 1  # 目标在左半部分


a = [1,2,3,4,5]
print(binary_search1(0, len(a) - 1, 3 , a))


def binary_search2(l, r, key,a):
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] == key :
            return mid
        elif a[mid] < key:
            l = mid + 1  # 目标在右半部分
        else:
            r = mid - 1  # 目标在左半部分


aa = [1,2,2,3,3,4,5]
print(binary_search2(0, len(a) - 1, 3 , aa))

# 有序数组中找>=num的最左位置
def binary_search3(l, r, key,a):
    ans = - 1
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] >= key:
            ans = mid  # 目标在右半部分
            r = mid - 1
        else:
            l = mid + 1  # 目标在左半部分
    return ans

aa = [1,2,2,3,3,4,5]
aaa = [1,2,2,4,5]
print(binary_search3(0, len(a) - 1, 3 , aa))
print(binary_search3(0, len(a) - 1, 3 , aaa))

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

aa = [1,2,2,3,3,4,5]
print(binary_search4(0, len(a) - 1, 3 , aa))



