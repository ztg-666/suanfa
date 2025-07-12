class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node = Node(1)
head = node

q = int(input())

for i in range(q):
    que = list(map(int, input().split()))
    # print(que)
    if que[0] == 1:
        n = que[1]
        v = que[2]
        node = Node(v)
        cur = head
        while cur is not None:
            if cur.value == n:
                node.next = cur.next
                cur.next = node
                break
            else:
                cur = cur.next
    elif que[0] == 2:
        cur = head
        v = que[1]
        while cur.next is not None:
            if cur.value == v:
                print(cur.next.value)
                break
            else:
                cur = cur.next
        else:
            print(0)
    elif que[0] == 3:
        cur = head
        v = que[1]
        while cur.next is not None:
            if cur.value == v:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next