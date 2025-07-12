from queue import Queue

# 创建队列
q = Queue()

# 入队操作
q.put("A")
q.put("B")
q.put("C")

# 出队操作
print(q.get())  # 输出: A
print(q.get())  # 输出: B

# 检查队列状态
print(q.empty())  # 输出: False
print(q.qsize())  # 输出: 1
