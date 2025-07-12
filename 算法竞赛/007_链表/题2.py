class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


n, m = map(int, input().split())

# 创建初始链表：1 -> 2 -> 3 -> ... -> n
head = Node(1)
nodes = [None] + [head]  # 1索引数组，便于访问
tail = head

for i in range(2, n + 1):
    node = Node(i)
    nodes.append(node)
    tail.next = node
    node.pre = tail
    tail = node

# 处理m个操作
for _ in range(m):
    operation = list(map(int, input().split()))

    if operation[0] == 1:  # 插入操作
        x, y = operation[1], operation[2]

        # 如果y已经在x后面，不需要操作
        if nodes[x].next and nodes[x].next.value == y:
            continue

        # 从当前位置移除节点y
        node_y = nodes[y]

        # 更新y的前驱和后继的连接
        if node_y.pre:
            node_y.pre.next = node_y.next
        else:  # y是头节点
            head = node_y.next

        if node_y.next:
            node_y.next.pre = node_y.pre
        else:  # y是尾节点
            tail = node_y.pre

        # 将节点y插入到节点x后面
        node_x = nodes[x]
        node_y.next = node_x.next
        node_y.pre = node_x

        if node_x.next:
            node_x.next.pre = node_y
        else:  # x原来是尾节点
            tail = node_y

        node_x.next = node_y
    elif operation[0] == 2:
        x, y = operation[1], operation[2]

        # 如果y已经在x后面，不需要操作
        if nodes[x].pre and nodes[x].pre.value == y:
            continue

        # 从当前位置移除节点y
        node_y = nodes[y]

        # 更新y的前驱和后继的连接
        if node_y.pre:
            node_y.pre.next = node_y.next
        else:  # y是头节点
            head = node_y.next

        if node_y.next:
            node_y.next.pre = node_y.pre
        else:  # y是尾节点
            tail = node_y.pre



        node_x = nodes[x]
        node_y.pre = node_x.pre
        node_y.next = node_x

        if node_x.pre:
            node_x.pre.next = node_y
        else:
            head = node_y

        node_x.pre = node_y
    elif operation[0] == 3:
        y = operation[1]
        # 从当前位置移除节点y
        node_y = nodes[y]
        if node_y.pre is None and node_y.next is None:
            continue
        # 更新y的前驱和后继的连接
        if node_y.pre:
            node_y.pre.next = node_y.next
        else:  # y是头节点
            head = node_y.next

        if node_y.next:
            node_y.next.pre = node_y.pre
        else:  # y是尾节点
            tail = node_y.pre


# 输出最终链表
cur = head
result = []
while cur:
    result.append(str(cur.value))
    cur = cur.next

print(' '.join(result))
