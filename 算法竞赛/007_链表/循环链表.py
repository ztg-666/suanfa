class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None

    def append(self, value):
        """在链表末尾添加节点"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # 指向自身形成环
            return

        current = self.head
        while current.next != self.head:  # 遍历到最后一个节点
            current = current.next
        current.next = new_node
        new_node.next = self.head  # 新节点指向头节点形成环

    def prepend(self, value):
        """在链表头部添加节点"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        # 找到尾节点并更新其指向
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        self.head = new_node  # 更新头节点

    def delete(self, key):
        """删除指定值的节点"""
        if self.is_empty():
            return

        # 删除头节点的情况
        if self.head.value == key:
            if self.head.next == self.head:  # 只有一个节点
                self.head = None
            else:
                # 找到尾节点并更新其指向
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  # 尾节点指向新头
                self.head = self.head.next  # 更新头节点
            return

        # 删除中间或尾部节点
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
            if current.value == key:
                prev.next = current.next
                return

    def traverse(self):
        """遍历链表并打印所有元素"""
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")


# 使用示例
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.append(10)
    clist.append(20)
    clist.prepend(5)
    clist.traverse()  # 输出: 5 -> 10 -> 20 -> HEAD

    clist.delete(10)
    clist.traverse()  # 输出: 5 -> 20 -> HEAD
