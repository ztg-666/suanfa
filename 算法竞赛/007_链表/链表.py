class Node:
    def __init__(self, value, name):
        self.value = value
        self.next = None
        self.name = name


a = Node(11,"a")
b = Node(2,"b")
c = Node(3,"c")
d = Node(4,"d")
e = Node(5,"e")
f = Node(6,"f")
a.next = b
head = a

b.next = c
c.next = d
d.next = e
e.next = f





cur = head
while cur.next is not None:
    print(f"当前节点为{cur.name}, 节点值为：{cur.value}，下一个节点为：{cur.next.name}")

    cur = cur.next

