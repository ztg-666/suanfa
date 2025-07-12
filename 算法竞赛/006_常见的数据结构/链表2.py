class Node:
    """链表节点类"""

    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.next = None  # 指向下一个节点的指针


class LinkedList:
    """单向链表类"""

    def __init__(self):
        self.head = None  # 链表头节点

    def append(self, data):
        """在链表末尾添加节点"""
        new_node = Node(data)
        if not self.head:  # 空链表
            self.head = new_node
            return
        current = self.head
        while current.next:  # 遍历到最后一个节点
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """在链表头部添加节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """在指定节点后插入新节点"""
        if not prev_node:
            print("错误：前一个节点不存在")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        """删除包含指定数据的节点"""
        current = self.head

        # 删除头节点
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:  # 未找到节点
            return

        prev.next = current.next
        current = None

    def display(self):
        """打印链表内容"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 使用示例
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(10)  # 链表: 10 -> None
    llist.append(20)  # 链表: 10 -> 20 -> None
    llist.prepend(5)  # 链表: 5 -> 10 -> 20 -> None

    # 在头节点后插入
    llist.insert_after(llist.head, 7)  # 链表: 5 -> 7 -> 10 -> 20 -> None

    llist.delete(10)  # 链表: 5 -> 7 -> 20 -> None
    llist.display()  # 输出: 5 -> 7 -> 20 -> None
