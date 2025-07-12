from collections import deque

stack = deque()  # 初始化

# 压栈
stack.append(10)  # 栈: [10]
stack.append(20)  # 栈: [10, 20]

print(stack[0])

# 弹栈
top = stack.pop() # 返回 20
print(top)


# 查看栈顶
if stack:
    peek = stack[0]  # 返回 10
    print(peek)
