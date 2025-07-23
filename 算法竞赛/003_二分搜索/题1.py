# 大于等于key的食物存储的房间的最右边的房间
def binary_search3(l, r, key,a):
    ans = -2
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] >= key:
            ans = mid  # 目标在右半部分
            r = mid - 1
        else:
            l = mid + 1  # 目标在左半部分
    return ans
n = int(input())
a = list(map(int, input().split()))
key = int(input())

# 最后加个1 因为题目的房间号是从1开始的
print(binary_search3(0, len(a) - 1, key, a) + 1)